# -*- coding: utf-8 -*-s

def factorization(n):
    cycle = True
    result = str(n) + " = "

    while cycle:
        if n == 1:
            result += str(n)
            break
        for i in range(2, n + 1):
            if i == n:
                cycle = False
                result += str(n)
                break

            if n % i == 0:
                result += str(i) + " * "
                n = int(n / i)
                break

    return result


def is_palindrome_number(n):
    str_n = str(n)
    flag = True

    for i in range(len(str_n) // 2):
        if str_n[i] != str_n[-i - 1]:
            flag = False
            break

    return flag


def fuc1(str):
    letter_count = 0
    space_count = 0
    number_count = 0
    other_count = 0

    for char in str:
        asc_number = ord(char)
        if (65 <= asc_number <= 90) or (97 <= asc_number <= 122):
            letter_count += 1
        elif asc_number == 32:
            space_count += 1
        elif 48 <= asc_number <= 57:
            number_count += 1
        else:
            other_count += 1

    print("有{}个字母，有{}个空格，有{}个数字，有{}个其他字符。"
          .format(letter_count, space_count, number_count, other_count))


def print_multiplication_table():
    # 方法1
    # for i in range(1, 10):
    #     for j in range(1, i + 1):
    #         print("{}*{}={}".format(j, i, i * j), end="\t")
    #     print("")

    # 方法2
    line_str = ""
    for i in range(1, 10):
        for j in range(1, i + 1):
            line_str += "{}*{}={}".format(j, i, i * j) + "\t"

        print(line_str)
        line_str = ""


def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n - 1) + 2
    return c


def get_list_sum():
    a = 2.0
    b = 1.0
    sum = 0
    for i in range(20):
        sum += a / b
        temp = a
        a = a + b
        b = temp

    return sum


def contains_substr(str):
    contains = True
    substr = 'boy'
    for char in substr:
        if char not in str:
            contains = False
            break

    return contains


if __name__ == "__main__":
    print("Hello world!")

    n = int(input("请输入数字："))
    print(factorization(n))

    # n = int(input("请输入数字："))
    # if is_palindrome_number(n):
    #     print(str(n) + "是一个回文数!")
    # else:
    #     print(str(n) + "不是一个回文数!")

    # s = input("请输入：")
    # fuc1(s)

    # print_multiplication_table()

    # n = int(input("请输入数字："))
    # age(n)

    # print(get_list_sum())
