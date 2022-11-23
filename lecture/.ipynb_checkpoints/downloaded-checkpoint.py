# ЛАБОРАТОРИЙН АЖИЛ 12 
# 	•	Numpy ажиллах
# 	•	Pandas ажиллах

# Жишээ бодлогууд 1: Numpy хоёр хэмжээст массив үүсгэх

# Хоёр хэмжээст массивын элементэд хандах
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 1])

# Нэг хэмжээст массивын хэсэгчилж хэвлэх
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Нэг хэмжээст массивын сондгой элементүүдийг хэвлэх
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

# Нэг хэмжээст массивыг хуулбарлах
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

# Хоёр хэмжээст массивыг элементүүдийг тоолох
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# Нэг хэмжээст массивыг хоёр хэмжээст массив болгож хөрвүүлэх
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Хоёр хэмжээст хоёр массивыг нийлүүлэх
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# Нэг хэмжээст массивыг хувааж нэг хэмжээст массивууд үүсгэх 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = n import numpy as np

# Нэг хэмжээст массивын тэгш индекстэй элементүүдийг хэвлэх
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x) 
p.array_split(arr, 4)
print(newarr)

# Нэг хэмжээст массивын элементүүдийг эрэмбэлэх
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

# Numpy ufunc
# Функц
# Тайлбар
# *add()
# Нэмэх
# *subtract()
# Хасах
# *multiply()
# Үржүүлэх
# *divide()
# Хуваах
# *power()
# Зэрэг
# *mod() 
# Бүхэл үлдэгдэл
# *remainder()
# Үлдэгдэл
# *divmod()
# Хуваагч, үлдэгдэл хоёр утга буцаана
# *absolute()
# Абсолют утга
# *sum()
# Нийлбэр олох
# *cumsum()
# Cummulative нийлбэр олох
# *prod()
# Үржвэр олох
# *cumprod()
# Cummulative үржвэр олох
# *gcd.reduce()
# Массивын хамгийн их хуваагчийг олох
# *gcd()
# Хамгийн их хуваагчийг олох
# *lcm.reduce()
# Массивын хамгийн бага тооны үржвэрийг олох
# *lcm()
# Хамгийн бага тооны үржвэрийг олох

# Нэг хэмжээст хоёр массивын элементүүдийн нийлбэрийг олох
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)

# Жишээ бодлогууд 2: Pandas
# Anaconda, Spyder гэх зэрэг платформууд нь NumPy суулгах
# C:\Users\Your Name>pip install pandas

# Түлхүүр талбар, утга бүхий талбаруудаар цувааг /serial/ үүсгэх
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# csv файл татаж авах холбоос: https://www.w3schools.com/python/pandas/dirtydata.csv.txt 

# Хоосон нүд бүхий мөрүүдийг устгах
import pandas as pd
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string()

# # Буруу мөр форматтай мөрийг арилгах
# # import pandas as \pd
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'], inplace = True)
# print(df.to_string())

# # Буруу өгөгдлүүдийг ялгаж хэвлэх 
# # import pandas as pd
# df = pd.read_csv('data.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)
# print(df.to_string())

# Даалгаварын бодлогууд
# 	•	Нэг хэмжээст хоёр массивыг нийлүүлж, элементүүдийн тоог хэвлэ.
# 	•	Нэг хэмжээст массивыг хуулж, хуулсан массивын элементүүдийг эрэмбэл.
# 	•	Хоёр хэмжээст массивын элементүүдийн нийлбэрийг ол.
# 	•	Хоёр хэмжээст массивын элементүүдийг эрэмбэлж, сондгой индекстэй элементүүдийн үржвэрийг ол.
# 	•	Хоёр хэмжээст массивын тэгш индекстэй элементүүдийг хуулбарлаж, хамгийн их хуваагчийг ол.
# 	•	5 хичээлийн код, нэр бүхий цувааг үүсгэж, 3 дахь хичээлийн нэрийг солж, цувааг хэвлэ.
# 	•	csv файл татаж авах холбоос: https://www.w3schools.com/python/pandas/dirtydata.csv.txt алдаатай хоосон нүдтэй мөрийг алгасаж хэвлэ.
# 	•	Дараах csv файл татан авч https://www.w3schools.com/python/pandas/dirtydata.csv.txt   “Pulse” баганийн 100-с 110 хооронд орших өгөгдлүүдийг хэвлэ.
