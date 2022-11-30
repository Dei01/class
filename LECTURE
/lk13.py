import pandas as pd
data = {'color':['blue', 'green', 'yellow', 'red', 'white'],
	'object': ['ball', 'pen', 'pencil', 'paper', 'mug'],
	'price': [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
frame
'''    color  object  price
0    blue    ball    1.2
1   green     pen    1.0
2  yellow  pencil    0.6
3     red   paper    0.9
4   white     mug    1.7'''
frame1 = pd.DataFrame(data,columns = ['object','price'])
frame1
'''   object  price
0    ball    1.2
1     pen    1.0
2  pencil    0.6
3   paper    0.9
4     mug    1.7'''
frame1 = pd.DataFrame(data,index = ['one','two', 'three', 'four', 'five'])
frame1
'''        color  object  price
one      blue    ball    1.2
two     green     pen    1.0
three  yellow  pencil    0.6
four      red   paper    0.9
five    white     mug    1.7'''

import numpy as np
frame2 = pd.DataFrame(np.arange(16).reshape((4,4)),index = ['red','blue', 'yellow', 'white'], columns = ['ball', 'pen', 'pencel','paper'])
frame2
'''        ball  pen  pencel  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15'''



frame.columns
'''Index(['color', 'object', 'price'], dtype='object')'''

frame.columns
'''Index(['color', 'object', 'price'], dtype='object')'''
frame.values
'''array([['blue', 'ball', 1.2],
       ['green', 'pen', 1.0],
       ['yellow', 'pencil', 0.6],
       ['red', 'paper', 0.9],
       ['white', 'mug', 1.7]], dtype=object)'''
frame.index
'''RangeIndex(start=0, stop=5, step=1)'''

 frame.price
'''0    1.2
1    1.0
2    0.6
3    0.9
4    1.7
Name: price, dtype: float64'''

frame.index.name = "id"; frame.columns.name = 'item'
frame
'''item   color  object  price
id                         
0       blue    ball    1.2
1      green     pen    1.0
2     yellow  pencil    0.6
3        red   paper    0.9
4      white     mug    1.7'''

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/'
df = pd.read_csv(url, header = None)
df.head()

headers = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base',
'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower',
 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
