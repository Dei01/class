#ЛАБОРАТОРИЙН АЖИЛ No5. 

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
print('# Бодлого 5-1: Өгсөн 2 бүхэл тооны багыг нь хэвлэ.')

a = int(input('num1: '))
b = int(input('num2: '))

if a > b:
       print(a)
else:
       print(b)

# Бодлого 5-2: Өгсөн 3 бодит тооны ихийг нь хэвлэ.
a = int(input('num1: '))
b = int(input('num2: '))
c = int(input('num2: '))

if a > b:
       print(a)
elif c > b:
       print(c)
else:
       print(b)


# Бодлого 5-3: Өгсөн 4 тооны 3-д хуваагддаг тоонуудын тоог хэвлэ.
list = []
list = num1 
num1 = int(input("Enter your number:"))
if(num1%3==0):
    print("{} is divisible by 3".format(num1))
else:
    print("{} is not divisible by 3".format(num1))

# Бодлого 5-4: Өгсөн 3 тооноос тэгш тоонуудын нийлбэрийг хэвлэ.


# Python program to print Even Numbers in a List
 
# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

# Бодлого 5-5: Өгсөн 3 оронтой тоог палиндром эсэхийг шалга. Хоёр талаасаа ижил байх тоог палиндром тоо гэнэ. Жишээ нь: 121,343
# Python3 implementation of the above approach
 
# function to check palindrome

def checkPalindrome(str):
   
    # Run loop from 0 to len/2
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
           
    # If the above loop doesn't
    #return then it is palindrome
    return True
 
 
# Driver code
st = "112233445566778899000000998877665544332211"
if(checkPalindrome(st) == True):
    print("it is a palindrome")
else:
    print("It is not a palindrome")

# Бодлого 5-6: Өгөгдсөн 4 тооны 11-д хуваагддаггүй тоонуудынх нь нийлбэрийг ол.
# Python code
# To check whether the given number is divisible by 11 or not
 
#input
n=1234567589333892
# the above input can also be given as n=input() -> taking input from user
# finding given number is divisible by 11 or not
if int(n)%11==0:
  print("Yes")
else:
  print("No")
 



# Бодлого 5-7: Өгсөн тоон үнэлгээг үсгэн үнэлгээнд шилжүүл. Тоон үнэлгээ 89-өөс их бол А, 79-өөс их В, 69-өөс их бол С, 59-өөс их бол D бусад тохиолдолд F үсгэн дүнг хэвлэнэ.

a = int(input(''))

if a > 89:
       print('A')
elif a > 79:
       print('B')
elif a > 69:
       print('C')
else a > 59:
       print('D')



# # # БИЕ ДААЖ БОДОХ БОДЛОГУУД:


# # # Бодлого 5-2: Өгсөн 3 бодит тооны ихийг нь хэвлэ.
# # # Бодлого 5-3: Өгсөн 4 тооны 3-д хуваагддаг тоонуудын тоог хэвлэ.
# # # Бодлого 5-4: Өгсөн 3 тооноос тэгш тоонуудын нийлбэрийг хэвлэ.
# # # Бодлого 5-5: Өгсөн 3 оронтой тоог палиндром эсэхийг шалга. 
# # # Хоёр талаасаа ижил байх тоог палиндром тоо гэнэ. 
# # # Жишээ нь: 121, 343
# # # Бодлого 5-6: Өгөгдсөн 4 тооны 11-д хуваагддаггүй тоонуудынх нь нийлбэрийг ол.
# # # Бодлого 5-7: Өгсөн тоон үнэлгээг үсгэн үнэлгээнд шилжүүл. 
# # # Тоон үнэлгээ 89-өөс их бол А, 79-өөс их В, 69-өөс их бол С, 
# # # 59-өөс их бол D бусад тохиолдолд F үсгэн дүнг хэвлэнэ.
# # #---------------------------------------------------------------------------------
# # # Бодлого 5-1: Өгсөн 2 бүхэл тооны багыг нь хэвлэ.

# # # a = int(input('бүхэл тоо 1 a = '))
# # # b = int(input('бүхэл тоо 2 b = '))

# # # if a > b:
# # #    print(f'{a} = a тоо их')
# # # elif b > a:
# # #    print(f"{b} = b тоо их")
# # # else:
# # #    print(f"nothing")

# # # # Бодлого 5-2: Өгсөн 3 бодит тооны ихийг нь хэвлэ.

# # def gurawtthuwaawgddagtoo():
# #    x = int(input('Enter number: '))

# #    if x % 3 == 0: 
# #       print('yes')


# # gurawtthuwaawgddagtoo()



# # def tegshtoonuudiinniilber():
   
# #    a, b, c = int(input('tegshtoonuudiinniilber: '))
# #    a, b, c % 2 != 0:
# #       print()


# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))

# def isDivisibleBy3(x,y,z):

#     if (x,y,z % 3) == 0:

#         print(x + y + z)
#     else:
#         print('Numbers are ')

# isDivisibleBy3(input('n:'))

# ###Бодлого 5-5: Өгсөн 3 оронтой тоог палиндром эсэхийг шалга. 


# # # x , y , z = int(input('бүхэл тоо утга оруул: '))
# # # x > y > z = 


 