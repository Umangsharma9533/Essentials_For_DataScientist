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
