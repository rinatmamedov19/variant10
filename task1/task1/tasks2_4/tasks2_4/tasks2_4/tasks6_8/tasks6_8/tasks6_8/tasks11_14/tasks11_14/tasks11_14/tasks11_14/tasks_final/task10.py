#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def common_elements(arr1, arr2):
    return len(set(arr1) & set(arr2))

def main():
    try:
        arr1 = list(map(int, input("Первый массив: ").split()))
        arr2 = list(map(int, input("Второй массив: ").split()))
        print(f"Совпадающих элементов: {common_elements(arr1, arr2)}")
    except:
        print("Ошибка ввода")

if __name__ == "__main__":
    main()
