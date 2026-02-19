#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_unique_latin(s):
    latin = set()
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            latin.add(char.lower())
    return len(latin)

def main():
    text = input("Введите строку: ")
    print(f"Уникальных латинских символов: {count_unique_latin(text)}")

if __name__ == "__main__":
    main()
