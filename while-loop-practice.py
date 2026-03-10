# 1
savol = "Sevgan kitobingizni kiriting"
savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

while True:
    kitob = input(savol)
    if kitob == 'exit':
        break
print('Rahmat!')  
# 2 
savol = "Yoshingiz nechada? Yoshingizni kiriting, sizga chipta narhini chiqarib beramiz: "

while True:
    yosh = input(savol)
    if yosh == 'exit' or yosh == 'quit':
        print("Dastur to'xtadi")
        break

    yosh = int(yosh)
    if yosh<7:
      print("2000 so'm")
    elif 7<=yosh<18:
      print("3000 so'm")
    elif 18<=yosh<65:
      print("10000 so'm")
    else: 
       print("Bepul")
# 3
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
     
