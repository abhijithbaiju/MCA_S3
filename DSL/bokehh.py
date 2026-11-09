from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

p = figure(title="Line Plot using Bokeh",
           x_axis_label="X-axis",
           y_axis_label="Y-axis")

p.line(x, y, line_width=2, color="blue")

output_file("lineplot.html")
show(p)