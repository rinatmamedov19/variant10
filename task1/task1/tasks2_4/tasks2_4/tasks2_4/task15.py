#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_unique_digits(n):
    return len(set(str(abs(n))))

def main():
    try:
        number = int(input("Введите натуральное число: "))
        if number <= 0:
            print("Ошибка: число должно быть натуральным")
            return
        print(f"Количество различных цифр: {count_unique_digits(number)}")
    except ValueError:
        print("Ошибка: введите целое число")

if __name__ == "__main__":
    main()
