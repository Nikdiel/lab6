# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

def fibonacci(n):
    if n <= 0:
        return "Некорректный ввод"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

def factorial(n):
    if n < 0:
        return "Некорректный ввод"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    num = int(input("Введите число:\n"))
    print(f"{num}-е число Фибоначчи: {fibonacci(num)}")
    print(f"Факториал {num}: {factorial(num)}")

main()

