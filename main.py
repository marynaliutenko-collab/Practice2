from mod import fibonacci
#Завдання 1.1
from math import sin
def expression (x):
    if x > 45:
     z = -(x ** 0.5)
    else:
     z = sin(2 * x)
    return z
x = int(input("Введіть значення x: "))
print ("Значення виразу z = ", expression(x))
p = int(input("Введіть значення p: "))
print("перше число Фібоначчі, що більше за p: ", fibonacci(p))
