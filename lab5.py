#ЛАБОРАТОРИЙН АЖИЛ No5

# Дасгал 5.1. Өгсөн тоог тэгш эсэхийг шалгаж тэгш бол ‘Yes’, сондгой бол ‘No’ гэж хэвлэ.


n = int(input('Бүхэл тоо оруул: ')) if n % 2 == 0:
       print('Yes')
else:
print('No')

# Дасгал 5.2. Өгсөн оныг өндөр эсэхийг шалгаж үр дүнг хэвлэ. Тухайн он 4 ба 400-д хуваагдаж байвал
# өндөр жил, 100-д хуваагдаж байвал өндөр жил биш болно.	

# Үүрлэсэн if ашиглан бичвэл:
 n = int(input('Оныг оруул: '))
 if n % 4 == 0:
       if n % 100 == 0:
             if n % 400 == 0:
else: else:
print('Өндөр жил мөн') else:
print('Өндөр жил биш') print('Өндөр жил мөн')
print('Өндөр жил биш')

# if-elif-else ашиглан бичвэл:
 n = int(input('Оныг оруул: '))
 if n % 4 != 0:
print('Өндөр жил биш') elif n % 100 != 0:
print('Өндөр жил мөн') elif n % 400 != 0:
print('Өндөр жил биш') else:
print('Өндөр жил мөн')

# Дасгал 5.3. Илэрхийллийн үр дүнг хэвлэ.

x, y, z = 5, 10, 8
 x, y, z = z, y, x
 print(x > z)
 print((y- 5) == x)

# Дасгал5.4. ax2 +bx+c=0квадраттэгшитгэлийгбод.d=b2 –4*a*c


 import math
 a = float(input('a = '))
 b = float(input('b = '))
  c = float(input('c = '))
 d = b ** 2 - 4 * a * c
 if d > 0:
x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a) print(x1,x2, sep=' ')
elif d == 0:
       print('Давхардсан шийдтэй')
       x = -b / (2 * a)
       print(x)
else:
       print('Комплекс шийдтэй')


# БИЕ ДААЖ БОДОХ БОДЛОГУУД:

# Бодлого 5-1: Өгсөн 2 бүхэл тооны багыг нь хэвлэ.

# Бодлого 5-2: Өгсөн 3 бодит тооны ихийг нь хэвлэ.

# Бодлого 5-3: Өгсөн 4 тооны 3-д хуваагддаг тоонуудын тоог хэвлэ.

# Бодлого 5-4: Өгсөн 3 тооноос тэгш тоонуудын нийлбэрийг хэвлэ.

# Бодлого 5-5: Өгсөн 3 оронтой тоог палиндром эсэхийг шалга. Хоёр талаасаа ижил байх тоог палиндром тоо гэнэ. Жишээ нь: 121,343
# Бодлого 5-6: Өгөгдсөн 4 тооны 11-д хуваагддаггүй тоонуудынх нь нийлбэрийг ол.


# Бодлого 5-7: Өгсөн тоон үнэлгээг үсгэн үнэлгээнд шилжүүл. Тоон үнэлгээ 89-өөс их бол А, 79-өөс их В, 69-өөс их бол С, 59-өөс их бол D бусад тохиолдолд F үсгэн дүнг хэвлэнэ.
