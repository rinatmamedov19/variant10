#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mirror_triplets_avg(s):
    if len(s) < 3:
        return 0
    count = 0
    for i in range(len(s)-2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            count += 1
    return count / len(s)

def main():
    strings = []
    print("Введите строки (пустая строка - конец):")
    while True:
        s = input()
        if not s and strings:
            break
        if s:
            strings.append(s)
    
    sorted_strings = sorted(strings, key=mirror_triplets_avg)
    print("\nОтсортировано по среднему количеству зеркальных троек:")
    for s in sorted_strings:
        print(f"'{s}' - среднее: {mirror_triplets_avg(s):.3f}")

if __name__ == "__main__":
    main()
