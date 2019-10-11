import pandas as pd 
import numpy as np 
import datetime

data = pd.read_csv('CV_03.csv', 'rb', delimiter = ',')
# print(data)
print(data)
df = data.dropna().reset_index()
df = df.drop(['index'], axis = 1)

df['Start_date'] = df['Start']
print(df.head())

n = 0
for i in df['Start']:
	df['Start_date'][n] = datetime.datetime.strptime(i, '%Y %m')
	n+=1
print(df.head())


df['End_date'] = df['End']
n = 0
for i in df['End']:
	df['End_date'][n] = datetime.datetime.strptime(i, '%Y %m')
	n+=1

print(df.head())

for i in df['End_date']:
	if type(i) == datetime.datetime:
		print('all good')
	else:
		print('ERRORRRRRRRR', i)


data_01 = df[['Lecture_or_Project', 'Software', 'hours', 'Start_date', 'End_date']]
print(data_01.head())

# Checkpoint
data_02 = data_01
data_02['Months'] = 1+12*(pd.DatetimeIndex(data_02['End_date']).year - pd.DatetimeIndex(data_02['Start_date']).year) + pd.DatetimeIndex(data_02['End_date']).month - pd.DatetimeIndex(data_02['Start_date']).month
print(data_02)

print(data_02['Start_date'].min())
print(data_02['Start_date'].max())

date_list = pd.date_range(data_02['Start_date'].min(),data_02['End_date'].max(), 
              freq='MS').strftime("%Y-%m").tolist()
print(date_list)

# Recreate the dataframe
Abilities = pd.DataFrame()
print(type(Abilities))

Abilities['Skill'] = 0
for i in date_list:
	Abilities[i] = 0
print(Abilities)

# create rows with skills
set_of_skills = set(data_02['Software'])
i=0
for n in set_of_skills:
	Abilities.loc[i, 'Skill'] = n
	i +=1

# change NaN to 0 
Abilities = Abilities.fillna(0)
print(Abilities)

for i in range(len(data_02)):
	# monthly hours spent on the program
	monthly = data_02.loc[i, 'hours'] / data_02.loc[i, 'Months']
	print('Monthly hours spent on', data_02.loc[i, 'Software'], 'are:', monthly)
	# get index for Abilities dataframe skill location
	n = Abilities.index[Abilities['Skill'] == data_02.loc[i, 'Software']][0]
	for column in Abilities:
		if column in pd.date_range(data_02.loc[i,'Start_date'],data_02.loc[i,'End_date']).strftime("%Y-%m").tolist():
		 	Abilities.loc[n,column] += monthly

print(Abilities)
# export to csv
Abilities.to_csv('Skills_monthly.csv')

