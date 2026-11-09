import matplotlib.pyplot as p

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

p.plot(x, y, marker='o')

p.title("Line Plot using Matplotlib")
p.xlabel("X-axis")
p.ylabel("Y-axis")
p.grid(True)

p.show()