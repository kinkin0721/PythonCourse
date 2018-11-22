# -*- coding: utf-8 -*-
if __name__ == "__main__":
    print("hello world")

# # 斐波那契数列输出前N项
#     def fibo(num):
#         if num == 0:
#             numlist = [0]
#             return numlist
#         else:
#             numList = [0, 1]
#             for i in range(num - 2):
#                 numList.append(numList[-2] + numList[-1])
#             return numList
#
#
#     print(fibo(9))


# # 猜数字游戏
#     secret_num = "5555"
#     guess = input("Enter the answer:")
#     guess_num = int(guess)
#     while guess != secret_num:
#         if 9999 >= guess_num >= 1000:
#             guess = input("Enter the answer: ")
#         else:
#             print("Out of range ")
#             break
#     else:
#         print("You win!")


def frange(start, stop=None, step=1):
    result = []
    if stop == None:
        stop = start
        start = 0.0
    if step >= 1:
        while start < stop:
            result.append(float(start))
            start += step
    elif step <= -1:
        while start > stop:
            result.append(float(start))
            start += step
    return result

























