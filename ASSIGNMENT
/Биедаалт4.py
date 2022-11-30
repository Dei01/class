import math

def songolt():
      
    a = "1.000.000$"
    choice = int(input('1 - сая төгрөгөө авах , 2 - Doubelдаж авах  Сонголт: '))
    
    if 1 == choice:
        print(f'одоо авах мөнгө: {a} $')
    elif 2 == choice:
        d = int(input('Хэдэн өдөрт: ')) 
        
 
        b = 0.01 * d 
        print(f'30 хоногт double-даж авах мөнгө: {b} $')
    else: 
        print('nothing')

songolt()

def money_days(start, days):
        power2days = math.pow(2, days)
        amount = start * power2days
        print(amount)
 
money_days(0.01, 30)
 
# def days(d):
#     if d <= 1:
#         return 0.01
#     else:
#         return days(d-1) * 2
 
# while True:
#     d = int(input("number of days (0 to stop): "))
#     if d == 0:
#         break
#     else:
#         print("Total amount: " + str(days(d)))