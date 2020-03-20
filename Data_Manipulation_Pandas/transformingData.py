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
#==============================================================================
# Add total col as sum of individuals and family_members
homelessness['total']=homelessness['individuals']+homelessness['family_members']

# Add p_individuals col as proportion of individuals
homelessness['p_individuals']=homelessness['individuals']/homelessness['total']

# See the result
print(homelessness)

#===============================================================================

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop'] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k']>20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k',ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state','indiv_per_10k']]

# See the result
print(result)

#====================================================================================
#Aggregating the values
# Import NumPy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
fuc_list=[np.min,np.max,np.mean,np.median]

sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min,np.max,np.mean,np.median])
# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')['unemployment','fuel_price_usd_per_l'].agg(fuc_list)

# Print unemp_fuel_stats
print(unemp_fuel_stats)




#==========================================================================================
#Aggregatig using pivot table
