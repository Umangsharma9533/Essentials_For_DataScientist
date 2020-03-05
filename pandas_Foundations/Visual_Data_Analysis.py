#Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a list of y-axis column names: y_columns
y_columns = list(['AAPL','IBM'])

# Generate a line plot
# Will plot 2 different lines with respect to Month
df.plot(x='Month', y=y_columns)

# Add the title

plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()
