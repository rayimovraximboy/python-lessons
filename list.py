# List - ro'yxat
user1 = "Bekhruz"
user2 = "Dilbek"
print(user1)
print(type(user2)) # str
users = ['Gulyoro', "Dilbek", 'Margaritta']
# List elementlari indekslanadi
# Dasturlshda indekslash 0 dan boshlanadi
# List elementini olish                 
first_element = users[0]
third_element = users[2]
print(first_element, third_element)
print(type(users)) # list
mixed_data =['test', 12, True, -5.75, False, ['they', 'hi'], 'py', 'js', 25 ]
# List uzunligi (length of list) - ro'yhatdagi elementlar soni
print(len(users))
print(len(mixed_data))
print(mixed_data[5])
# first element
print(mixed_data[0])
# last element
lenght = len(mixed_data)
last_index = lenght - 1
print(mixed_data[last_index])
print(mixed_data[2])
# Ro'yhat elementini o'zgartirish
mixed_data[2] = False
print(mixed_data[2])
# Element qo'shish
# users.append('valeriy')
# print(users)    

users.insert(0, 'Boburbek')
print(users)
users.insert(2, 'Ronaldo')
print(users)

users.insert(len(users) - 1, 'Nodir')
print(users)

# Element o'chirish
# del users[4]
# print(users)
# users.remove('Dilbek')
# print(users)
# users.remove('Margaritta')
# print(users)

# Listdan element sug'urib olish
# List.pop(index?)
deletedElement = users.pop(1)
print(deletedElement)
print(users)

lastElement = users.pop()
print(lastElement)
print(users)


