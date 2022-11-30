# METHOD 

# hello.append(x) # add number to the lsit 
# hello.clear() # Removes all elements from the list lst–which becomes empty.
# hello.copy()
from pkg_resources import fixup_namespace_packages


lst = [1, 2, 3]
print(lst.copy())
print(type(lst.copy()))
print(type(lst))



# hello.count()
# hello.extend(iter)
# hello.index(x)
# hello.insert(i,x)
# hello.pop()
# hello.remove(x)
# hello.reverse()
# hello.sort()


numbers = [111, 7, 2, 1]
print(len(numbers)) # жагсаалтын уртыг хэвлэнэ 
print(numbers) # жагсаалтыг хэвлэнэ 
numbers.append(4) # жагсаалтад элемент нэмж байна 
print(len(numbers)) # жагсаалтын уртыг хэвлэнэ 
print(numbers) # жагсаалтыг хэвлэнэ
numbers.insert(0, 222) # жагсаалтын эхэнд 222 утгыг нэмнэ 
print(len(numbers)) # жагсаалтын уртыг хэвлэнэ 
print(numbers) # жагсаалтыг хэвлэнэ


myList = []
#FIXME: 
for i in range(5):
    myList.append(i+1)
print(myList)

myList1 = []

for x in range(5):
    myList1.insert(0, x + 1)
    
print(myList1)
#TODO:
list2 = [1, 10, 4, 100, 59, 600, 734, 8123, 9555]
list2.reverse()
list2.sort()
list2.pop()
print(list2)

#//TODO:
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    
for f in sorted(set(basket)):
    print(f)