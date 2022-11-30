# # # List 

# # list = [1, 2, 3, 4, 5] # = list
# # b = (1, 2, 3, 4, 5) # = Tuple 
# # c = {1, 2, 3, 4, 5} # = 

# # list2 = list # assign to the new variable !
# # list[0] = 5

# # print(list2) 
# # print(list) 
# # print(list[:2]) 
# # print(list[3:]) # [Start: End]


# # # print(a[-2])
# # print(b[3])
# # # for i in a:

# # REVERSE()
# # NEXT()
# # POP()

# a_list = ['datagy', 1,[3,4,5], 14.3, 32, 3]
# last_item = next(reversed(a_list)) # same as POP() funvtion

# last_item1 = a_list.pop()
# print(last_item)
# print(last_item1)
# #--------------------------------------------------------------------------
# myList = [10,8,6,4,2]

# newList = myList[:2]
# print(newList[:2])
# print(myList[1:-1])
# print(myList[-1]) # calling index 
# print(f'---> {len(myList)}') # checking lenght 



# a_list = ['datagy', 1,[3,4,5], 14.3, 32, 3]
# last_item = a_list[-1]

# print(last_item)

numbers = [111, 1, 7, 2, 1]
print("Өнөөгийн жагсаалтын урт:", len(numbers)) # Өнөөгийн жагсаалтын уртыг хэвлэнэ 
print("Хуучин жагсаалтын урт:", numbers) # Өнөөгийн жагсаалтын уртыг хэвлэнэ 
del numbers[1] # 2 дахь элементийг устгана
del numbers[2] # 2 дахь элементийг устгана
print("Шинэ жагсаалтын урт:", len(numbers)) # Шинэ жагсаалтын уртыг хэвлэнэ 
print("\nШинэ жагсаалт :", numbers) # Шинэ жагсаалтын агуулгыг хэвлэнэ


temp = [18, 20, 22.5, 24]
print(temp[3 : 4])
print(temp[4]) #   INDEXERROR: LIST INDEX OUT OF RANGE



