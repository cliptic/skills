import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

monthly_data = pd.read_csv('Skills_monthly.csv', 'rb', delimiter = ',')

# sns.set()
# sns.relplot(x="timepoint", y="", col="region",
#             hue="event", style="event",
#             kind="line", data=fmri);

print(monthly_data.columns)

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

###########################
###PLOT NO 1

# for k in data.columns:
# 	data[k].plot(linewidth=0.5)
# sns.despine()
# plt.show()

###########################
### Create data_c where index is date and data_px where date is a column
data_c = data.copy()
for k in data.columns:
	for i in range(len(data[k])-1):
		data_c[k][i+1] = data_c[k][i]+data_c[k][i+1]

data_for_sort = data_c.copy()
end_list = []
for k in data_c.columns:
	end_hours = data_for_sort[k][-1]
	end_list.append(end_hours)
print(end_list)

# sort indexes from the biggest last value to the lowest
index_list = []
ls = end_list
while sum(ls) > 0:
	for i in range(len(ls)):
		if ls[i] == max(ls) and sum(ls) > 0:
			index_list.append(i)
			ls[i] = 0
print(index_list)



# data_px = data_c.reset_index()

###########################
###PLOT NO 2

# for k in data_c.columns:
# 	data_c[k].plot(linewidth=0.75, legend = True, )
# sns.despine()
# sns.set_context("paper")
# plt.show()

###########################
###PLOT NO 3

# data_c = data.copy()
# for k in data_c.columns:
# 	plt.stackplot(data_px["Date"], data_px[k], alpha=0.25) 
# plt.show()

##########################

###########################
###PLOT NO 4

# data_c.plot.area()
# plt.show()

###########################
###PLOT NO 5

sns.lineplot(data=data_c, dashes=False, linewidth=1.3, palette = "husl", sort = True)
legend = plt.legend(frameon = False)
sns.despine(bottom = True, left = True)
sns.set_context("paper")
plt.ylabel('Hours on Skill')
plt.xlabel(' ')
plt.show()