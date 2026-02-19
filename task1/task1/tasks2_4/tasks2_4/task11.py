#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_words(s):
    return len(s.split())

def main():
    text = input("Введите строку: ")
    print(f"Количество слов: {count_words(text)}")

if __name__ == "__main__":
    main()
