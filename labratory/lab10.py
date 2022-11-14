#ЛАБОРАТОРИЙН АЖИЛ No10. ФУНКЦ
# TUPLE , DICTIONARY


input_string = input('Enter num: ')
list = input_string.split()
sum = 0
for num in list:
	sum += int(num)
print(sum)

# Tuple  <-- is tuple is immutable, unlike lists that are mutable.

dictionary = {''} # we can assign numbers in dic


grade = {'A1': 80, 'A2': 70, 'A3': 90}
for assignment in grade:
	print(f'{assignment} : {grade[assignment]}')


d = {'b':2, 'a':1, 'c':3}

for mongolian,numbers in d:
	print(f'{mongolian} : {numbers}')
print(2 in d) # checking variables VARIABLE = OBJECT
print('a' in d)
object in d

#TODO:
#METHOD VS FUNCTION 
#METHODS are used for connect to variables 
#FUNCTIONS can be called anywhere in the script.
ssh-keygen -t ed25519 -C "baqateacate@gmail.com"
ssh-keygen -t rsa -b 4096 -C “baqateacate@gmail.com”





