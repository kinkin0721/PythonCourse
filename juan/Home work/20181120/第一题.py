#!/usr/bin/env python
# -*- coding: utf-8 -*-


Input = input('请输入:  ')

for filter_word in open('filtered_words.txt'):
    filters = filter_word.rstrip()
    if filters in Input:
        filters_len = len(filters)
        Input = Input.replace(filters, '*'*filters_len)

else:
    print(Input)
