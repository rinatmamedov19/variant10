#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_min_in_interval(arr, a, b):
    if a < 0 or b >= len(arr) or a > b:
        return 0
    sub = arr[a:b+1]
    if not sub:
        return 0
    min_val = min(sub)
    return sub.count(min_val)

def main():
    try:
        arr = list(map(int, input("Массив: ").split()))
        a = int(input("a: "))
        b = int(input("b: "))
        print(f"Минимальных в [{a},{b}]: {count_min_in_interval(arr, a, b)}")
    except:
        print("Ошибка ввода")

if __name__ == "__main__":
    main()
