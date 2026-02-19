#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_elements_as_sum(arr):
    if len(arr) < 3:
        return 0
    sums = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sums.add(arr[i] + arr[j])
    return sum(1 for x in arr if x in sums)

def main():
    try:
        arr = list(map(int, input("Массив: ").split()))
        print(f"Элементов, которые можно получить как сумму двух других: {count_elements_as_sum(arr)}")
    except:
        print("Ошибка ввода")

if __name__ == "__main__":
    main()
