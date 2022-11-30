# ДАСГАЛ АЖИЛУУД:
# Дасгал 1. Үгэн алгоритмыг блок схемээр илэрхийл.
# 1. Алгоритм эхэлнэ.
# 2. x хувьсагчийн утгыг гараас оруулна. 3.x-г 100-д хуваагаад M хувьсагчид утгыг
# олгоно.
# 4. Дэлгэцэнд М утгыг хэвлэнэ. 5. Алгоритм төгсөнө.

# Дасгал 2. Өөрийн овог, нэр, суралцаж буй мэргэжлийг асуугаад дараа нь хариулдаг алгоритм зохио.
name = input('Enter your name: ')
age = input('Enter your age: ')
study = input('Enter your study: ')
print(f'your name: {name}, age:{age}  ' )

# Дасгал 3. Гурвалжны 3 тал өгөгдсөн бол талбайг нь ол.

inputString = input('Зай аваад 3-н тоо оруулах: ')
list = inputString.split()
sum = 0 
for num in list:
    sum+= int(num)
print(f'периметр = {sum}\n')
print(f'талбай = {sum/2}\n')

# Дасгал 4. Квадрат тэгшитгэлийг бодох алгоритм зохио.

# importing library sympy
from sympy import symbols, Eq, solve
  
# defining symbols used in equations
# or unknown variables
x, y, z = symbols('x,y,z')
  
# defining equations
eq1 = Eq((x+y+z), 1)
print("Equation 1:")
print(eq1)
  
eq2 = Eq((x-y+2*z), 1)
print("Equation 2")
print(eq2)
  
eq3 = Eq((2*x-y+2*z), 1)
print("Equation 3")
  
# solving the equation and printing the 
# value of unknown variables
print("Values of 3 unknown variable are as follows:")
print(solve((eq1, eq2, eq3), (x, y, z)))

# Дасгал 5. m,n натурал тоонууд өгөгджээ. m n зэрэгтийг ол.

m = int(input('m-ийн утга: '))
n = int(input('n-ийн утга: '))
print(f"m: {m**2},n: {n**2}")

# Дасгал 6. Натурал тоо M ийн хүрдийг хэвлэх.
# Multiplication table (from 1 to 10) in Python

num = 12
# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# Дасгал 7. Натурал N хүртлэх сондгой тоонуудын үржвэрийг олох 
print("====The First 10 Odd Natural Numbers====")
num = int(input('Natural num:'))
for i in num:
    print(2 * i - 1)

# Дасгал 8. Ялгавар нь 2 байх 15 хосыг хэвлэ.


# Жнь: (3,5) (11,13) ........ 16
# Дасгал 9. Тэгш өнцөгт гурвалжны 2 катет өгөгдсөн бол гипотенузыг ол.

#  #Бодлого 3-4 

from re import A


def периметр():
    a = 19
    b = 21
    c = 22
    print( a + b + c )    
периметр()
#  #Бодлого 3-5
# def kvadrattegshtgel():

#     d = int(input('квадтрат тэгштгэлийн шийдийг олох: '))

#     if d > 0:
#         print('Бодит 2 шийдтэй')
#     elif d = 0:
#         print('1 шийдтэй')
#     elif d < 0:
#         print('шийдгүй')
#     else:
#         print('noting')
# kvadrattegshtgel()

def sondgoinemeh():

    list = [a, b, c]

    if list % 3:
        print(a+b+c)
    else:
        print('number is not odd')
sondgoinemeh()


