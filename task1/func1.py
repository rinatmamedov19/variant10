#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_even_not_coprime(n):
    if n < 2:
        return 0
    count = 0
    for i in range(2, n + 1):
        if i % 2 == 0 and gcd(i, n) != 1:
            count += 1
    return count

def main():
    try:
        number = int(input("Введите натуральное число: "))
        if number <= 0:
            print("Ошибка: число должно быть натуральным")
            return
        result = count_even_not_coprime(number)
        print(f"Количество четных чисел, не взаимно простых с {number}: {result}")
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()
