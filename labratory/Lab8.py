# # # Дасгал 8.1. Жагсаалтын myList[3], myList[-1] элементүүдийг хэвлэ. myList[1] элементэд ? утга олгож, жасгаалтыг бүхэлд нь хэвлэ. Жагсаалтын эхэнд “first” утгатай элемент, төгсгөлд нь “last” утгатай элементийг тус тус нэмж оруул.

# # myList = [1, None, True, 'I am a string', 256, 0]
# # print(myList[3]) # I am a string
# # print(myList[-1]) # 0
# # myList[1] = '?'
# # print(myList) # [1, '?', True, 'I am a string', 256, 0]
# # myList.insert(0, "first")
# # myList.append("last")
# # print(myList) # ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

# # Дасгал 8.2. myList = [1, 2, 3, 4] жагсаалтаас myList[2] элементийг хасаж, жагсаалтыг хэвлэ. Жагсаалтыг бүхэлд нь устга.

# myList = [1, 2, 3, 4]
# del myList[2]
# print(myList) # [1, 2, 4]
# del myList # Жагсаалтыг бүхэлд нь устгана

# # Дасгал 8.3. for давталт ашиглан myList жагсаалтын элементүүдийг хэвлэ.

# myList = ["white", "purple", "blue", "yellow", "green"]
# for color in myList:
# print(color)

# # Дасгал 8.4. len() функц ашиглан жагсаалтын урт, агуулгыг хэвлэ.

# myList = ["white", "purple", "blue", "yellow", "green"]
# print(len(myList)) # 5
# del myList[2]
# print(len(myList)) # 4
# myList.append("red")
# print(myList)) # ['white', 'purple', 'yellow', 'green', 'red']

# # Дасгал 8.5. sort() метод ашиглан жагсаалтын элементүүдийг эрэмбэл.

# lst = [5, 3, 1, 2, 4]
# print(lst)
# lst.sort()
# print(lst) # [1, 2, 3, 4, 5]

# # Дасгал 8.6. samplelist жагсаалтаас элементүүдийг таслан авч, жагсаалтыг хэвлэ.

# sampleList = ["A", "B", "C", "D", "E"]
#  newList = sampleList[2 : -1]
#  print(newList) # ['C', 'D']

# # Дасгал 8.7. Жагсаалтад элементийг агуулж буй эсэхийг шалгаж үр дүнг хэвлэ.

# myList = ["A", "B", 1, 2]
# print("A" in myList) # True
# print("C" not in myList) # True
# print(2 not in myList) # Falsehood


# БИЕ ДААЖ БОДОХ БОДЛОГУУД:
# Бодлого 8-1: 1-ээс 5 тоонуудаар жагсаалт үүсгэ.
# list = [1,2,3,4,5]
# x = int(input('бүхэл тоо оруулах: ')) # a) бүхэл тоо оруулахыг хүсэх 1 мөр код бичих;
# list1 = [1, 2, 3, 4, 5]
# list2 = list1 
# list1[0] = x # b) Жасгаалтын голд байрлах элементийг оруулсан тоогоор солих;
# del list1[4] # c) Жагсаалтын хамгийн сүүлийн элементийг устгах 1 мөр код бичих;
# print(list2)
# print(f'{len(list2)} <-- Жагсаалтын уртыг хэвлэх код\n') # d) Жагсаалтын уртыг хэвлэх 1 мөр код бичих;0
# print('Жагсаалтыг хэвлэнэ')
# for i in list: # e) Жагсаалтыг хэвлэнэ.
# 	print(i)

# Бодлого 8-2: Битлз хамтлагийн гишүүдийн өөрчлөлтийг тусгасан программ бич.


# beatles = [''] # a) beatles нэртэй хоосон жагсаалт үүсгэх;
# result = beatles.append('John Lennon,','Paul McCartney' ) # b) John Lennon, Paul McCartney, ба George Harrison нэр бүхий гишүүдийг нэмэхийн тулд # append() метод ашиглах;


beatles = [] # хоосон жагсаалт үүсгэнэ
beatlesz.append('John Lennon','Paul McCartney',)
for i in beatles: # давталтын бие 5 удаа биелэнэ
	beatles.insert(0, i + 1) # шинэ элемент бүрийг print(myList) # 0 индексэд оруулна

print(i)
# for x in beatles:
# 	x.append('Stu Sutcliffe','Pete Best')
# c) for давталт болон append () метод ашиглан хамтлагийн дараах гишүүд (Stu Sutcliffe ба Pete
# Best)-ийг жагсаалтад нэмж оруулах;
# d) del үйлдэл ашиглан Stu Sutcliffe, Pete Best нарыг жагсаалтаас хасах;
# e) insert () метод ашиглан жагсаалтын эхэнд Ринго Старрыг нэмнэ.
# Бодлого 8-3: Бодлого 8-4: Бодлого 8-5: Бодлого 8-6:
# "D", "F", "A", "Z" тэмдэгтүүдээр жагсаалт үүсгэ. sort метод ашиглан тэдгээрийг эрэмбэл.
# list1 = ["A", "B", "C"] жагсаалт үүсгэ. a) List2 = list1, list3 = list2 утга олго. b) List1 ба List2-ийн 0 индекстэй элементүүдийг тус бүр устга. c) List3 жагсаалтыг хэвлэ.
# sampleList = ["A", "B", "C", "D", "E"] жагсаалт үүсгэ. Жагсаалтаас 1-ээс -3 хүртэлх индекстэй элементүүдийг таслан авч хэвлэ.
# a = ‘A’, b = ‘B’, c = ‘C’, d = ‘ ’ тэмдэгтүүдээр жагсаалт үүсгэ. reverse метод ашиглан тэдгээрийг урвуугаар эрэмбэл.


