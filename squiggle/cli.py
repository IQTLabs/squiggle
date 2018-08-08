import math

import click
from pyfaidx import Fasta
from tqdm import tqdm
from box import Box

from bokeh.plotting import figure, show, save, output_file
from bokeh.palettes import small_palettes
from bokeh.layouts import gridplot
from bokeh.models import annotations
from bokeh.resources import INLINE

from squiggle import transform

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument("FASTA", type=click.Path(dir_okay=False, exists=True), nargs=-1)
@click.option("-w", "--width", default=1, type=float, help="The width of the line. Defaults to 1.")
@click.option("-p", "--palette", type=str, default="Category10", help="Which color palette to use. Choose from bokeh.pydata.org/en/latest/docs/reference/palettes.html. Defaults to Category10.")
@click.option("--color/--no-color", default=True, help="Whether to plot the visualizations in color.")
@click.option('--hide/--no-hide', default=False, help="Whether to hide sequences when clicked in the legend. Defaults to false if plotting one sequence and true if plotting multiple.")
@click.option('--bar/--no-bar', default=True, help="Whether to show a progress bar when processing multiple sequences. Defaults to true.")
@click.option("-t", "--title", type=str, help="A title to display when plotting sequences together.")
@click.option("--separate", is_flag=True, help="Whether to plot the visualizations separately.")
@click.option("-c", "--cols", default=0, type=int, help="The number of columns when plotting separately. Defaults to a the closest to square layout as possible.")
@click.option("--link-x/--no-link-x", default=True, help="Whether to link the x axes for separate plotting. Defaults to true.")
@click.option("--link-y/--no-link-y", default=False, help="Whether to link the y axes for separate plotting. Defaults to false.")
@click.option("-o", "--output", type=click.Path(dir_okay=False, exists=False), help="The output file for the visualization. If not provided, will open visualization in browser. The filetype must be .html")
@click.option("--offline", is_flag=True, default=False, help="Whether to include the resources needed to plot offline when outputting to file. Defaults to false.")
@click.option('--method', type=click.Choice(['squiggle', 'gates', "yau", "yau-bp", "randic", "qi"]), default="squiggle", help="The visualization method.")
@click.option("-d", "--dimensions", nargs=2, type=int, metavar='WIDTH HEIGHT', help="The width and height of the plot, respectively. If not provided, will default to 750x500.")
@click.option("--skip/--no-skip", default=False, help="Whether to skip any warnings. Defaults to false.")
@click.option('--mode', type=click.Choice(['seq', 'file', "auto"]), default="auto", help="Whether to treat each sequence or file as the individual object. Defaults to automatic selection.")
@click.option("--legend-loc", type=click.Choice(["top_left", "top_center", "top_right", "center_right", "bottom_right", "bottom_center", "bottom_left", "center_left", "center"]), default="top_left", help="Where to put the legend, if applicable. Defaults to top left.")
@click.option("--output-backend", type=click.Choice(["canvas", "svg", "webgl"]), default="canvas", help="Which output backend to use while plotting. Defaults to canvas.")
@click.option("-s", "--downsample", type=int, default=1, help="The downsampling factor. Useful for handling large sequences. Default value is 1.")
def visualize(fasta, width, palette, color, hide, bar, title, separate, cols, link_x, link_y, output, offline, method, dimensions, skip, mode, legend_loc, output_backend, downsample):
    # check filetype
    if fasta is None:
        raise ValueError("Must provide FASTA file.")

    # handle selecting the palette
    palette = small_palettes[palette]

    # handle setting the dimensions automatically if not specified
    if not dimensions:
        dimensions = (750, 500)

    if len([record for _f in fasta for record in Fasta(_f)]) > len(palette) and mode != "file":
        if len(fasta) > 1 and mode == "auto":
            if not skip:
                print("Visualizing each file in separate color. To override, provide mode selection.")
            mode = "file"
        else:
            print("Visualizing each sequence in black.")
            color = False
    elif mode == "auto":
        mode = "seq"

    # get all the sequences
    seqs = []
    color_counter = 0
    warned = False
    for i, _f in enumerate(fasta):
        for j, seq in enumerate(Fasta(_f, sequence_always_upper=True)):
            seqs.append(Box(color=palette[color_counter + 1 if color_counter > 2 else 3][color_counter] if color else "black",
                            name=_f if mode == "file" else seq.name,
                            raw_seq=str(seq)))

            # check the length of the seq
            if len(seq) > 10000 and not skip and not warned and downsample == 1:
                click.confirm("You are plotting a long sequence ({} bp). This may be very slow, although downsampling might help. "
                              "Do you want to continue?".format(len(seq)), abort=True)
                warned = True

            if mode == "seq":
                color_counter += 1
        if mode == "file":
            color_counter += 1

    # warn if plotting a large number of seqs
    if len(seqs) > 500 and not skip:
        click.confirm("You are plotting a large number of sequences ({}). This may be very slow, although downsampling might help. "
                      "Do you want to continue?".format(len(seqs)), abort=True)

    # warn if using a bad method
    if max([len(seq.raw_seq) for seq in seqs]) > 25 and method in ["qi", "randic"] and not skip:
        click.confirm("This method is not well suited to a sequence of this length. "
                      "Do you want to continue?", abort=True)

    axis_labels = {
        "squiggle": {"x": "position (BP)",
                     "y": None},
        "gates": {"x": "C-G axis",
                  "y": "A-T axis"},
        "yau": {"x": None,
                "y": None},
        "yau-bp": {"x": "position (BP)",
                   "y": None},
        "randic": {"x": "position (BP)",
                   "y": "nucleotide"},
        "qi": {"x": "position (BP)",
               "y": "dinucleotide"}
    }

    # the number of figures to draw is either the number of sequences or files (or 1)
    if separate:
        if mode == "seq":
            fig_count = len(seqs)
        elif mode == "file":
            fig_count = len(fasta)
    else:
        fig_count = 1

    fig = []
    for i in range(fig_count):

        # link the axes, if requested
        if i > 0 and link_x:
            x_range = fig[i - 1].x_range
        else:
            x_range = None
        if i > 0 and link_y:
            y_range = fig[i - 1].y_range
        else:
            y_range = None

        # the y axes for randic and qi are bases
        if method == "randic":
            y_range = ["A", "T", "G", "C"]
        elif method == "qi":
            y_range = ['AA',
                       'AC',
                       'AG',
                       'AT',
                       'CA',
                       'CC',
                       'CG',
                       'CT',
                       'GA',
                       'GC',
                       'GG',
                       'GT',
                       'TA',
                       'TC',
                       'TG',
                       'TT']

        fig.append(figure(x_axis_label=axis_labels[method]["x"],
                          y_axis_label=axis_labels[method]["y"],
                          title=title,
                          x_range=x_range,
                          y_range=y_range,
                          plot_width=dimensions[0],
                          plot_height=dimensions[1],
                          output_backend=output_backend))

    # show a progress bar if processing multiple files
    if len(seqs) > 1 and bar:
        _seqs = tqdm(seqs, unit=" seqs", leave=False)
    else:
        _seqs = seqs

    for i, seq in enumerate(_seqs):
        # perform the actual transformation
        transformed = transform(seq.raw_seq, method=method)
        transformed = (transformed[0][::downsample], transformed[1][::downsample])

        # figure (no pun intended) which figure to plot the data on
        if separate:
            if mode == "seq":
                _fig = fig[i]
            elif mode == "file":
                _fig = fig[fasta.index(seq.name)]

            # add a title to the plot
            _fig.title = annotations.Title()
            if mode == "seq":
                _fig.title.text = seq.name
            elif mode == "file":
                _fig.title.text = click.format_filename(seq.name, shorten=True)
        else:
            _fig = fig[0]
            _fig.title = annotations.Title()

            # if only plotting on one figure, set up the title
            if title:
                _fig.title.text = title
            elif len(seqs) > 1 and not title and len(fasta) == 1:
                _fig.title.text = click.format_filename(fasta[0], shorten=True)
            elif len(seqs) == 1:
                # if just plotting one sequence, title it with the name of the sequence
                _fig.title.text = seq.name

        # randic and qi method's have categorical y axes
        if method == "randic":
            y = list(seq.raw_seq)
        elif method == "qi":
            y = [seq.raw_seq[i:i + 2] for i in range(len(seq.raw_seq))]
            y = [str(i) for i in y if len(i) == 2]
        else:
            y = transformed[1]

        # figure out whether to add a legend
        if (separate or not color or mode == "file" or len(seqs) == 1) and not hide:
            legend = None
        else:
            legend = click.format_filename(seq.name, shorten=True)

        # optimization for comparing large FASTA files without hiding
        try:
            if mode == "file" and seqs[i + 1].color != seq.color and not separate:
                legend = click.format_filename(seq.name, shorten=True)
        except IndexError:
            if mode == "file" and not separate:
                legend = click.format_filename(seq.name, shorten=True)

    # do the actual plotting
        _fig.line(x=transformed[0],
                  y=y,
                  line_width=width,
                  legend=legend,
                  color=seq.color)

        # set up the legend
        _fig.legend.location = legend_loc
        if hide:
            _fig.legend.click_policy = "hide"

    # clean up the tqdm bar
    try:
        _seqs.close()
    except AttributeError:
        pass

    # lay out the figure
    if separate:
        plot = gridplot(fig,
                        ncols=math.ceil(len(fig)**0.5) if cols == 0 else cols,
                        toolbar_options=dict(logo=None)) # note that 0 denotes the automatic default
    else:
        plot = fig[0]

    if output is not None and output.endswith(".html"):
        output_file(output, title="Squiggle Visualization" if title is not None else title)
        save(plot, resources=INLINE if offline else None)
    else:
        show(plot)


if __name__ == '__main__':
    visualize()
