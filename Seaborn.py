import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

monthly_data = pd.read_csv('Skills_monthly.csv', 'rb', delimiter = ',')
# print(monthly_data.columns)

trns = monthly_data.transpose()
trns = trns.drop(['Unnamed: 0'])
print(trns)

names = monthly_data['Skill']
print(names)

trns.columns = names
print('table')
trns = trns.iloc[1:]

trns = trns.reset_index()
trns['index'] = pd.to_datetime(trns['index'])
print(trns)

# seaborn settings
# sns.set()
sns.set_style("whitegrid", {'legend.frameon':False, 'grid.linestyle': '--',})


trns = trns.rename({'index':'Date'}, axis = 1)
trns = trns.set_index('Date')

trns.to_csv('Skills_transpose.csv')
# print(trns)

data = pd.read_csv('Skills_transpose.csv', index_col=0, parse_dates=True)
# print(data)

###########################################################
### Calculate acumulated values
data_c = data.copy()
for k in data.columns:
	for i in range(len(data[k])-1):
		data_c[k][i+1] = data_c[k][i]+data_c[k][i+1]

###########################################################
### Get last values
data_for_sort = data_c.copy()
end_list = []
for k in data_c.columns:
	end_hours = data_for_sort[k][-1]
	end_list.append(end_hours)
print(end_list)

###########################################################
# sort columns from the biggest value to the lowest 
# at the last recorded date time
column_list = []
ls = end_list
while sum(ls) > 0:
	for i in range(len(ls)):
		if ls[i] == max(ls) and sum(ls) > 0:
			column_list.append(data_for_sort.columns[i])
			ls[i] = 0
# print(index_list)
# print(column_list)

############################################################
# Change data order

data_sorted = data_c[column_list]


# data_px = data_c.reset_index()

############################ PLOT 


sns.lineplot(data=data_sorted, dashes=False, linewidth=1.3, palette = "Spectral")
legend = plt.legend(frameon = False)
sns.despine(bottom = True, left = True)
sns.set_context("paper")
plt.ylabel('Hours on Skill')
plt.xlabel(' ')
plt.show()

# palettes husl, Spectral, RdYlGn_r, "RdYlBu", 
