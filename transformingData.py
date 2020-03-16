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
