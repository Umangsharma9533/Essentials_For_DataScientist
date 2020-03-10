import matploltlib.pyplot as plt
#Plot a line with plot()
plt.plot(xvalue,y_value)
#Plot a scatter Graph
plt.scatter(x_value,y_value)
#Plot a histogram
#bins: In how many category data to be divided, by default its 10
plt.hist(value_to_plot, bins=11)
#Display any graph plotted above
plt.show()

#=====================================================
# Build histogram with 5 bins
plt.hist(life_exp, bins=5)
# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)

# Show and clean up again
plt.show()
plt.clf()
#====================================================
# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins=15)

# Show and clear plot again
plt.show()
plt.clf()


#=========================================================
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

# Add title


# After customizing, display the plot
plt.show()

#=====================================================================
# Import numpy as np
import numpy as np
# Store pop as a numpy array: np_pop
np_pop=np.array(pop)

# Double np_pop
np_pop=np_pop*2

# Update: set s argument to np_pop
# Will increase the size of the dot we plot
plt.scatter(gdp_cap, life_exp, s = pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

#=================================================================
#add different  color to different country to make it more diffrentiable
#alpha value ranges from 0 to 1 , 0 means transparent and 1 is opaque
