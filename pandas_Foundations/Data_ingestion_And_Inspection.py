#Importing Relevant Libraries
import pandas as pd
# Import numpy
import numpy as np

#import data from csv file into dataframe
df=pd.read_csv('World_Bank.csv')
#Check first 5 rows of the table
df.head(5)
#Check last 5 rows of the table
df.tail(5)

#Check about the information of dataframe
df.info()

# Create array of DataFrame values: np_vals
np_vals = df.values

# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)

# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(df)

# Print original and new data containers
[print(x, 'has type', type(eval(x))) for x in ['np_vals', 'np_vals_log10', 'df', 'df_log10']]

#=============================================================================================
#Zip lists into a dataframe
# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys,list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

#=============================================================================================
#Labelling your data
# Build a list of labels: list_labels
list_labels = list(['year','artist','song','chart weeks'])

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels

#=============================================================================================
#Broadcasting a Data
# Make a string with the value 'PA': state
state = 'PA'

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
