# Read in the file: df1
df1 = pd.read_csv(data_file)

# Create a list of the new column labels: new_labels
new_labels = list(['year','population'])

# Read in the file, specifying the header and names parameters: df2
# Header = 0(row number) , means first row of the file is not header..should be used as a index for a dataFrame
# Header=3 , means 3rd row of a dataframe to be used as a header for the table/dataframe
df2 = pd.read_csv(data_file, header=0, names=new_labels)

# Print both the DataFrames
print(df1)
print(df2)

#===============================================================================================
More about read_csv() with different  parameters
# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head())

# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())

# Save the cleaned up DataFrame to a CSV file without the index
#index = False , will force not to use first column as a index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('file_clean.xlsx', index=False)


#==================================================================================
#Plotting using Pandas
# Create a plot with color='red'
df.plot(color='red')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()

#==============================================================================
# Plot all columns (default)
# We will have a common plot diagram for all the columns
df.plot()
plt.show()

# Plot all columns as subplots
#subplots=True , means we will have main plotting divide into 3 mini subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
#Will plot a single columns
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()
