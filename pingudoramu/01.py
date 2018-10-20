# 📕函数-闰年
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year) + "是闰年")
#     else:
#         print(str(year) + "不是闰年")

# return
# def sqr(n):
#     return n * n

# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return True

# 📕函数-斐波那契数列
# 从第3项开始,每一项都等于前两项之和
# def fibonacci(th):
#     if th == 0:
#         print(0)
#     elif th == 1:
#         print(1)
#     else:
#         n1 = 0
#         n2 = 1
#         count = 1
#         nall = 1
#         while count < th:
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             count = count + 1
#             nall = nth + nall
#         print(nall)


if __name__ == "__main__":

    # fibonacci(8)

    # 📕打hello word
    # print("hello word!")
    #
    # 📕注意顺序和覆盖
    # count = 4
    # count = 222
    # if count == 4:
    #     print("success")
    # else:
    #     print("failed")
    #
    # if count != 4:
    #     print("success")
    # else:
    #     print("failed")
    #
    # print(count)
    #
    # 📕周末和布尔值
    # isMonday = True
    # isSunday = False
    # isTuesday = False
    # isWendsay = False
    # isTuesday = False
    # isFriday = False
    # isSaturday = False
    #
    # if isSaturday or isSunday:
    #     print("xiuxi")
    # else:
    #     print("shangban")
    #
    # if isSaturday or isSunday:
    #     print("xiuxi")
    # elif isMonday:
    #     print("di1tian")
    # elif isTuesday:
    #     print("di2tian")
    # elif isWendsay:
    #     print("di3tian")
    # elif isTuesday:
    #     print("di4tian")
    # else:
    #     print("di5tian")
    #
    # 📕数组，取出数组
    # today = [True, False, False, False, False, False, False]
    # if today[5] or today[6]:
    #     print("xiuxi")
    # elif today[0]:
    #     print("di1tian")
    # elif today[1]:
    #     print("di2tian")
    # else:
    #     print("qita")
    #
    # 📕index与for索引循环
    # today = [True, False, False, False, False, False, False]
    # for index in range(len(today)):
    #     today = index + 1
    #     print(today)
    # print("wancheng")
    #
    # 📕index，for索引循环
    # today = [True, False, False, False, False, False, False]
    # for aaa in range(len(today)):
    #     suibian = aaa + 1
    #     if today[aaa]:
    #         print(str(suibian)+"：yes")
    #     else:
    #         print(str(suibian)+"：no")
    # 📕for内容循环，自己做索引
    # today = [True, False, False, False, False, False, False]
    # suibian = 0
    # for aaa in today:
    #     suibian = suibian + 1
    #     if aaa:
    #         print(str(suibian)+"：yes")
    #     else:
    #         print(str(suibian)+"：no")
    #
    # 📕for内容循环自己做索引
    # today = [False, False, True, False, False, False, False]
    # count = 0
    # for day in today:
    #     count = count + 1
    #     print(count)
    #
    # 📕转str，print两个拼起来
    # today = [False, False, True, False, False, False, False]
    # for index in range(len(today)):
    #     suibian = index + 1
    #     if today[index]:
    #         print(str(suibian)+"：yes")
    #     else:
    #         print(str(suibian)+"：no")
    # print("wancheng")
    #
    # 📕如果today里的内容不是布尔值
    # today = ["Monday", "Tuesday", "Wendsay", "Tuesday", "Friday", "Saturday", "Sunday"]
    #
    # count = 0
    # for day in today:
    #     count = count + 1
    #     if day == "Monday" :
    #         print(str(count)+":yes")
    #     else:
    #         print(str(count)+":no")
    #
    # 📕
    # count = -1
    # for count in range(2):
    #     count = count
    #     print(count)
    #
    # 📕从-1加到99
    # shuzi = 0
    # for index in range(-1, 100):
    #     shuzi = index + shuzi
    #
    # print(shuzi)

    # 📕for循环的break
    # shuzi = 0
    # for index in range(100):
    #     shuzi = index * index
    #     if shuzi > 100 :
    #         print(index)
    #         break
    # print(shuzi)

    # 📗为什么要加"shuzi = 0"？不加得出的结果是一样的
    # for index in range(100):
    #     shuzi = index * index
    #     if shuzi > 100 :
    #         print(index)
    #         break
    # print(shuzi)

    # ～～～～～～～～～～～～～～～～～～～～2018年10月13日～～～～～～～～～～～～～～～～～～～～

    # 📕while循环
    # count = 0
    # while count >=0:
    #     count = count + 1
    #     print(count)

    # count = 5/2
    # print(count)
    #
    # count = 6 % 2
    # print(count)

    # 📕not in 和 in
    # numlist = [2, 3, 4, 5, 6, 9, 10, 100]
    # if 8 in numlist:
    #     print("8 zai limian")
    # else:
    #     print("bu zai limian")

    # 📕输出a中2的个数
    # a = [9, 0, 8, 0, 8, 2, 7, 6, 2, 1, 2, 2, 10, 39]
    # count = 0
    # for shuzi in a:
    #     if shuzi == 2:
    #         count = count + 1
    # print(count)
    #
    # 📕输出a中第一个2的索引值
    # a = [9, 0, 8, 0, 8, 2, 7, 6, 2, 1, 2, 2, 10, 39]
    # count = 0
    # for shuzi in a:
    #     if shuzi == 2:
    #         print(count)
    #         break
    #     else:
    #         count = count + 1
    #
    # 📕输出a中第三个2的索引值
    # a = [9, 0, 8, 0, 8, 2, 7, 6, 2, 1, 2, 2, 10, 39]
    # acount = 0
    # count = 0
    # for shuzi in a:
    #     if shuzi == 2:
    #         acount = acount + 1
    #         if acount == 3:
    #             print(count)
    #             break
    #     count = count + 1

    # 📕闰年否
    # is_leap_year(1992)

    # 📕斐波那契数列
    # fibonacci(4)

    # ～～～～～～～～～～～～～～～～～～～～2018年10月20日～～～～～～～～～～～～～～～～～～～～

    # continue
    # for i in range(5):
    #     if i ==3:
    #         break
    #     print(i)

    # for i in range(5):
    #     if i == 3;
    #         continue
    #     print(i)

    # 返回值 sqr是平方
    # def sqr(n):
    #     return n * n

    # a = [1, 1, 3, 1, 8, 5]
    # for shuzi in a:
    #     if 1 in a:
    #         a.remove(1)
    #
    # print(a)

    # a = [1, 1, 3, 1, 8, 5]
    # while 1 in a:
    #     a.remove(1)
    #
    # print(a)

    # a = []
    # a.append(1)
    # a.append(2)
    # a.append(3)
    # a.append(4)
    # a.append(5)
    # print(a)

    a = []

    for i in range(5):
        a.append(i + 1)
    print(a)

    def my_range(n):
        idx = list()
        count = 0
        while count < n:
            idx.append(count)
            count += 2

        return idx

