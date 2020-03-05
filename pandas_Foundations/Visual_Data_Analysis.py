#Import Libraries
import pandas as pd

# Create a list of y-axis column names: y_columns
y_columns = list(['AAPL','IBM'])

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.plot('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()
