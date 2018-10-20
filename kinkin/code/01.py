# -*- coding: utf-8 -*-


def sqr(n):
    return n * n


def lis_range(n):
    l = list()
    for i in range(5):
        l.append(i+1)

    return l


def fibonacci(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        n1 = 0
        n2 = 1
        count = 1
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        print(nth)


def find2(n):

    if n < 0:
        print("请输入正整数")

    a = [9, 0, 8, 0, 8, 2, 7, 6, 2, 1, 2, 2, 10, 39]

    count = 0
    count_for_2 = 0
    for num in a:
        if num == 2:
            count_for_2 += 1
            if count_for_2 == n:
                break
        count += 1

    if count_for_2 < n:
        print("meiyounameduo2 godie")
    else:
        print(count)


if __name__ == "__main__":
    print("Hello world!")

    # count = 4
    # count = 999
    #
    # if count == 4:
    #     print("chenggong")
    # else:
    #     print("shibai")
    #
    # if count != 4:
    #     print("chenggong")
    # else:
    #     print("shibai")
    #
    # isMonday = True
    # isSunday = False

    # [ismonday, is]
    # today = [True, False, False, False, False, False, False]
    #
    # for index in range(100):
    #     print(today[index])
    #
    # count = 0
    # for day in today:
    #     print(count)
    #     count = count + 1
    #     count += 1

    # countsum = 0
    # for idx in range(-1, 101):
    #     sum = (sum + idx) / 2
    #
    # print(sum)

    # count = 0
    # while count >= 0:
    #     count = count + 1
    #     print(count)

    # numList = [2, 3, 4, 5, 7, 9, 10, 100]
    #
    # # find2(90)
    #
    # fibonacci(8)
    #
    # d = {'apple': 3, 'banana': 10, 'pineapple': 7}
    #
    # print(numList)

    # for i in range(5):
    #     if i == 3:
    #         break
    #     print(i)

    # for i in range(5):
    #     if i == 3:
    #         continue
    #     print(i)

    print(sqr(2))











