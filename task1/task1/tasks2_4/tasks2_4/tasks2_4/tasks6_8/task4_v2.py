#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def count_numbers_less_than_5(s):
    numbers = re.findall(r'\d+', s)
    return sum(1 for num in numbers if int(num) < 5)

def main():
    text = input("Введите строку с числами: ")
    print(f"Количество чисел меньше 5: {count_numbers_less_than_5(text)}")

if __name__ == "__main__":
    main()
