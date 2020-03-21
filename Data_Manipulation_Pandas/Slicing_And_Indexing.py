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
#=======================================================================================
#You can only slice an index if the index is sorted (using .sort_index()).
#To slice at the outer level, first and last can be strings.
#To slice at inner levels, first and last should be tuples.
#If you pass a single slice to .loc[], it will slice the rows.
# Add a year column to temperatures
temperatures['year']=temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c",index=['country','city'],columns='year')

# See the result
print(temp_by_country_city_vs_year)

#=================================================================================
# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"),"2005":"2010"]
#=========================================================================================
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis="index")
# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year>=mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city<=mean_temp_by_city.min()])
