# БОДЛОГУУД:


# 1. Гурвалжны 3 тал өгөгдсөн бол (гурвалжны тал болох эсэх нөхцлийг шалгаж) гурвалжны талбай ба периметрийг олох программ зохио.
print('# 1. Гурвалжны 3 тал өгөгдсөн бол (гурвалжны тал болох эсэх нөхцлийг шалгаж) гурвалжны талбай ба периметрийг олох программ зохио.')
# method 1

# inputString = input('Зай аваад 3-н тоо оруулах: ')
# list = inputString.split()
# sum = 0 
# for num in list:
#     sum+= int(num)
# print(f'периметр = {sum}\n')
# print(f'талбай = {sum/2}\n')



# # method 2 (FIXED) 

# a,b,c = 1,2,3
# result = a + b + c
# print(result)


# 2. 100-аас бага тэгш тоонуудыг do оператор ашиглан хэвлэх программ зохио.
print('# 2. 100-аас бага тэгш тоонуудыг do оператор ашиглан хэвлэх программ зохио.')

# Python program to print Even Numbers in given range
start, end = 1, 100
# iterating each number in list
for num in range(100):
      
    # checking condition
    if num % 2 == 0:
        print(num, end = "")
        
print('\n')




# # 3. Дурын n тоон цувааны үржвэрийг while оператор ашиглан хэвлэх программ зохио.
# print('# 3. Дурын n тоон цувааны үржвэрийг while оператор ашиглан хэвлэх программ зохио.')

# x = int(input('Enter random number for loop: '))
# i = 1
# while i < x:
#   print(i,end = " ")
#   i += 1





# # 4. For давталт ашиглан 1-ээс n хүртэлх тоог 3 алхамтайгаар өсөхөөр хэвлэх программ зохио.
# print('# 4. For давталт ашиглан 1-ээс n хүртэлх тоог 3 алхамтайгаар өсөхөөр хэвлэх программ зохио.')

# i = 0
# for i in range(3):
#     i+=1
#     print(i)




# # 5. For давталт ашиглан 1-ээс 10 хүртэлх тоонуудын нийлбэрийг хэвлэх программ зохио.
# print('# 5. For давталт ашиглан 1-ээс 10 хүртэлх тоонуудын нийлбэрийг хэвлэх программ зохио.')

# # x = 0
# # for x in range(1,10):
# for i in range(0, 10, 2):
#     print(i, end=" ")
# print()





# # 6. Өгсөн а тооны n хүртэлх зэргүүдийг хэвлэх программ зохио.
# print('# 6. Өгсөн а тооны n хүртэлх зэргүүдийг хэвлэх программ зохио.')

# n = int(input('Тоо:ро'))






# # 7. 100-аас бага 3 –д хуваагдах тоонуудыг буурахаар хэвлэх программ зохио.
# print('# 7. 100-аас бага 3 –д хуваагдах тоонуудыг буурахаар хэвлэх программ зохио.')

# x = 100
# for i in x:
#     if x3:
#         print(i)






# # 8. Дурын тэмдэгт мөр хувьсагчийг (жнь: hello) n удаа дараалан болон шинэ мөрөнд хэвлэх программ зохио.
# print('# 8. Дурын тэмдэгт мөр хувьсагчийг (жнь: hello) n удаа дараалан болон шинэ мөрөнд хэвлэх программ зохио.')








# # 9. 1-ээс n хүртэлх сондгой тоонуудын нийлбэрийг олох программ зохио.
# print('# 9. 1-ээс n хүртэлх сондгой тоонуудын нийлбэрийг олох программ зохио.')










# # 10. Өгсөн m тооны квадрат болон куб зэргүүдийг хэвлэх программ зохио.
# print('# 10. Өгсөн m тооны квадрат болон куб зэргүүдийг хэвлэх программ зохио.')







