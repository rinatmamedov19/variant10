#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mirror_criterion(s):
    if not s:
        return 0
    max_ascii = max(ord(c) for c in s)
    if len(s) < 2:
        return max_ascii ** 2
    mid = len(s) // 2
    if len(s) % 2 == 0:
        mirror_diff = abs(ord(s[mid-1]) - ord(s[mid]))
    else:
        mirror_diff = abs(ord(s[mid-1]) - ord(s[mid+1])) if len(s) > 2 else 0
    return (max_ascii - mirror_diff) ** 2

def main():
    strings = []
    print("Введите строки (пустая строка - конец):")
    while True:
        s = input()
        if not s and strings:
            break
        if s:
            strings.append(s)
    
    sorted_strings = sorted(strings, key=mirror_criterion)
    print("\nОтсортировано по зеркальному критерию:")
    for s in sorted_strings:
        print(f"'{s}' - значение: {mirror_criterion(s)}")

if __name__ == "__main__":
    main()
