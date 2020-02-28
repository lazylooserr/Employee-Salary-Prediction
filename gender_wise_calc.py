import pandas as pd
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

empsal_df=pd.read_csv('empsal.csv',index_col='empno',parse_dates=['dob'])
print(empsal_df.info())
empsal_df.dropna(axis=0,how='any',inplace=True)
print(empsal_df.head())

#adding col conventional salary

empsal_df['conv']=empsal_df.salary*0.10
empsal_df['total']=empsal_df.salary+empsal_df.hra+empsal_df.conv
print(empsal_df.head())


#dataframe to csv

empsal_df.to_csv('empsalnew.csv')


#mean of total,salary,hra,conv gender wise

print('Sum details:- ')
print(empsal_df.groupby(['sex'])['salary','hra','conv','total'].sum())

print('Mean details:- ')
print(empsal_df.groupby(['sex'])['salary','hra','conv','total'].mean())

print('Standard deviation:-  ')
print(empsal_df.groupby(['sex'])['salary','hra','conv','total'].std())
x=input('press Enter to continue')
