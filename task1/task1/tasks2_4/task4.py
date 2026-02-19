#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(s):
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

def main():
    text = input("Введите строку: ")
    if is_palindrome(text):
        print("Строка является палиндромом")
    else:
        print("Строка НЕ является палиндромом")

if __name__ == "__main__":
    main()
