# Problem 1 : Matplotlib Line Chart in Matplotlib (https://www.geeksforgeeks.org/line-chart-in-matplotlib-python/	)
# =====================================
import matplotlib.pyplot as plt
import numpy as np

#Line chart was covered in previous class. Here we learn about fill_between
x = np.array([1,2,3,4])
y = x *2
plt.plot(x,y)

y1 = [3,5,6,9]
plt.plot(x,y1,'-.')
plt.fill_between(x, y ,y1 , color = 'g')
plt.show()

x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.sin(x) + 0.5
plt.plot(x,y1,label = 'lower_bound')
plt.plot(x,y2 , label = 'upper_bound')
plt.fill_between(x,y1,y2, color = 'gray' , alpha = 0.2)
plt.legend()
plt.show()
