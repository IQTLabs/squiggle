import math

import click
from Bio import SeqIO
from tqdm import tqdm

from bokeh.plotting import figure, show, save, output_file
from bokeh.palettes import small_palettes
from bokeh.layouts import gridplot
from bokeh.models import annotations
from bokeh.resources import INLINE

from squiggle import transform

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option("-f", type=click.Path(dir_okay=False, exists=True), multiple=True, help="The FASTA file whose sequences are to be visualized. May be repeated to visualize multiple files.")
@click.option("-w", "--width", default=1, type=float, help="The width of the line. Defaults to 1.")
@click.option("-p", "--palette", type=str, default="Category10", help="Which color palette to use. Choose from bokeh.pydata.org/en/latest/docs/reference/palettes.html. Defaults to Category20.")
@click.option("--color/--no-color", default=True, help="Whether to plot the visualizations in color.")
@click.option('--hide/--no-hide', default=True, help="Whether to hide sequences when clicked in the legend. Defaults to false if plotting one sequence and true if plotting multiple.")
@click.option('--bar/--no-bar', default=True, help="Whether to show a progress bar when processing multiple sequences. Defaults to true.")
@click.option("-t", "--title", type=str, help="A title to display when plotting sequences together.")
@click.option("--separate", is_flag=True, help="Whether to plot the visualizations separately.")
@click.option("-c", "--cols", default=0, type=int, help="The number of columns when plotting separately. Defaults to a the closest to square layout as possible.")
@click.option("--link-x/--no-link-x", default=True, help="Whether to link the x axes for separate plotting. Defaults to true.")
@click.option("--link-y/--no-link-y", default=False, help="Whether to link the y axes for separate plotting. Defaults to false.")
@click.option("-o", "--output", type=click.Path(dir_okay=False, exists=False), help="The output file for the visualization. If not provided, will open visualization in browser. The filetype must be .html")
@click.option("--offline", is_flag=True, default=False, help="Whether to include the resources needed to plot offline when outputting to file. Defaults to false.")
@click.option('--method', type=click.Choice(['squiggle', 'gates', "yau"]), default="squiggle", help="The visualization method.")
def visualize(f, width, palette, color, hide, bar, title, separate, cols, link_x, link_y, output, offline, method):

    # check filetype
    if f is None:
        raise ValueError("Must provide FASTA file.")

    # handle selecting the palette
    palette = small_palettes[palette]

    # get all the sequences
    seqs = [record for _f in f for record in SeqIO.parse(_f, "fasta")]

    axis_labels = {
        "squiggle": {"x": "position (BP)",
                     "y": None},
        "gates": {"x": "C-G axis",
                  "y": "A-T axis"},
        "yau": {"x": None,
                "y": None},
    }

    fig_count = len(seqs) if separate else 1
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

        fig.append(figure(x_axis_label=axis_labels[method]["x"],
                          y_axis_label=axis_labels[method]["y"],
                          title=title,
                          x_range=x_range,
                          y_range=y_range))

    # show a progress bar if processing multiple files
    if len(seqs) > 1 and bar:
        seqs = tqdm(seqs, unit=" seqs", leave=False)

    for i, seq in enumerate(seqs):
        # perform the actual transformation
        transformed = transform(seq.seq, method=method)

        # figure (no pun intended) which figure to plot the data on
        if separate:
            _fig = fig[i]
            _fig.title = annotations.Title()
            _fig.title.text = seq.name
        else:
            _fig = fig[0]

        # do the actual plotting
        _fig.line(x=transformed[0],
                  y=transformed[1],
                  line_width=width,
                  legend=seq.name if color and not separate else None,
                  color=palette[i + 1 if i > 2 else 3][i] if color else "black")

        # set up the legend
        _fig.legend.location = "top_left"
        if len(f) > 1 and hide:
            _fig.legend.click_policy = "hide"

    seqs.close()
    print("Generating graph...")

    # lay out the figure
    if separate:
        plot = gridplot(fig, ncols=math.ceil(len(fig)**0.5) if cols == 0 else cols) # note that 0 denotes the automatic default
    else:
        plot = fig[0]

    if output is not None and output.endswith(".html"):
        output_file(output)
        save(plot, resources=INLINE if offline else None)
    else:
        show(plot)


if __name__ == '__main__':
    visualize()
