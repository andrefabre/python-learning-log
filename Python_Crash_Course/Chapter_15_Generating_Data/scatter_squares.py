#-------------------------------------------------------------------------------
# To plot a single point, pass the single x- and y-values of the point to scatter():
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=200)

# # Set chart title and label axises.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# # Set size of tick lablels.
# ax.tick_params(labelsize=14)

# plt.show()

#-------------------------------------------------------------------------------
# Plotting a series of points with scatter():
#-------------------------------------------------------------------------------
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Set chart title and label axises.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_000_000])
# Set size of tick labels.
ax.tick_params(labelsize=14)

# plt.show()
plt.savefig("squares_plot.png", bbox_inches='tight')