# # 11. 2-оос 100 хүртэлх бүх тэгш тоог for ашиглан хэвлэх программ зохио.
# print('# 11. 2-оос 100 хүртэлх бүх тэгш тоог for ашиглан хэвлэх программ зохио.')

# start, end = 1, 100
#   # iterating each number in list
# for num in range(start, end + 1):
      
#     # checking condition
#     if num % 2 == 0:
#         print(num, end = " ")
# print('\n')








# # 12. Өгсөн m тооны хүрдийг хэвлэх программ зохио.
# print('# 12. Өгсөн m тооны хүрдийг хэвлэх программ зохио.')

# hurd = int(input(''))








# # 13. 1-ээс 100 хүртэлх бүх сондгой тоог while ашиглан хэвлэх программ зохио.
# print('# 13. 1-ээс 100 хүртэлх бүх сондгой тоог while ашиглан хэвлэх программ зохио.')

# maximum = int(input(" сондгой тоонууд хэвлэх : "))
# number = 1
# while number <= maximum:
#     if(number % 3 != 0):
#         print(number, end="")







# # 14. Өгсөн n бүхэл тооны факториалыг олох программ зохио.
# print('# 14. Өгсөн n бүхэл тооны факториалыг олох программ зохио.')

# def factorial(n):
#     res = 1
#     for i in range(2, n+1):
#         res *= i
#     return res
#  # Driver Code
# num = 5;
# print("Factorial of", num, "is",
# factorial(num))







# # 15. Өгсөн n тоо хүртэлх сондгой тоонуудын факториалуудын нийлбэрийг олох программ зохио.
# print('# 15. Өгсөн n тоо хүртэлх сондгой тоонуудын факториалуудын нийлбэрийг олох программ зохио.')      
      







# # 16. [50, 100] завсарт орших 7-д хуваагддаг тоонуудын цифрүүдийн нийлбэрийг олох программ зохио.
# print('# 16. [50, 100] завсарт орших 7-д хуваагддаг тоонуудын цифрүүдийн нийлбэрийг олох программ зохио.')


# # enter the starting range number
# start_num = int(50)  
# # enter the ending range number
# end_num = int(100)
# # initialise counter with starting number
# cnt = start_num
# # check until end of the range is achieved
# while cnt <= end_num: 
#     # if number divisible by 7 and 5
#     if cnt % 7 == 0 :
#         print(cnt, " нь 7-д хуваагддаг.")     
#     # increment counter
#     cnt += 1







# # 17. Тоог урдаас нь хойш, хойноос урагш бичихэд тэнцүү байх тоог хөрвөсөн тоо буюу “палиндром тоо” гэдэг. [100, 150] завсарт байх палиндром тоонуудыг хэвлэх программ зохио.
# print('# 17. Тоог урдаас нь хойш, хойноос урагш бичихэд тэнцүү байх тоог хөрвөсөн тоо буюу “палиндром тоо” гэдэг. [100, 150] завсарт байх палиндром тоонуудыг хэвлэх программ зохио.')









# # 18. [100, 200] завсарт орших тоонуудаас 25-д хуваагдах тоонуудын хөрвөсөн тоог хэвлэх программ зохио.
# print('# 18. [100, 200] завсарт орших тоонуудаас 25-д хуваагдах тоонуудын хөрвөсөн тоог хэвлэх программ зохио.')


# # 19. N бүхэл тоо өгөгджээ. 1-ээс N хүртэлх тэгш тоонуудыг өөрөөс нь 2 дахин бага тоон зэрэгт дэвшүүлж гарсан утгуудын нийлбэрийг олох программ зохио.
# print('# 19. N бүхэл тоо өгөгджээ. 1-ээс N хүртэлх тэгш тоонуудыг өөрөөс нь 2 дахин бага тоон зэрэгт дэвшүүлж гарсан утгуудын нийлбэрийг олох программ зохио.')


