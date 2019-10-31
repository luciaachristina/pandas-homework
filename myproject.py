import os

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.tab.txt', sep='\t')

print(df)

#printing information:
print(df.info())

#printing summary of stats:
print(df.describe())

#printing correlations
print(df.corr())

#REACH

print("diabetes dataframe", df.to_string())
print("diabetes columns", df.columns)

os.makedirs('plots', exist_ok=True)

#histogram of Age/BMI
plt.hist(df['AGE'], bins='auto', color='b')
plt.title('Age BMI')
plt.xlabel('AGE')
plt.ylabel('BMI number')
plt.savefig(f'plots/sex_hist.png', format='png')

#scatterplot of age vs bmi
plt.scatter(df['AGE'], df['BMI'], color='red')
plt.title('AGE vs BMI')
plt.xlabel('AGE')
plt.ylabel('BMI')
plt.savefig(f'plots/age_vs_bmi.png', format='png')
