import math

x = int(input("Введите х:\n"))
n = int(input("Введите n:\n"))

if n < 0:
    print("error")

f = x**n/math.factorial(n)

print("x^n/n!:", f, "\n")


x = int(input("Введите х:\n"))
n = int(input("Введите n:\n"))

pow = x**n  

if x == 0:
    print("error")

print("x^n:", pow, "\n")