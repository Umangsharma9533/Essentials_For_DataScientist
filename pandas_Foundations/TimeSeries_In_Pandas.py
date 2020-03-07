import pandas as pd

#Below read_csv will read data from file and convert dates into iso8601 format and it in Date column
df1=pd.read_csv('file_name',index_col='Date',parse_dates=True)

#Creating and using a DatetimeIndex
#In this exercise, a list of temperature data and a list of date strings has been pre-loaded for you
#as temperature_list and date_list respectively.
#Your job is to use the .to_datetime() method to build a DatetimeIndex out of the list of date strings, 
#and to then use it along with the list of temperature data to build a pandas Series.

# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)  

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)

#========================================================================================

# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['2010-07-04']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['2010-12-15':'2010-12-31']

#Reindexing the Index====================================================================
#To reindex the data, we provide a new index and ask pandas to try and match the old data to the new index.
#If data is unavailable for one of the new index dates or times, you must tell pandas how to fill it in.
#Otherwise, pandas will fill with NaN by default.

# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4

#ffill: will fill the NaN vlaue with values at forward indexes
#bfill: will fill the NaN vlaue with values at backward indexes
ts4 = ts2.reindex(ts1.index,method="ffill")

# Combine ts1 + ts2: sum12
sum12 = ts1+ts2

# Combine ts1 + ts3: sum13
sum13 = ts1+ts3

# Combine ts1 + ts4: sum14
sum14 = ts1+ts4


#==============================================================================
# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('D').count()

#==============================================================================
#Separating and resampling

# Extract temperature data for August: august
august = df['Temperature'].loc['2010-08']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('24h').max()

# Extract temperature data for February: february
february = df['Temperature'].loc['2010-02']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('24h').min()
