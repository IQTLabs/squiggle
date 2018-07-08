from bokeh.plotting import figure, output_file, save, show
from bokeh.layouts import gridplot

output_file("squiggle_bases.html")

A = figure(plot_width=250, plot_height=250, title="A")
A.line(x=[0, 0.5, 1], y=[0, 0.5, 0], color="black")
A.xaxis.ticker = [0, 0.5, 1]
A.yaxis.ticker = [0, 0.5]
A.toolbar_location = None

T = figure(plot_width=250, plot_height=250, title="T")
T.line(x=[0, 0.5, 1], y=[0, -0.5, -1], color="black")
T.xaxis.ticker = [0, 0.5, 1]
T.yaxis.ticker = [0, -0.5, -1.0]

G = figure(plot_width=250, plot_height=250, title="G")
G.line(x=[0, 0.5, 1], y=[0, 0.5, 1], color="black")
G.xaxis.ticker = [0, 0.5, 1]
G.yaxis.ticker = [0, 0.5, 1.0]

C = figure(plot_width=250, plot_height=250, title="C")
C.line(x=[0, 0.5, 1], y=[0, -0.5, 0], color="black")
C.xaxis.ticker = [0, 0.5, 1]
C.yaxis.ticker = [0, -0.5]


p = gridplot([[A, T], [G, C]], toolbar_location=None)

save(p)
