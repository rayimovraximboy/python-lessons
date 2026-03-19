# Dictionary elementlari bilan ishlash
phone = {
    'brand': 'Apple',
    'model': 'iPhone 17 Pro',
    'color': 'Black',
    'price': 1500,
    'year': 2025
}
# 1. get metodi - kalit orqali qiymatni olish
print(phone.get('model')) # iPhone 17 Pro
print(phone.get('price', "Narx topilmadi")) # 1500
print(phone.get('battery', "Kalit topilmadi")) # Kalit topilmadi

# 2. items() metodi - lug'at elementlarini (kalit-qiymat) juftlari sifatida olish
print(phone.items()) # dict_items([('brand', 'Apple'), ('model', 'iPhone 17 Pro'), ('color', 'Black'), ('price', 1500), ('year', 2025)])
for key, value in phone.items():
    print(f"{key}: {value}")

telefonlar = {
    'ali': 'iPhone 17 Pro',
    'vali': 'Samsung Galaxy S30',
    'olim': 'Xiaomi Mi 12',
    'orif': 'Google Pixel 7'
}

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

# 3. keys() metodi - lug'atning barcha kalitlarini olish
print(phone.keys()) # dict_keys(['brand', 'model', 'color', 'price', 'year'])
print(telefonlar.keys()) # dict_keys(['ali', 'vali', 'olim', 'orif'])

mahsulotlar = {
    'olma': 5000,
    'banan': 3000,
    'apelsin': 4000,
    'uzum': 6000
}

# print(mahsulotlar.keys())
print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 4. in operatori
# 1. listda in operatori qiymatning mavjudligini tekshiradi
fruits = ['olma', 'banan', 'apelsin', 'uzum']
print('olma' in fruits) # True
print('anor' in fruits) # False

fruit = input("Qaysi meva yoqadi? ")
if fruit in fruits:
    print(f"{fruit.title()} do'konimizda bor.")
else:   
    print(f"{fruit.title()} do'konimizda yo'q.")

bozorlik = ['anor', 'shaftoli', 'gilos', 'non']
# for mahsulot in bozorlik:
#     print(mahsulot) # lug'atning kalitlari bo'ladi

# mahsulotlar - lug'at, bozorlik - ro'yxat, mahsulot - lug'atning kaliti
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
      print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

print(sorted(mahsulotlar.keys())) # ['apelsin', 'banan', 'olma', 'uzum']
print("Do'kondagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# 5. values() metodi - lug'atning barcha qiymatlarini olish
print(phone.values()) # dict_values(['Apple', 'iPhone 17 Pro', 'Black', 1500, 2025])
print(telefonlar.values()) # dict_values(['iPhone 17 Pro', 'Samsung Galaxy S30', 'Xiaomi Mi 12', 'Google Pixel 7'])

telefonlar = {
    'ali': 'iPhone 17 Pro',
    'vali': 'Samsung Galaxy S30',
    'olim': 'Xiaomi Mi 12',
    'orif': 'Google Pixel 7',
    'hamida': 'OnePlus 11',
    'maryam': 'Redmi Note 12 Pro',
    'tohir': 'Realme GT Neo 5',
    'umar': 'Vivo X80 Pro'
}

print("Foydalanuvchilar quidagi telefonlarni ishlatishadi:")
for tel in telefonlar.values():
    print(tel)