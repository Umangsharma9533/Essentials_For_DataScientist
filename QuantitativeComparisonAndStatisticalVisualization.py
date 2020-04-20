fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index,medals['Gold'])

# Set the x-axis tick labels to the country names
#this will roate the labels on x axis by 90 degree
ax.set_xticklabels(medals.index,rotation=90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()

#=========================================================
# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals['Gold'], label="Gold")

# Stack bars for "Silver" on top with label "Silver"
# Will overlap on bar over another
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], label='Silver')

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals['Bronze'] ,bottom=medals['Gold']+medals['Silver'], label='Bronze')

# Display the legend
# will display in the top right corner of a graph about the color and the value that particular color represent
ax.legend()

plt.show()

#================================================
fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()
