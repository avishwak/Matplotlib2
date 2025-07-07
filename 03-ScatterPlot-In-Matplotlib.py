# Problem 3 : Matplotlib Scatterplot in Matplotlib (	https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/)	
# =====================================

import matplotlib.pyplot as plt
import numpy as np

# scatter plot with two datasets in single plot
x = [4,5,6,7,3,6,9,8,7]
y = [6,3,4,8,2,6,1,2,3]

plt.scatter(x , y , c = 'red' , marker = '^' , edgecolor = 'green' , s = 100)

y1 = [22,34,23,43,56]
x1 = [33,24,23,14,53]
plt.scatter(x1 , y1 , c = 'yellow' , marker = 's' ,edgecolor = 'red' , s = 20)
plt.show()