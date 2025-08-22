from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_name = 'death_valley_2021_simple.csv'
path = Path(file_name)
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Get station name from path
if "sitka" in file_name:
    station_name = "Sitka"
elif "death" in file_name:
    station_name = "Death Valley"
    
for index, column_header in enumerate(header_row):
    # print(index, column_header)
    if column_header == "TMAX":
        high_index = index
    if column_header == "TMIN":
        low_index = index
    if column_header == "DATE":
        date_index = index

# Extract dates and high temperatures

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        high = int(row[high_index])
        low = int(row[low_index])
    except ValueError:
        print(f"Missing data for {current_date}")
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
current_year = datetime.strptime(row[date_index], '%Y-%m-%d').year
ax.set_title(f"{station_name} - Daily High and Low Temperatures, {current_year}", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
# y_min = min(lows)-10
y_max = max(highs)+10
ax.set_ylim(0, y_max)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()