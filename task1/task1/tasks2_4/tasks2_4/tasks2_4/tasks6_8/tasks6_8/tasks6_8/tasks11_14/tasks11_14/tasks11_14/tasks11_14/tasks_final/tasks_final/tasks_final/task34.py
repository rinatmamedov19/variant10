#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def elements_in_range(arr, a, b):
    return [x for x in arr if a <= x <= b]

def main():
    try:
        arr = list(map(int, input("Массив: ").split()))
        a = int(input("a: "))
        b = int(input("b: "))
        result = elements_in_range(arr, a, b)
        print(f"Элементы в [{a},{b}]: {result}")
    except:
        print("Ошибка ввода")

if __name__ == "__main__":
    main()
