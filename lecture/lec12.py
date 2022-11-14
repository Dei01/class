
# LIBRARIES 

# MASSIVE 
import numpy as np
import pandas as pd
# a = np.array([1,2,3])
# a
# type(a)

# print('hi')


# a.ndim 

# a.size 
# np.arange(0,10)

# np.arange(0,12,3)
# np.arange(0,3,0.5)

# np.linspace(0,10,5) # функцийн эхний 2 аргумент массивын эхнйи ба ёүүлийн элементүүд байх ба 3 дахь нь эдгээр утгыг хэдэн завсар хуваагыг заана.


# a = np.arange(10, 19).reshape((3, 3))
# a


# arr = np.array([1,2, 3, 4, 5])
# print(arr.dtype)
# print('------------------------------------------------------------')

# a = np.arange(10, 15)
# for i in a:
# print (i)
# print('------------------------------------------------------------')

# b =np.arange(10, 19).reshape((3, 3))
# for row in b:
# print(row)

# print('------------------------------------------------------------')

# import numpy as np 
# x = np.array([3, 5])
# y = np.array([2, 5])
# print(np.greater(x, y))


obj = pd.Series([4,7,-5,3,])

print(obj)
print(obj.values)
print(obj.index)
print('------------------------------------------------------------')


obj2 = pd.Series([4, 7, -5], index = ['a', 'b', 'c'])
print(obj2)
print(obj2/2)
print(obj2+5)

mydict = {'red':2000, 'blue':1000, 'yellow':500, 'orange':1000}
colors = ['red', 'yellow', 'orange', 'blue', 'green']
myseries = pd.Series(mydict, index = colors)
myseries

print('--------------------------ДАТАФРЭЙМИЙГ ҮҮСГЭХ----------------------------------')


# ДАТАФРЭЙМИЙГ ҮҮСГЭХ

data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'], 'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'], 'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
print(frame)
print('--------------------------frame1----------------------------------')

frame1 = pd.DataFrame(data, columns = ['object', 'price'])
print(frame1)
print('-------------------------frame2-----------------------------------')

frame2 = pd.DataFrame(data,
index = ['one', 'two', 'three', 'four', 'five'])
print(frame2)

print('------------------------frame3------------------------------------')

 #COMBINING NUMPY & PANDAS 
 
frame3 = pd.DataFrame(np.arange(16).reshape((4, 4)), index = ['red', 'blue', 'yellow', 'white'],
columns = ['ball', 'pen', 'pencil', 'paper']) 
print(frame3)

print('-------------------------frame4-----------------------------------')