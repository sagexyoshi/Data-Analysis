import pandas as pd

# Uploading dataframe 
df = pd.read_csv('GoogleApps.csv')

print(df.head())
print(df.describe())
print(df.tail())
print(df.info())

print(df[df['Type'] == 'Paid']['Price'].min())
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())
free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print(free - paid)

print(df[df['Content Rating'] == 'Teen']['Size'].min())

print(df[df['Reviews'] == df['Reviews'].max()]['Category'])

print(df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean())
# What is the name of the first application containing in the dataset?


# What is the category of the last application containing in the dataset?


# How many columns are there in the dataset?
# What is the type of data stored in each column?


# Specify the arithmetic mean and median for the size of the applications.
# How much does the most expensive application cost?
# *Specify the arithmetic mean and median for the number of application installs.
