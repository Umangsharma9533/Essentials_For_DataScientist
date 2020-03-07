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


#======================================================================================
# Extract the August 2010 data: august
august = df['Temperature']['2010-08']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)


#======================================================================================
#Manipulating Time Series Data
# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('24h').min()

#===================================================================================
#Rolling mean and frequency
# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()



#============================================================================
#Method Chaining and filtering
# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()


#===================================================================================
#Missing Values and interpolation
# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how="linear")

# Compute the absolute difference of ts1 and ts2_interp: differences 
differences = np.abs(ts2_interp-ts1)

# Generate and print summary statistics of the differences
print(differences.describe())

#===================================================================================
# Time Zones and Conversion
# Build a Boolean mask to filter for the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none 
times_tz_none = pd.to_datetime( la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'] )

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')
