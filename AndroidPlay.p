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
