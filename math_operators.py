PI = 3.14
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
 
def modulus(a, b):
    return a % b    

for i in range(1, 11):
    print(f"{i} * 5 = {multiplication(i, 5)}")
    