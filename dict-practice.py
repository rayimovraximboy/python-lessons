# Amaliyot
# 1.
izohli_l = {
    'boolean': 'mantiqiy qiymat',
    'integer': 'butun son',
    'float': 'o\'nlik son',
    'string': 'matn',
    'list': 'ro\'yxat',
    'dict': 'lug\'at',
    'tuple': 'o\'zgarmas ro\'yxat',
    'set': 'to\'plam',
    'input': 'foydalanuvchi kiritgan ma\'lumot',
    'print': 'ma\'lumotni ekranga chiqarish'
}
for kalit in sorted(izohli_l):
     print(f"{kalit.title()}: {izohli_l[kalit]}")

# 2.
dunyo_davlatlari = {
'Dunyo davlatlari': 'Davlat poytaxtlari',
'Uzbekiston': 'Toshkent',
'Qozogiston': 'Astana',
'Rossiya': 'Moskva',
'Turkiya': 'Anqara',
'Fransiya': 'Parij',
'Germaniya': 'Berlin',
'Amerika': 'Vashington',
'Italiya': 'Rim',
}

for davlat in sorted(dunyo_davlatlari):
    if davlat != 'Dunyo davlatlari':
        print(f"{davlat.title()}ning poytaxti {dunyo_davlatlari[davlat]}")

# 3.
davlatlar = {
    "uzbekiston": "Toshkent",
    "qozogiston": "Astana",
    "rossiya": "Moskva",
    "turkiya": "Anqara",
    "fransiya": "Parij",
    "germaniya": "Berlin"
}
davlat = input("Davlat nomini kiriting: ")

if davlat in davlatlar:
    print("Poytaxt:", davlatlar[davlat])
else:
    print("Bizda bunday ma'lumot yo'q")

# 4.
r_menusi = {
    'osh': 15000,
    'shashlik': 20000,
    'somsa': 5000,
    'lag\'mon': 12000,
    'manti': 10000,
}