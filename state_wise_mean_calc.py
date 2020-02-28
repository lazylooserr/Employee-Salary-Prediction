# Program name: state_wise_mean_calc.py
# State wise figures of salary, hra, conv, total on empsal.csv
# Plot a bar graph where state will be in X axis and
# total figures will be in Y axis

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

empsal_df = pd.read_csv('empsal.csv', index_col='empno', parse_dates=['dob'])
print(empsal_df.info())

empsal_df.dropna(axis=0, how='any', inplace=True)
print(empsal_df.info())

# Add columns conv. Salary
empsal_df['conv'] = empsal_df.salary * 0.10
empsal_df['total'] = empsal_df.salary + empsal_df.hra + empsal_df.conv
print(empsal_df.head())

# Find the mean of Salary, Hra, conv and total - state wise
mean_list = empsal_df.groupby(['state'])['salary', 'hra', 'conv', 'total'].mean()
print(mean_list)

# Plotting a bar chart of mean figures of salary, hra, conv, and total
mean_list.plot(kind='bar')
plt.title('State wise mean figures of \n salary, hra, conv, total')
plt.xlabel('States-->')
plt.ylabel('Mean Figures')
plt.tight_layout()
plt.legend(loc='best')
plt.show()

x = input('Press Enter to continue')
