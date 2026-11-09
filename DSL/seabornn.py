import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

sns.lineplot(x=x, y=y, marker='o')

plt.title("Line Plot using Seaborn")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()