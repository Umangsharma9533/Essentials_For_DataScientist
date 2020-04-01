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

'''
After having witnessed the market share for each category of apps,
let's see how all these apps perform on an average.
App ratings (on a scale of 1 to 5) impact the discoverability, conversion
of apps as well as the company's overall brand image. Ratings are a key performance indicator of an app.
From our research, we found that the average volume of ratings across
all app categories is 4.17. The histogram plot is skewed to the right 
indicating that the majority of the apps are highly rated with only a few exceptions in the low-rated apps.
'''

# Average rating of apps
avg_app_rating = apps['Rating'].mean()
print('Average app rating = ', avg_app_rating)

# Distribution of apps according to their ratings
data = [go.Histogram(
        x = apps['Rating']
)]

# Vertical dashed line to indicate the average app rating
layout = {'shapes': [{
              'type' :'line',
              'x0': avg_app_rating,
              'y0': 0,
              'x1': avg_app_rating,
              'y1': 1000,
              'line': { 'dash': 'dashdot'}
          }]
          }

plotly.offline.iplot({'data': data, 'layout': layout})

'''
5. Size and price of an app

Let's now examine app size and app price. For size, if the mobile app is too large, it may be difficult and/or expensive for users to download. Lengthy download times could turn users off before they even experience your mobile app. Plus, each user's device has a finite amount of disk space. For price, some users expect their apps to be free or inexpensive. These problems compound if the developing world is part of your target market; especially due to internet speeds, earning power and exchange rates.

How can we effectively come up with strategies to size and price our app?

    Does the size of an app affect its rating?
    Do users really care about system-heavy apps or do they prefer light-weighted apps?
    Does the price of an app affect its rating?
    Do users always prefer free apps over paid apps?

'''
%matplotlib inline
import seaborn as sns
sns.set_style("darkgrid")
import warnings
warnings.filterwarnings("ignore")

# Subset for categories with at least 250 apps
large_categories = apps.groupby('Category').filter(lambda x: len(x) >= 250).reset_index()

# Plot size vs. rating
plt1 = sns.jointplot(x = large_categories['Size'], y = large_categories['Rating'], kind = 'hex')

# Subset out apps whose type is 'Paid'
paid_apps = apps[apps['Type'] == 'Paid']

# Plot price vs. rating
plt2 = sns.jointplot(x = paid_apps['Price'], y = paid_apps['Rating'])

'''
6. Relation between app category and app price

So now comes the hard part. How are companies and developers supposed to make ends meet?
What monetization strategies can companies use to maximize profit? The costs of apps are 
largely based on features, complexity, and platform.

There are many factors to consider when selecting the right pricing strategy for your mobile app.
It is important to consider the willingness of your customer to pay for your app.
A wrong price could break the deal before the download even happens. 
Potential customers could be turned off by what they perceive to be a shocking cost,
or they might delete an app they’ve downloaded after receiving too many ads or simply not getting their money's worth.

Different categories demand different price ranges. Some apps that are simple and used daily,
like the calculator app, should probably be kept free. 
However, it would make sense to charge for a highly-specialized medical app that diagnoses diabetic patients.
Below, we see that Medical and Family apps are the most expensive.
Some medical apps extend even up to $80! All game apps are reasonably priced below $20.
'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# Select a few popular app categories
popular_app_cats = apps[apps.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY',
                                            'MEDICAL', 'TOOLS', 'FINANCE',
                                            'LIFESTYLE','BUSINESS'])]

# Examine the price trend by plotting Price vs Category
ax = sns.stripplot(x = popular_app_cats['Price'], y = popular_app_cats['Category'], jitter=True, linewidth=1)
ax.set_title('App pricing trend across categories')

# Apps whose Price is greater than 200
apps_above_200 = popular_app_cats[['Category', 'App', 'Price']][popular_app_cats['Price'] > 200]
apps_above_200

'''
7. Filter out "junk" apps

It looks like a bunch of the really expensive apps are "junk" apps. That is, apps that don't really have a purpose.
Some app developer may create an app called I Am Rich Premium or most expensive app (H) just for a joke or to test
their app development skills. Some developers even do this with malicious intent and try to make money by hoping people
accidentally click purchase on their app in the store.
Let's filter out these junk apps and re-do our visualization. The distribution of apps under $20 becomes clearer.
'''
# Select apps priced below $100
apps_under_100 = popular_app_cats[popular_app_cats['Price']<100]

fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# Examine price vs category with the authentic apps
ax = sns.stripplot(x='Price', y='Category', data=apps_under_100,
                   jitter=True, linewidth=1)
ax.set_title('App pricing trend across categories after filtering for junk apps')
