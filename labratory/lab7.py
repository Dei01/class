#ЛАБОРАТОРИЙН АЖИЛ No7. ФУНКЦ
# Дасгал 7.1. 2 тооны нийлбэр олох функц зохио.

def sum(num1, num2):
        return num1 + num2
print(sum(2, 3))
print(sum(225, 336))

# Дасгал 7.2. Өндөр жил бол True, бусад тохиолдолд False утгыг буцаах 1 параметртай isYearLeap(year) функц зохио.

def checkYear(year):
# Return true if year is a multiple of 4 and not multiple of 100. # OR year is multiple of 400.
return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) year = int(input('year: '))
if checkYear(year) == True:
else:
print("Leap Year")
print("Not a Leap Year")

# Дасгал 7.3. Тоон утгыг бүхэл тоо, бутархай тоо эсэхийг шалгах функц зохио.

def isInt(number):
       if type(number) == int:
           return True
       elif type(number) == float:
return False
print(isInt(5))
print(isInt(5.0))
print(isInt("5"))

# Дасгал 7.4. Өнөөдрөөс өгсөн өдрийн дараа ямар гараг байхыг олох функц зохио.

def get_weekday(currend_weekday:int, days_ahead: int) -> int: """Өнөөдрөөс өгсөн өдрийн дараа тохиох гарагийн тоог буцаана. Гарагийг
1-7-оор өгнө. Даваа гараг-1, Мягмар гараг–2, ... Ням гараг–7. • current_weekday – өнөөдрийн гарагийг тоогоор өгнө
• days_ahead – хэдэн өдөр """
    return (current_weekday + days_ahead) % 7

# Дасгал 7.5. Хэрэглэгчийн оруулсан a тоог b зэрэгт дэвшүүлэх функц зохио.

def power(a, b):
       if b == 1:
           return a
       else:
return (a * power(a, b-1))
a = int(input('Enter the first number\t: ')) b = int(input('Enter the second number\t: ')) p = power(a, b)
print(a, ' to the power of ', b, ' is ', p)




# # # # def sum(num1, num2):


# # # # num1 = int(input('1 num: '))
# # # # num2 = int(input('2 num: '))
# # # #         return num1 + num2
# # # # print(sum(2, 3))
# # # # print(sum(225, 336))


# # # # tooo awah too oruulah 
# # # # 0-6 nas bol tasalbaraiin une unegui
# # # # 7-14 - deesh 75 $
# # # # 15+ 100$
# # # # ger buliin 5 gishuun tasalbar hudal awna gj toosnguut hummuus nas oruulahaar tulburiig tootsno 
# # # # une tsanaasaa fixed 



# age = int(input(''))
# members = int(input(''))

# if age <= 6:
#     return price 
# elif age >= 75
#     return price1
# else: 
    

# for i in range(1,members+1):
#     print()



a = 0
b = 0
sum = 0
d = 0
members = int(input('Members: '))
for sum in range(1, members + 1, 1):
    b = int(input('age: '))
    if b < 6: 
        c = 0
    else:
        if b < 14:
            c = 75
        else:
            c = 100
    d = d + c

print(f'Total amount: {d}')




# # def getFamilyMembers():
    
# i = 0
# while i < 10:
#     i = i + 1
#     if i == 5:
#         continue
#     print(i)

# i = 0 
# while i < 10:
#     i = i + 1
#     if i==10:
#         continue
#     print(i)

# for x in range(1,10):
#     if x==10:
#         continue
#     print(x)