# # 20. 1100110 ба 10101 тоонууд хооронд логик and, or, xor үйлдлүүд хийж зөв # хариуг 10 ба 2-тын тоогоор харуул;
# print('# 20. 1100110 ба 10101 тоонууд хооронд логик and, or, xor үйлдлүүд хийж зөв хариуг 10 ба 2-тын тоогоор харуул;')


# # 21. 16 суурьтай системд өгсөн тоог 10 суурьтай тооллын системд хөрвүүлэх.
# print('# 21. 16 суурьтай системд өгсөн тоог 10 суурьтай тооллын системд хөрвүүлэх.')

# # 22. N бүхэл тоо өгөгджээ. 1-ээс N хүртэлх бүх сондгой тоогоос квадрат язгуурыг # бодож, гарсан утгуудын нийлбэрийг олох программ зохио.
# print('# 22. N бүхэл тоо өгөгджээ. 1-ээс N хүртэлх бүх сондгой тоогоос квадрат язгуурыг бодож, гарсан утгуудын нийлбэрийг олох программ зохио.')


# # 23. 1100110 ба 10101 тоонууд хооронд нэмэх, хасах, үржих үйлдлүүд хийж зөв хариуг 10 ба 2-тын тоогоор харуул.

# pirnt('# 23. 1100110 ба 10101 тоонууд хооронд нэмэх, хасах, үржих үйлдлүүд хийж зөв хариуг 10 ба 2-тын тоогоор харуул.')
# # 24. Өгсөн а тоог анхны тоо эсэхийг шалгах программ зохио.
# print('# 24. Өгсөн а тоог анхны тоо эсэхийг шалгах программ зохио.')

# # 25. [a, b] завсар дахь хөрвөсөн тооноосоо их байх тоонуудыг хэвлэ.
# print('# 25. [a, b] завсар дахь хөрвөсөн тооноосоо их байх тоонуудыг хэвлэ.')

# # 26. Өгсөн n хүртэлх тоонуудын факториалуудын нийлбэрийг олох программ зохио.
# print('# 26. Өгсөн n хүртэлх тоонуудын факториалуудын нийлбэрийг олох программ зохио.')

# # 27. Өөрийнхөө цифрүүдийн нийлбэрт хуваагддаг 3 оронтой тоог “сайн тоо”гэдэг. Бүх сайн тоог хэвлэ. Мөн хэд байгааг тоолох программ зохио.
# prnit('# 27. Өөрийнхөө цифрүүдийн нийлбэрт хуваагддаг 3 оронтой тоог “сайн тоо”гэдэг. Бүх сайн тоог хэвлэ. Мөн хэд байгааг тоолох программ зохио.')

# # 28. Фибоначчийн эхний к ширхэг гишүүнийг хэвлэ (Фибоначчийн тоо нь дараах дарааллаас бүрдэнэ: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .... Тодорхойлолт ёсоор бол Фибоначчийн тооны эхний 2 тоо нь 0 болон 1 гэж өгөгдсөн ба түүнээс хойшхи Фибоначчийн тоонууд нь өмнөх 2 тооныхоо нийлбэртэй тэнцүү болно).
# print('28. Фибоначчийн эхний к ширхэг гишүүнийг хэвлэ (Фибоначчийн тоо нь дараах дарааллаас бүрдэнэ: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .... Тодорхойлолт ёсоор бол Фибоначчийн тооны эхний 2 тоо нь 0 болон 1 гэж өгөгдсөн ба түүнээс хойшхи Фибоначчийн тоонууд нь өмнөх 2 тооныхоо нийлбэртэй тэнцүү болно).')
# # 29. 2 суурьтай системд өгсөн тоог 10 суурьтай тооллын системд хөрвүүл.
# print('# 29. 2 суурьтай системд өгсөн тоог 10 суурьтай тооллын системд хөрвүүл.')

# # 30. 4 оронтой бүх палиндром тоог хэвлэж, нийт хэдэн тоо байгааг тоол.
# print('# 30. 4 оронтой бүх палиндром тоог хэвлэж, нийт хэдэн тоо байгааг тоол.')


