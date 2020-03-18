# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

#=======================================================================
# Sort homelessness by individual

homelessness_ind = homelessness.sort_values('individuals',ascending=True)

# Print the top few rows
print(homelessness_ind)

#=======================================================================
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(by=['region','family_members'],ascending=[True,False])
# Print the top few rows
print(homelessness_reg_fam.head())
#=======================================================================
# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals','state']]

# Print the head of the result
print(ind_state.head())
#========================================================================
#Subsetting Rows
# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals','state']]

# Print the head of the result
print(ind_state.head())
#=========================================================================
# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region']=='Mountain']

# See the result
print(mountain_reg)
#=========================================================================
# Filter for rows where family_members is less than 1000 
# and region is Pacific
ab=homelessness['family_members']<1000
bc=homelessness['region']=='Pacific'
fam_lt_1k_pac = homelessness[ab&bc]

# See the result
print(fam_lt_1k_pac)
#=========================================================================
# Subset for rows in South Atlantic or Mid-Atlantic regions
ab=homelessness['region']=='South Atlantic'
bc=homelessness['region']=='Mid-Atlantic'
south_mid_atlantic = homelessness[ab|bc]

# See the result
print(south_mid_atlantic)
#==========================================================================
#This can get tedious when you want all states in one of three different regions, 
#for example. Instead, use the .isin() method, which will allow you to tackle this
#problem by writing one condition instead of three separate ones.
# The Mojave Desert states
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)
