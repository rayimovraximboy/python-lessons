# # # Pythonda modullar
# # # import math
# # # print(math.sqrt(16))
# # # print(math.pi)
# 1. modul ichidagi barcha elementlarni chaqirish
# m = 5
# import math_operators as m
# # # print(math_operators.addition(7, 8))
# # # print(math_operators.multiplication(5, 8))
# # # print(math_operators.division(10, 2))
# # # print(math_operators.PI)
# print(m.subtraction(10, 4))

# 2. 
# modul ichidan faqatgina kerakli variableni chaqirish
# from math_operators import addition, multiplication, PI 
# print(addition(5, 7))
# print(multiplication(3, 4))
# print(PI)

# # 3. * modul ichidan barcha elementlarni chaqirish
# from math_operators import *
# print(multiplication(7, 4))
# print(addition(10, 3))
# print(PI)

# 4. python random modul
import random as r
# print(r.random()) # 0 dan 1 gacha bo'lgan tasodifiy sonni qaytaradi
# print(r.randint(1, 100)) # 1 dan 100 gacha bo'lgan tasodifiy butun son

ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(0,51,5))
print(x)
print(r.choice(x))