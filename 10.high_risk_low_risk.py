import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from operator import add
import seaborn as sns

# Load the data
data = pd.read_csv('framingham.csv')
data.drop(['education'], axis=1, inplace=True)
data.head()

# total percentage of missing data
missing_data = data.isnull().sum()
total_percentage = (missing_data.sum()/data.shape[0]) * 100
print(f'The total percentage of missing data is {round(total_percentage,2)}%')


# percentage of missing data per category
total = data.isnull().sum().sort_values(ascending=False)
percent_total = (data.isnull().sum()/data.isnull().count()
                 ).sort_values(ascending=False)*100
missing = pd.concat([total, percent_total], axis=1,
                    keys=["Total", "Percentage"])
missing_data = missing[missing['Total'] > 0]
missing_data


plt.figure(figsize=(9, 6))
sns.set(style="whitegrid")
sns.barplot(x=missing_data.index,
            y=missing_data['Percentage'], data=missing_data)
plt.title('Percentage of missing data by feature')
plt.xlabel('Features', fontsize=14)
plt.ylabel('Percentage', fontsize=14)
plt.show()

data.dropna(axis=0, inplace=True)
data.shape

# plot histogram to see the distribution of the data
fig = plt.figure(figsize=(15, 20))
ax = fig.gca()
data.hist(ax=ax)
plt.show()

# Case counts
sns.countplot(x='TenYearCHD', data=data)
plt.show()
cases = data.TenYearCHD.value_counts()
print(
    f"There are {cases[0]} patients without heart disease and {cases[1]} patients with the disease")

# Number of people who have disease vs age
plt.figure(figsize=(15, 6))
sns.countplot(x='age', data=data, hue='TenYearCHD', palette='husl')
plt.show()
