import matplotlib.pyplot as plt

x_values = range(1, 11)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Set chart title and label axises.
ax.set_title("Cubed Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)

# Set the range for each axis.
ax.axis([0, 11, 0, 2_000])
# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
