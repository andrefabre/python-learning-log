from die import Die
import plotly.express as px
# import plotly.io as pio

# pio.renderers.default = 'browser'

# Create a D6
die = Die()

# Make some rolls, and store results in a list
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# Refactor with list comprehension
results = [die.roll() for roll_num in range(1000)]

# Analyse the results.
# frequencies = []
poss_results = range(1, die.num_sides+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# Refactor with list comprehension
frequencies = [results.count(value) for value in poss_results]
# Visualise the results
title = "Results of Rolling One D6 1,000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

#print(frequencies)
