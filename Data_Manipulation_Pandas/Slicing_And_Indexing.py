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
temperatures_ind = temperatures.set_index(["country","city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = temperatures_ind.loc[[('Brazil','Rio De Janeiro'),('Pakistan','Lahore')]]

# Subset for rows to keep
print(rows_to_keep)
