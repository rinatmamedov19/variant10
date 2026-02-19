#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

REF_FREQ = {'e': 0.127, 't': 0.091, 'a': 0.082, 'o': 0.075, 'i': 0.07,
            'n': 0.067, 's': 0.063, 'r': 0.06, 'h': 0.061, 'd': 0.043}

def freq_deviation(s):
    if not s:
        return 0
    letters = [c.lower() for c in s if c.isalpha()]
    if not letters:
        return 0
    counter = Counter(letters)
    most_common, count = counter.most_common(1)[0]
    freq = count / len(letters)
    ref = REF_FREQ.get(most_common, 0.05)
    return (freq - ref) ** 2

def main():
    strings = []
    print("Введите строки (пустая строка - конец):")
    while True:
        s = input()
        if not s and strings:
            break
        if s:
            strings.append(s)
    
    sorted_strings = sorted(strings, key=freq_deviation)
    print("\nОтсортировано по отклонению частоты:")
    for s in sorted_strings:
        print(f"'{s}' - отклонение: {freq_deviation(s):.6f}")

if __name__ == "__main__":
    main()
