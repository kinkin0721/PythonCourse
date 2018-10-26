#!/usr/bin/env python
# -*- coding: utf-8 -*-


def my_range(n):
    idxs = list()
    count = 0
    while count < n:
        idxs.append(count)
        count += 1

    return idxs


def fibonacci(n):
    if n <= 0:
        print("请输入一个正整数！")
        return []

    f = [1]
    n1 = 0
    n2 = 1
    count = 1
    while count < n:
        nth = n1 + n2
        f.append(nth)
        n1 = n2
        n2 = nth
        count += 1

    return f


def my_range(start, end, step):
    idxs = list()
    idx = start
    while (step > 0 and idx < end)\
            or (step < 0 and idx > end):
        idxs.append(idx)
        idx += step

    return idxs


if __name__ == "__main__":
    pass
    # print(my_range(1, 8, 2))
    # [1,3,5,7]
    # print(fibonacci(8))
    # [1, 1, 2, 3, 5, 8, 13, 21]

