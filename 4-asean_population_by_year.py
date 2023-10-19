import csv
import matplotlib.pyplot as plt
import numpy as np
from main import population_reader,ASEAN_Countries

asean_population = { key : [] for key in ASEAN_Countries}

# Dictionary to store ASEAN countries population over the years
population = {}
for row in population_reader:
    year = row['Year']
    country = row['Region']
    if year >= '2004' and year <= '2014' and country in ASEAN_Countries:
        asean_population[country].append(row['Population'])

asean_population = {key: value for key, value in asean_population.items() if value}

for country in asean_population:
    print(country , "-----")
    print(asean_population[country])
    print()
    

# Plotting the grouped bar chart
years = [str(i) for i in range(2004, 2015)]
fig, ax = plt.subplots()
bar_width = 0.1                 # width of each bar
pos = np.arange(len(years))     # creates an array of values from 0 to the length of the years.

# [i * bar_width] adds an offset to the x-coordinates of the bars for each country to pos.
# this is done to plot bars on correct position on x-axis 
for i, country in enumerate(asean_population):
    ax.bar(pos + i * bar_width, asean_population[country], width=bar_width, label=country)

# Adding labels and title
ax.set_xlabel('Years')
ax.set_ylabel('Population')
ax.set_title('ASEAN Population from 2004 to 2014')
ax.set_xticks(pos + bar_width * (len(asean_population) / 2 - 0.5))    # to ensure proper positioning of the years on the x-axis.
ax.set_xticklabels(years)       # x-axis labels
ax.legend()

# Display the plot
plt.show()
