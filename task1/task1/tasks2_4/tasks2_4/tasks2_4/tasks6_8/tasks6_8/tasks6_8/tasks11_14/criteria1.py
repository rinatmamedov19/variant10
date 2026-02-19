#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def vowel_consonant_diff(s):
    vowels = set('aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ')
    v = sum(1 for c in s if c.isalpha() and c in vowels)
    c = sum(1 for c in s if c.isalpha() and c not in vowels)
    return abs(c - v)

def main():
    strings = []
    print("Введите строки (пустая строка - конец):")
    while True:
        s = input()
        if not s and strings:
            break
        if s:
            strings.append(s)
    
    if not strings:
        print("Нет строк")
        return
    
    sorted_strings = sorted(strings, key=vowel_consonant_diff)
    print("\nОтсортировано по разнице согласные-гласные:")
    for s in sorted_strings:
        print(f"'{s}' - разница: {vowel_consonant_diff(s)}")

if __name__ == "__main__":
    main()
