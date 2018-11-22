#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_han(word):
    for char in word:
        if not '\u4e00' <= char <= '\u9fff':
            return False

    return True


def get_filtered_words(path):
    words = []
    with open(path, 'r') as f:
        for line in f:
            words.append(line.strip())
    return words


if __name__ == "__main__":
    filtered_words = get_filtered_words('filtered_words.txt')
    while True:
        text = input('content: ').strip()
        for word in filtered_words:
            if word not in text:
                continue

            if is_han(word):
                text = text.replace(word, '*' * len(word))
            else:
                text = text.replace(word, '*')

        print(text)

