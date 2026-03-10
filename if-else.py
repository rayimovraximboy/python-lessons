# age = int(input("Yoshingizni kiriting"))
# if age > 18:
#     print("Kirish huquqiga egasiz")
# else: 
#     print("Siz hali yoshsiz")   

# ball = int(input("Ballingizni kiriting :"))
# if ball < 56:
#     print("Siz imtihondan o'ta olmadingiz")
# elif ball >= 56 and ball < 70:
#     print("Siz imtihondan 3 baho bilan o'tdingiz")   
# elif ball >= 70 and ball < 86:
#     print("Siz imtihondan 4 baho bilan o'tdingiz")   
# elif ball >= 86 and ball < 100:
#     print("Siz imtihondan 5 baho bilan o'tdingiz")  
# else:
#     print("Iltimos, 0 dan 100 gacha ball kiriting")


# age = int(input("Yoshingizni kiriting"))
# if age > 16:
#     print("Siz posport olasiz")
# else: 
#     print("Siz hali posport olaolmaysiz")  

# number = int(input("Sonni kiriting")) 
# if number > 0:
#     print("Musbat son")
# else:         
#     print("Manfiy son")

# son = int(input("Sonni kiriting"))
# if son  % 2 == 0:
#     print("Toq son")
# else:
#     print("Juft son")

# Amaliyot
# 1-Mashq
# son = int(input("Sonni kiriting"))
# if son  % 2 == 0 and son % 3 == 0:
#     print("6 ga bo'linadi")
# else:
#     print("6 ga bo'linmaydi")

# 2-Mashq
# a = int(input("Uchburchakning 1-tomonini kiriting: "))
# b = int(input("Uchburchakning 2-tomonini kiriting: "))
# c = int(input("Uchburchakning 3-tomonini kiriting: "))

# if a + b > c and a + c > b and b + c > a:
#     print("Uchburchak yasash mumkin")
# else: 
#     print("Uchburchak yasab bo'lmaydi")

# 3-Mashq
# a = int(input("1-tomonini kiriting: "))
# b = int(input("2-tomonini kiriting: "))
# c = int(input("3-tomonini kiriting: "))
# if a < b < c:
#        print("Yes")
# else:
#        print("NO")       

# # 4-Mashq
# a = int(input("1-tomonini kiriting: "))
# b = int(input("2-tomonini kiriting: "))
# if a > b:
#      print(a)
# else:
#       print(a,b)     

# 5-Mashq      
# a = int(input("1-tomonini kiriting: "))
# b = int(input("2-tomonini kiriting: "))
# if a <= b:
#      a = 0
#      print(a, b)
# else:
#       print(a, b)    

# import math
# # 6-Mashq
# a = int(input("1-tomonini kiriting: "))
# b = int(input("2-tomonini kiriting: "))
# c = int(input("3-tomonini kiriting: "))
# if a >= b >= c:
#     print(2 * a, 2 * b, 2 * c)
# else:
#     print(math.fabs(a), math.fabs(b), math.fabs(c))

# 7-Mashq 
# x = int(input("1-tomonini kiriting: "))
# y = int(input("2-tomonini kiriting: "))
# a = (2 * x * 2 * y) 
# b = (x + y) / 2
# if x > y:
#     x = a
#     y = b
# else:
#     x = b
#     y = a

# print("%.1f" % x, "%.1f" % y)

# 8-Mashq
# x = float(input("x ni kiriting"))
# y = float(input("y ni kiriting"))
# if x < 0 and y < 0:
#       print(abs(x), abs(y))
# elif x < 0 or y < 0:
#       print(x + 0.5, y + 0.5)
# else: 
#    print(x, y)

# Uyga vazifa 45
# import math
# # a = int(input("1-sonni kiriting :"))
# # b = int(input("2-sonni kiriting :"))
# # c = int(input("3-sonni kiriting :"))
# # d = b ** 2 - 4 * a * c
# # if d < 0:
# #       print("NO")
# # else:
# #      x1 = (-b + math.sqrt(d)) / (2 * a)
# #      x2 = (-b - math.sqrt(d)) / (2 * a)
# #      print("%.1f" % x1, "%.1f" % x2)

# # 38 - Mashq
# x = float(input("1-sonni kiriting"))
# y = float(input("2-sonni kiriting"))
# z = float(input("3-sonni kiriting"))
# if x >= 1 and x <=3:
#     print(x)
# if y >= 1 and y <=3:
#     print(y)
# if z <= 1 and z <= 3:
#    print(z)

# 40 - Mashq
# x = int(input("1-sonni kiriting"))
# y = int(input("2-sonni kiriting"))
# z = int(input("3-sonni kiriting"))   
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2 
   
# print(x, y, z)

# 12.77, 15.88, -75, 18, 0, 89, 25
# max - eng katta
# min - eng kichik => -75
# print(max( 12.77, 15.88, -75, 18, 0, 89, 25))
# print(min(12.77, 15.88, -75, 18, 0, 89, 25))

# # 31-Mashq
# x = float(input("1-sonni kiriting :"))
# y = float(input("2-sonni kiriting :"))
# z = float(input("3-sonni kiriting :"))
# print(max(x, y, z), min(x, y, z))

# 33-Mashq
# x = float(input("1-sonni kiriting :"))
# y = float(input("2-sonni kiriting :"))
# z = float(input("3-sonni kiriting :"))
# print(max(x + y  + z, x, y, z), min(x + y / 2, x, y, z ) ** 2)

# a = float(input("1-sonni kiriting :"))
# b = float(input("2-sonni kiriting :"))
# c = float(input("3-sonni kiriting :"))
# d = float(input("4-sonni kiriting :"))
# max_value = max(a, b , c, d)
# min_value = min(a, b , c, d)
# if a <= b<= c<= d:
#     a = b = c = d = max_value
# else:
#     a = b = c = d = min_value
   
# print(max_value, min_value)

# Uyga vazifa
# import math
# x = float(input("1-sonni kiriting :"))
# y = float(input("2-sonni kiriting :"))
# a = (x + y) / 2
# b = 2 * x * y
# if x < y:
#     x = a
#     y = b
# elif x > y:
#     x = b
#     y = a
# else:
#     x = x
#     y = y

# print(x, y)

x = float(input("1-sonni kiriting :"))
y = float(input("2-sonni kiriting :"))
z = float(input("3-sonni kiriting :"))
min_value = min(x, y, z)
if x < 1 and y < 1 and z < 1:
    if x == min_value:
       x = (y + z) / 2
    elif min_value == y:
       y = (x + z) / 2
    else:
       z = (x + y) / 2
else:
   x = x
   y = y
   z = z

print(x, y, z)




