#1. Google Play Store apps and reviews
#Mobile apps are everywhere. They are easy to create and can be lucrative.
# Because of these two factors, more and more apps are being developed. 
#In this notebook, we will do a comprehensive analysis of the Android app market 
#by comparing over ten thousand apps in Google Play across different categories. 
#We'll look for insights in the data to devise strategies to drive growth and retention.

# Read in dataset
import pandas as pd
apps_with_duplicates = pd.read_csv('datasets/apps.csv')

# Drop duplicates
apps = apps_with_duplicates.drop_duplicates()

# Print the total number of apps
print('Total number of apps in the dataset = ', apps.count())

# Have a look at a random sample of 5 rows
n = 5
apps.sample(n)

# List of characters to remove
chars_to_remove = ['+',',','M','$']
# List of column names to clean
cols_to_clean = ['Installs','Size','Price']

# Loop for each column
for col in cols_to_clean:
    # Replace each character with an empty string
    for char in chars_to_remove:
        apps[col] = apps[col].str.replace(char, '')
    # Convert col to numeric
    apps[col] = pd.to_numeric(apps[col])
'''
3. Exploring app categories

With more than 1 billion active users in 190 countries around the world, Google Play continues to be an important
distribution platform to build a global audience. 
For businesses to get their apps in front of users, it's important to make them more quickly and easily discoverable on Google Play.
To improve the overall search experience, Google has introduced the concept of grouping apps into categories.
This brings us to the following questions:
Which category has the highest share of (active) apps in the market?
Is any specific category dominating the market Which categories have the fewest number of apps?
We will see that there are 33 unique app categories present in our dataset. Family and Game apps 
have the highest market prevalence. Interestingly, Tools, Business and Medical apps are also at the top.
'''
import plotly
plotly.offline.init_notebook_mode(connected=True)
import plotly.graph_objs as go

# Print the total number of unique categories
num_categories = len(apps['Category'].unique())
print('Number of categories = ', num_categories)

# Count the number of apps in each 'Category' and sort them in descending order
num_apps_in_category = apps['Category'].value_counts().sort_values(ascending = False)

data = [go.Bar(
        x = num_apps_in_category.index, # index = category name
        y = num_apps_in_category.values, # value = count
)]

plotly.offline.iplot(data)
