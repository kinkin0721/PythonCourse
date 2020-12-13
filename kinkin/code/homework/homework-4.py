# -*- coding: utf-8 -*-s

def sort(l):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l


def sort2(l):
    for i in range(1, len(l)):
        value = l[i]
        j = i - 1
        while j >= 0:
            if l[j] > value:
                l[j + 1] = l[j]
                l[j] = value
                j -= 1
            else:
                break

    return l


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


def max_in_list(l):
    max = float("-inf")
    for num in l:
        if num > max:
            max = num

    return max


def min_in_list(l):
    min = float("inf")
    for num in l:
        if num < min:
            min = num

    return min


def average(l):
    sum = 0
    for num in l:
        sum += num

    return sum / len(l)


def exercise4():
    list1 = [1, 2, 3, 4]
    result = []
    for x in list1:
        for y in list1:
            if y == x:
                continue

            for z in list1:
                if x != z and y != z:
                    a = x * 100 + y * 10 + z
                    result.append(a)

    print(result)
    print(len(result))


def exercise5(s):
    d = dict()
    max_count = 0
    max_char = ''
    for char in s:
        count = 1
        if char in d.keys():
            d[char] += 1
            count = d[char]
        else:
            d[char] = 1

        if count > max_count:
            max_count = count
            max_char = char

    return max_char


def exercise6(l):
    new_list = [l[0]]
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            new_list.append(l[i])
    return new_list


if __name__ == "__main__":
    print("Hello world!")

    a = [1, 7, 4, 89, 34, 2, 100, 0]
    # print(sort(a))
    print(sort2(a))

    # print(factorial(4))

    # L = [2, 5, 6, 7, 8, 9, 2, 9, 9]
    # max_in_list(L)
    # min_in_list(L)
    # average(L)

    # exercise4()

    # s = input("请输入：")
    # exercise5(s)

    # L = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 4, 4, 6, 6, 8, 8, 12, 12, 8, 12, 12, 13]
    # print(exercise6(L))