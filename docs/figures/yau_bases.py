from bokeh.plotting import figure, output_file, save, show
from bokeh.models import Arrow, OpenHead, NormalHead, VeeHead
from bokeh.layouts import gridplot

output_file("yau_bases.html")

p = figure(plot_width=500, plot_height=350, title="Yau's vectors")

# plot the lines
p.line(x=[0, 0.5], y=[0, (3**0.5) / 2], color="red", legend="T")
p.line(x=[0, (3**0.5) / 2], y=[0, 0.5], color="black", legend="C")
p.line(x=[0, (3**0.5) / 2], y=[0, -0.5], color="green", legend="G")
p.line(x=[0, 0.5], y=[0, -(3**0.5) / 2], color="blue", legend="A")


# plot the arrows
p.add_layout(Arrow(end=OpenHead(size=10), line_color="blue",
                   x_start=0, y_start=0, x_end=0.5, y_end=-(3**0.5) / 2))
p.add_layout(Arrow(end=OpenHead(size=10), line_color="red",
                   x_start=0, y_start=0, x_end=0.5, y_end=(3**0.5) / 2))
p.add_layout(Arrow(end=OpenHead(size=10), line_color="green",
                   x_start=0, y_start=0, x_end=(3**0.5) / 2, y_end=-0.5))
p.add_layout(Arrow(end=OpenHead(size=10), line_color="black",
                   x_start=0, y_start=0, x_end=(3**0.5) / 2, y_end=0.5))

# configure the plot
p.xaxis.ticker = [0, 0.5, (3**0.5) / 2]
p.yaxis.ticker = [-(3**0.5) / 2, -0.5, 0, 0.5, (3**0.5) / 2]
p.toolbar_location = None
p.legend.location = "top_left"

save(p)
