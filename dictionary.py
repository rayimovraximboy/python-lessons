# Data types
# 1. integer; 2. float; 3. string; 4. boolean; 5. list; 6. tuple; 7. dictionary
cars = ['audi', 'chevrolet', 'BYD', 'tesla']

# Dictionary (lug'at)
# key-value pair (kalit-qiymat juftligi)
car = {
    'brand': "Ford",
    'name': "Mustang",
    'year': 2000,
    'color': "blue"
}
print(car)
print(type(car)) # <class 'dict'>

student = {
    'fullname': "John Doe",
    'age': 20,
    'course': 3,
    'favorite_books': ["Atomic habits", "O'tkan kunlar", "Dunyoning ishlari"],
    'is_completed': False,
    'is_married': True
}
# 1. Qiymatlar olish
print(student['fullname'])
print(student['age'])
print(student['favorite_books'])        

for book in student['favorite_books']:
    print(book)

# 2. Qiymatlarni o'zgartirish
student['age'] = 21
student['course'] = 4
print(student)

# 3. Yangi key-value qo'shish
student['hobbies'] = ["Reading a book", 'Watching a football match', 'Learning knowledges']
print(student)

# 4.Key-value ni o'chirish
del student['is_married']
print(student)

# 5. Empty dict(bo'sh lug'at)
talaba_1 = {}

talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# get() metodi
telefonlar = {
     'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
}
print(telefonlar.get('vali')) # galaxy s9
print(telefonlar.get('akmal')) # None

# Amaliyot
otam = {
    'ism': 'Alisher',
    'yosh': 42,
    'kasb': 'Electrik',
     't_yil': 1984
}
print(otam)

onam = {
    'ism': 'Surayyo',
    'yosh': 43,
    'kasb': 'oshpaz',
    't_yil': 1983
}
print(onam)

taomlar = {
    'bexruz': 'palov',
    'elbek': 'logmon',
    'sardor': 'osh',
    'qobil': 'manti'
}
print(taomlar)
print(f"Elbekning sevimli taomi {taomlar['elbek']},  Qobilning sevimli taomi {taomlar['qobil']}")