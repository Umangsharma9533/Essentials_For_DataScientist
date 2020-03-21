#You'll be exploring temperatures, a DataFrame of average temperatures in cities around the world. pandas is loaded as pd.
# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))



# Make a list of cities to subset on
cities = list(["Moscow","Saint Petersburg"])

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]

print(temperatures_ind.loc[cities])

#==============================================================================
#Multi Level Inedexing
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])
#================================================================================
#Sorted! Sorting index values is similar to sorting values in columns, exectp that you call .sort_index() instead of .sort_values().
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city",ascending=True))
# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country","city"],ascending=[True,False]))
#==================================================================================
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Incorrectly subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan","Lahore"):("Russia","Moscow")])
#======================================================================================
#You've seen slicing DataFrames by rows and by columns, but since DataFrames are two dimensional objects it is
#often natural to slice both dimensions at once. That is, by passing two arguments to .loc[], you can subset by 
#rows and columns in one go.
#pandas is loaded as pd. temperatures_srt is indexed by country and city, has a sorted index, and is available.
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"): ("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"): ("Iraq", "Baghdad"),"date":"avg_temp_c"])

#===============================================================================================
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
print(temperatures[(temperatures["date"]>="2010") & (temperatures["date"]<"2012")])

# Set date as an index
temperatures_ind = temperatures.set_index('date')

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["Aug 2010":"Feb 2011"])
