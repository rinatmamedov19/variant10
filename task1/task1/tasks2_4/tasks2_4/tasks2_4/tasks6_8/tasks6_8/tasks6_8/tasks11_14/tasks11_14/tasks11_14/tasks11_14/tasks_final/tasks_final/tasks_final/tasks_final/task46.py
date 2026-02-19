#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def split_positive_negative(arr):
    return [x for x in arr if x > 0] + [x for x in arr if x < 0]

def main():
    try:
        arr = list(map(int, input("Массив: ").split()))
        result = split_positive_negative(arr)
        print(f"Сначала положительные, потом отрицательные: {result}")
    except:
        print("Ошибка ввода")

if __name__ == "__main__":
    main()
