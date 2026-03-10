# String - matn
# Data types: 1. string(matn) 2. number(son)
# region = "Xorazm"
# city = "Shovot"
# street = "Ibn Sino"
# emoji = "😀"
# firstname = "Raximboy"
# lastname = "Rayimov"

# # Matnlarni qo'shish
# adress = "Men " + region + " Viloyati " + city + " tumanida yashayman"
# full_name = "Mening to'liq ismim familyam " + firstname + " "  +  lastname
# print(adress)
# print(full_name)

# # f-string
# name = f"Mening to'liq ism familyam {firstname} {lastname}" 
# full_address = f"Men {region} viloyatida {city} tumanida yashayman"
# print(name)
# print(full_address)

# # Amaliyot
# kocha = "Ibn sino"
# mahalla = "Taraqqiyot"
# tuman = "Shovot"
# viloyat = "Xorazm"
# address = f" {kocha} ko'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati" 
# print(address)
# # Vazifa
# a = 4
# b = 8
# c = 2
# orta_a = (a + b + c) / 3
# orta_g = (a * b * c) ** (1 / 3)
# print(orta_a)
# print(orta_g)

# String metodlari(methods)
firstname = "John"
lastname = "Doe"
fullname  = f"{firstname} {lastname}" # Jhon Doe
# upper () / lower()
print(fullname.upper()) #JHON DOE
print(fullname.lower()) # jhon doe
print('Adminjon'.upper())
# title() / capitalize()
print('Welcom to uzbekistan'.title()) # Welcom To Uzbekistan
print("Where are you from?".title()) # Where Are You From?
print('manual tester'.capitalize())
fullname = fullname.capitalize() # John Doe
print(fullname)

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")

# # Input()
# nickname1 = '@Rakhimoff_524'
# nickname2 = input("Iltimos, Instagram  nicknamei kriting:")
# print("1-account:", nickname1)
# print("Foydalanuvchi account:", nickname2)

# Amaliyot
kocha = input("Iltimos, ko'changizni kiriting")
mahalla = input("Iltimos, mahallangizni kiriting")
tuman = input("Iltimos, tumaningizni kiriting")
viloyat = input("Iltimos, viloyatingizni kiriting")
manzil = f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati,"
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
print(manzil.title())

