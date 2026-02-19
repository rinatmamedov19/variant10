#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def smallest_divisor(n):
    if n < 2:
        return n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def max_not_coprime_not_divisible_by_min_divisor(n):
    min_div = smallest_divisor(n)
    for i in range(n, 1, -1):
        if gcd(i, n) != 1 and i % min_div != 0:
            return i
    return 0

def sum_digits_less_than_5(n):
    digits = [int(d) for d in str(abs(n))]
    return sum(d for d in digits if d < 5)

def main():
    try:
        number = int(input("Введите натуральное число: "))
        if number <= 0:
            print("Ошибка: число должно быть натуральным")
            return
        max_num = max_not_coprime_not_divisible_by_min_divisor(number)
        sum_digits = sum_digits_less_than_5(number)
        if max_num == 0:
            print("Не найдено подходящее число")
        else:
            product = max_num * sum_digits
            print(f"Максимальное подходящее число: {max_num}")
            print(f"Сумма цифр < 5: {sum_digits}")
            print(f"Произведение: {product}")
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()
