import pandas as pd
sales=pd.read_csv('')
# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())

#===========================================================
# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())

#==============================================================
#Custom use of function in aggregate
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales["temperature_c"].agg(iqr))
#================================================================
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Print date col of holiday_dates
print(holiday_dates['date'])
#====================================================================
#Counting Categorical Variables

# Count the number of stores of each type
store_counts = stores['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props =  stores['type'].value_counts(normalize=True)
print(store_props)

# Count the number of departments of each type and sort
dept_counts_sorted = departments['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each type and sort
dept_props_sorted = departments['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)
#=============================================================================
#Group By stuff.
#Marvelous mathematics! About 91% of sales occured in stores of type A',
# 9% in stores of type B, and there are no sales records for stores of type C. 
#Now see if you can do this calculation using .groupby().

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)
#=====================================================================
# From previous step
sales_by_type = sales.groupby(['type','is_holiday'])["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales_by_type
print(sales_by_type_is_holiday)
