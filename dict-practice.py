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
for key, value in sorted(izohli_l.items()):
     print(f"{key.title()}: {value}")

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
    print("Bizda bunday davlat yo'q")

# 4.
r_menusi = {
    'osh': 15000,
    'shashlik': 20000,
    'somsa': 5000,
    'lag\'mon': 12000,
    'manti': 10000,
    'qabuli': 18000,
    'plov': 16000,
    'shurup': 8000,
    'qozonkatak': 14000,
    'dimlama': 17000,
    'chuchvara': 9000,
}
jami = 0
taom1 = input("1-taom: ")
taom2 = input("2-taom: ")
taom3 = input("3-taom: ")

for taom in [taom1, taom2, taom3]:
    if taom in r_menusi:
        print(taom, "narxi:", r_menusi[taom])
        jami += r_menusi[taom]
    else:
        print(taom, "- bizda bunday taom yo'q")

print("Jami hisob:", jami, "so'm")


