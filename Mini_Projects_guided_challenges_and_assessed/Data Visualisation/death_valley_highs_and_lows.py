from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('Chapter_16_Downloading_Data\\death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     # print(index, column_header)
#     if column_header == "TMAX":
#         high_index = index
#         #print(high_index)
#     if column_header == "TMIN":
#         low_index = index
#         #print(low_index)

# Extract dates and high temperatures

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(high_index)
        low = int(low_index)
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
#ax.set_ylim(0, 100)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()