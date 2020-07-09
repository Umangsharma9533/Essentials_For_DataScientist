Data Manipulation using Pandas

Summarizing of data:

	1) df.head(): shows top 5 rows
	2) df.info() : shows the datatype and number of elements in df
	3) df.mean() : Calculate mean of each columns in dataframe
	4) df.max(), df['column'].max() : Max of each column / max of column specified
	5) df.min()
	6) df.drop_duplicates()
	7) column.quantile():
	8) df['column'].value_counts() : give frequency of each element in the column
	9) # Subset for type A stores, calc total weekly sales
       sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
	10) sales.groupby(['type','is_holiday'])["weekly_sales"].sum()
	
	
Transforming data:
	1) sort_values('column_name', ascending= True/False)
	2) sort_values(by=['region','family_members'],ascending=[True,False]) // multiple sorting
	3) agg() : to apply cutomize function on data set.
	   Example : unemp_fuel_stats = sales.groupby('type')['unemployment','fuel_price_usd_per_l'].agg(fuc_list)
	4) pivot_table(values='weekly_sales',index='type',aggfunc=[np.mean,np.median]) // for numpy
	   OR
	   # Print mean weekly_sales by department and type; fill missing values with 0
	   #when we have to use 2 columns at once
       print(sales.pivot_table(values='weekly_sales',index='type',columns='department',fill_value=0))
	
	
Slicing and Indexing:
	
	1) dfone=df.set_index('city') / to create a index name 
	2) df.reset_index() : Index resetted while content is preserved.
	3) df.isin(condition) : Selects the data if it statisfy the condition
	   Example:
	   # Make a list of cities to subset on
	   cities = list(["Moscow","Saint Petersburg"])

       # Subset temperatures using square brackets
       print(temperatures[temperatures["city"].isin(cities)])
	4) df.loc[value] : output the value from data frame
	5) df.sort_index(level=["country","city"],ascending=[True,False]))
	6) # Pivot avg_temp_c by country and city vs year
       temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c",index=['country','city'],columns='year')
	
	7) # Get the total number of avocados sold of each size
      nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()
	
	8) plt.legend() : 