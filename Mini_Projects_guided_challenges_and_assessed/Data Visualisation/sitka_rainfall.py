from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('Chapter_16_Downloading_Data\\sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# # Extract dates and rainfall temperatures

# dates, rainfall = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     rain = float(row[5])
#     dates.append(current_date)
#     rainfall.append(rain)

# # # Plot the rainfall.
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(dates, rainfall, color='red')

# # # Format plot
# ax.set_title("Daily Rainfall 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Rainfall", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()