# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates=True, index_col='date')
# Read the date from the csv and parse that as a date so using panda we can do that as done above

#================================================
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index,climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()

#====================================================
#To see graph in more details by zoom in the data
import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig,ax=plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change['1970-01-01':'1979-12-31']

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()

#===================================================
import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig,ax=plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change['co2'], color='blue')

# Create a twin Axes that shares the x-axis
#Means ax ,ax2 will have x axis in common and y-axis will change
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change['relative_temp'], color='blue')
# Means the color of the y axis will change for ax in the labelling
ax.tick_params('y', colors=color)
plt.show()
