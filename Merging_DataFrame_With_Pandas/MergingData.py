'''
Merging on a specific column
'''
# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue,managers,on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue,managers,on='branch_id')

# Print merge_by_id
print(merge_by_id)


'''
Merge the DataFrames revenue and managers into a single DataFrame called combined using the 'city' and 'branch' columns from the appropriate DataFrames.

    In your call to pd.merge(), you will have to specify the parameters left_on and right_on appropriately.
'''
# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue,managers,left_on='city',right_on='branch')

# Print combined
print(combined)

'''
Merging on multiple columns
'''
# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue,managers,on=['branch_id','city','state'])

# Print combined
print(combined)


'''
'''
# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue,sales,how="right",on=['city','state'])

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales,managers,how="left",left_on=['city','state'],right_on=['branch', 'state'])

# Print sales_and_managers
print(sales_and_managers)
