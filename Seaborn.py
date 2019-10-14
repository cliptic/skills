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
# trns = sns.load_dataset("trns")
trns['index'] = pd.to_datetime(trns['index'])
print(trns)

sns.set_style("white")

trns = trns.rename({'index':'Date'}, axis = 1)
i = 0
for k in trns.columns:
	if i > 0:
		plt.scatterplot(trns['Date'], trns[k], data=trns)
	i+=1
plt.show()

trns.to_csv('Skills_transpose.csv')

print(trns)