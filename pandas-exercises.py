import os
import pandas as pd

def print_nice(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

df = pd.read_csv('../downloads/insurance.csv')

print(df)

print_nice("printing series", df.to_string())

print_nice("show all column names of insurance file", df.columns)

print_nice("show all index names of insurance file", df.index)
#can see that the index names are actually numbered from 0 to 1339 (from my understanding)

print_nice("infers the data types in insurance file", df.dtypes)

print_nice("Here is the shape of the series", df.shape)

print_nice("here is summarized information about the insurance file", df.info())

print_nice("here is a description of the insurance file including percentiles, mean, std, min, max", df.describe())

#Exercise number 3:
print_nice("selecting column Age", df['age'])

#Exercise number 4:
print_nice("selecting column Age, Children, Charges", df[['age', 'children', 'charges']])

#Exercise number 5:
print_nice("only the 5 first lines of the columns: Age, Children and Charges", df.head(n=5)[['age', 'children', 'charges']])

# Exercise number 6:
print_nice("Average of charges", df['charges'].mean())
print_nice("Minimum of charges", df['charges'].min())
print_nice("Maximum of charges", df['charges'].max())

#Exercise number 7:
print_nice("age of the person who paid 10797.3362", df[df['charges'] == 10797.3362])
#age is of 52 years, female, not a smoker

#Exercise number 8:
print_nice("age of person with maximum charge", df[df['charges'] == 63770.42801])
# age is of 54 years

#Exercise number 9:
print_nice("the number of people per region", df['region'].value_counts())

#Exercise number 10:
print_nice("the number of of insured children", df['children'].count())

#Exercisee number 11:
#Charges and age would be positively correlated, and bmi and children would not have any correlation

#Exercise number 12:
print_nice("dataframe correlactions", df.corr())