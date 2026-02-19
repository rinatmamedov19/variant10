#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def max_consecutive_digits(s):
    max_len = cur = 0
    for char in s:
        if char.isdigit():
            cur += 1
            max_len = max(max_len, cur)
        else:
            cur = 0
    return max_len

def main():
    text = input("Введите строку: ")
    print(f"Максимально подряд цифр: {max_consecutive_digits(text)}")

if __name__ == "__main__":
    main()
