# Problem 4 : Matplotlib Pie Chart in Matplotlib (	https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/		)	
# =====================================

import matplotlib.pyplot as plt
import numpy as np

cars = ['AUDI' , 'BMW' , 'MERCEDES' , 'TESLA' , 'JAGUAR']
data = [25,45,5,38,20]

fig = plt.figure(figsize = (10,7))
plt.pie(data , labels = cars)
plt.show()

# very important feature to get the wedge out for small fractions or to emphasize on a value
explode = (0 , 0 , 0.4 , 0 , 0)
plt.pie(data , labels = cars , explode = explode , autopct = '%8.1f%%' , startangle = 90)
a = 78
print("%2.1f%%" , 3.5)
print("%9.1f%%" % 13.5) # this is a new way of printing % for me! very interesting.
print("hello" , a)
plt.show()

# adding more text and parameters like edge color and so on to pie chart 
colors = ('orange' , 'cyan' ,'brown' ,'grey' ,'indigo')
wp = {'linewidth' : 5 , 'edgecolor' : 'green'}
fig , ax = plt.subplots(figsize = (10,7))
wedges , text , autotexts = plt.pie(data , labels = cars , explode = explode , shadow = True , startangle = 90 ,
                                    wedgeprops= wp , autopct = '%0.2f%%' , textprops = {'color' : 'magenta'})

plt.setp(autotexts , size = 8 , weight = 'bold' , color = 'blue')
ax.set_title("My pie chart")
fig.text(0.9 , 0.15 , "Sample car data" , fontsize = 12 ,  color = 'red' , ha = 'right' , va = 'bottom' , alpha = 0.2)
fig.text(0.1 , 0.15 , "Sample car data 1" , fontsize = 12 ,  color = 'red' , ha = 'left' , va = 'bottom' , alpha = 0.8)
plt.show()

# I feel the nested pie chart didn't work as expected but this is what was demonstrated in the class
size = 6
cars = ['AUDI' , 'BMW' , 'MERCEDES' , 'TESLA' , 'JAGUAR' , 'FORD']
data = np.array([[23,16] ,[17,23] , [22,11] ,[12,15] ,[34,26] ,[29,34]])

#normalize data to 2pi
norm = data/np.sum(data) * 2 * np.pi
# print(np.sum(data))
# print(23/262 * 2 * np.pi)
# print(norm)

left = np.cumsum(np.append(0 , norm.flatten()[:-1])).reshape(data.shape)
# print(norm.flatten()[:-1])
# left
# [0 0.55157734 0.38370597 0.4076876  0.55157734 0.52759571 0.26379786
#  0.28777948 0.35972435 0.81537519 0.62352221 0.69546708]

cmap = plt.get_cmap("tab20c") # 20 colors
outer_colors = cmap(np.arange(6) * 4)
# print(np.arange(6) * 4)
# outer_colors
inner_colors = cmap(np.array([1,2,5,6,9,10,11,13,14,15,18,19]))
fig , ax = plt.subplots(figsize = (8,7) , subplot_kw = dict(polar = True))
#yscale = 'log'
#aspect =: 'equal'

#starting angle for each inner bar ,
ax.bar(x = left.flatten() , height = size , bottom = -17, color = inner_colors , edgecolor = 'w' , linewidth = 1 , align = 'edge')

#outer pie
ax.bar(x = left[: , 0]   ,width = norm.sum(axis = 1),  height = size , color = outer_colors , edgecolor = 'w' , linewidth = 1 , align = 'edge' )
#width - angle width
ax.set(title = "Nested pie chart")
ax.set_axis_off()
plt.show()