from bokeh.plotting import figure, output_file, save
from bokeh.models import Arrow, OpenHead, NormalHead, VeeHead
from bokeh.layouts import row

output_file("squiggle_vectors.html")

p0 = figure(plot_width=250, plot_height=250, title="Bit 0")
p0.segment(x0=[0], y0=[0], x1=[0.5],
           y1=[-0.5], line_width=0)
p0.add_layout(Arrow(end=OpenHead(size=10),
                    x_start=0, y_start=0, x_end=0.5, y_end=-0.5))
p0.xaxis.ticker = [0, 0.5]
p0.yaxis.ticker = [0, -0.5]
p0.toolbar_location = None

p1 = figure(plot_width=250, plot_height=250, title="Bit 1")
p1.segment(x0=[0], y0=[0], x1=[0.5],
           y1=[0.5], line_width=0)
p1.add_layout(Arrow(end=OpenHead(size=10),
                    x_start=0, y_start=0, x_end=0.5, y_end=0.5))
p1.xaxis.ticker = [0, 0.5]
p1.yaxis.ticker = [0, 0.5]
p1.toolbar_location = None

save(row(p0, p1))
