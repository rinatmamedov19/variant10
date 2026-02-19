#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def max_digit_not_divisible_by_3(n):
    digits = [int(d) for d in str(abs(n))]
    valid_digits = [d for d in digits if d % 3 != 0]
    return max(valid_digits) if valid_digits else -1

def main():
    try:
        number = int(input("Введите число: "))
        result = max_digit_not_divisible_by_3(number)
        if result == -1:
            print("В числе нет цифр, не делящихся на 3")
        else:
            print(f"Максимальная цифра, не делящаяся на 3: {result}")
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()
