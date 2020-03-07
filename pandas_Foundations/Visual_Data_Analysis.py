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

#===================================================================================

#Plotting Scatter Graph 
# Generate a scatter plot
# Kind =Scatter , means scatter plots
df.plot(kind='scatter', x='hp', y='mpg', s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()


#====================================================================================
# While pandas can plot multiple columns of data in a single figure, 
# making plots that share the same x and y axes, there are cases where
# two columns cannot be plotted together because their units do not match.
# The .plot() method can generate subplots for each column being plotted. Here, each plot will be scaled independently
# Make a list of the column names to be plotted: cols
#The kind of plot to produce:
#‘line’ : line plot (default)
#‘bar’ : vertical bar plot
#‘barh’ : horizontal bar plot
#‘hist’ : histogram
#‘box’ : boxplot
#‘kde’ : Kernel Density Estimation plot
#‘density’ : same as ‘kde’
#‘area’ : area plot
#‘pie’ : pie plot
#‘scatter’ : scatter plot
#‘hexbin’ : hexbin plot.
cols = list(['weight','mpg'])

# Generate the box plots
df[cols].plot(kind='box',subplots=True)

# Display the plot
plt.show()

#======================================================================================
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', bins=30, normed=True, range=(0,.3))
plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', bins=30, cumulative=True, normed=True, range=(0,.3))
plt.show()
