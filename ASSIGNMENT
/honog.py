

# x = int(input(' Хоног: '))

# if x >= 0:
#     multiply = x * 24 * 60 * 60
    
#     print(f'{multiply} seconds')
  
# Бодлого 2 say dolaroo odoo awahuuu 
#     30 honogiin daraa awahuu 
#   0.01 dollor udur bolgon 2 dahin nemegden 

#   x = int(input('$: '))
# fv = pv * (1 + r)^t
# vf: Future Value
# pv: Present Value
# r: Rate
# t: Time


def doublePenny():
    a = int(1_000_000)
    b = 0.01 *(2**30)
    choice = int(input('1 - сая төгрөгөө одоо авах: \n2 - оруулсан хоногт 0.01 -ийг double-даж авах\nСонголт оруулах:  '))
    
    if 1 == choice:
        print(f'одоо авах мөнгө: {a} $')
    elif 2 == choice:
        print(f'30 хоногт double-даж авах мөнгө: {b} $')
    else: 
        return
doublePenny()

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

# мөнгө, бэлэг, хоног = 1, 0.01, 1
# while True:
#     мөнгө += бэлэг
#     if мөнгө >= 1000000:
#         break
#     бэлэг *= 2
#     хоног += 1


# print(f"Хоног {хоног}, авах бэлэг ${бэлэг:,} нийт авах мөнгө ${мөнгө:,}.")

# def main():
#     num_input = int(input('How many days do you have? '))
#     # Accumulate the total
#     total = 0.01
#     for day_num in range(num_input):
#         if day_num == 0:
#             print("Day: ", day_num, end=' ')
#             total = total
#             print("the pennies today are:", total)
#             day_num += day_num
#         else:    
#             print("Day: ", day_num + 1, end=' ')
#             total += 2 * total
#             print("the pennies today are:", total)






