# -*- coding: utf-8 -*-s

def exer1():
    n = 1
    h = 100
    s = 100
    while n <= 10:
        h = h / 2
        s += h * 2
        n = n + 1
    print("小球共经过: " + str(s) + "米")
    print("小球反弹高度: " + str(h) + "米")


def exer2():
    n = 1
    a = 1
    sum = 0
    while n <= 20:
        a *= n
        sum += a
        n = n + 1
    print(sum)


def exer3(n):
    count = 0
    reverse_str = ""
    while n != 0:
        reverse_str += str(n % 10)
        n = n // 10
        count += 1
    print("位数：" + str(count))
    print("反向输出：" + reverse_str)


if __name__ == "__main__":
    print("Hello world!")

    # exer1()

    # exer2()

    # n = int(input("请输入一个正整数："))
    # exer3(n)
