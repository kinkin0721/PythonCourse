# -*- coding: utf-8 -*-s

import math


def fuc1(a, n):
    # 方法1：
    # i = 0
    # sum = 0
    # while n > 0:
    #     sum = sum + a * 10 ** i * n
    #     n = n - 1
    #     i = i + 1

    # 方法2：
    sum = 0
    while n > 0:
        m = n - 1
        b = 0
        while m >= 0:
            b = b + a * 10 ** m
            m = m - 1
        n = n - 1
        sum = sum + b
        print("b = " + str(b))

    print("sum = " + str(sum))


def fibonacci(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        n1 = 0
        n2 = 1
        sum = n1 + n2
        count = 1
        while count < n:
            nth = n1 + n2
            sum += nth
            n1 = n2
            n2 = nth
            count += 1
        print(sum)


def narcissistic_number():
    n = 100
    # end = 1000
    while n < 1000:
        i = n // 100
        j = n // 10 % 10
        k = n % 10
        if n == i ** 3 + j ** 3 + k ** 3:
            print(n)
        n += 1


def day_of_year(year, month, day):
    bleap = False
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        bleap = True

    if month > 12 or month < 1:
        print("input month error")
        return
    else:
        sum = 31 * month
        if month >= 2:
            if bleap:
                sum -= 2
            else:
                sum -= 3

            if month <= 7:
                sum -= month // 2 - 1
            else:
                sum -= 7 // 2 - 1
                sum -= (month - 7) // 2

        sum += day
        print(sum)


def is_prime_number(n):
    if n == 1:
        print("是质数")
    else:
        bprime = True
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                print(i)
                bprime = False
                break
            i += 1
        if bprime:
            print("是质数")
        else:
            print("不是质数")


def fuc2(n):
    if n % 2 == 0:
        print("请输入奇数！")
    else:
        sum = 9
        m9 = 9
        i = 1
        while True:
            if sum % n == 0:
                print(sum/n)
                break
            else:
                m9 *= 10
                sum += m9
                i += 1
        print(i)


if __name__ == "__main__":
    print("Hello world!")

    # a = int(input("请输入一个数值："))
    # n = int(input("请输入次数："))
    # fuc1(a, n)

    # n = int(input("请输入数字："))
    # fibonacci(n)

    # narcissistic_number()

    # year = int(input('year:'))
    # month = int(input('month:'))
    # day = int(input('day:'))
    # day_of_year(year, month, day)

    # n = int(input("请输入数字："))
    # is_prime_number(n)

    # n = int(input("请输入奇数："))
    # fuc2(n)
