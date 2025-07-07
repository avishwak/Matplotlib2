# Problem 2 : Matplotlib Histogram in Matplotlib (https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/	)
# =====================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import pandas as pd

# 1. Histogram with different bins
a = [22,97,5,56,38,79,90,34,20,22,25]
fig,ax = plt.subplots(figsize = (8,4))
# ax.hist(a , bins =[0,20,50,75,100])
N , bins , patches = ax.hist(a ,bins = 4)
plt.show()

# 2. This is a more advanced histogram example with color normalization MUST REVISE 
np.random.seed(6643433)
n_bins = 20
x = np.random.randn(10000)
y = .8 ** 5 + np.random.randn(10000) + 25
legend = ['distribution']
fig,ax = plt.subplots(1,1 ,figsize = (8,5) , tight_layout = True)

#spines
for s in ['right' , 'top']:
    ax.spines[s].set_visible(False)

#remove ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

#padding
ax.xaxis.set_tick_params(pad = 20)
ax.yaxis.set_tick_params(pad = 20)

#grid lines
ax.grid(color = 'grey' , linestyle = "-." , linewidth = 0.5 , alpha = 0.5)

N , bins , patches = ax.hist(x , bins = 20)
# print(N)
fracs = ((N ** (2)))
# print(fracs)
norm = colors.Normalize(fracs.min() , fracs.max()) # to get colormap scaling
# print(norm)
# print(patches)

for thisfrac , thispatch in zip(fracs , patches):
#     print(thisfrac)
#     print(thispatch)
    color = plt.cm.viridis(norm(thisfrac))
#     print(color)
    thispatch.set_facecolor(color)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(legend)
plt.title("Customized histogram")

plt.show()


# 3. Showing how to plot hitogram from a dataset
# number of credit card users for every geography as per their gender
dataset = pd.read_csv("Churn_Modelling.csv")
# dataset.head()
df = dataset[dataset['HasCrCard'] == 1]
df1 = df.groupby(['Geography' ,'Gender'])['HasCrCard'].size().reset_index(name = 'count')
df = df1[df1['Gender'] == 'Female']
plt.figure()
plt.bar(df['Geography'] , df['count'])
plt.show()

df = df1[df1['Gender'] == 'Male']
plt.bar(df['Geography'] , df['count'])
plt.show()
