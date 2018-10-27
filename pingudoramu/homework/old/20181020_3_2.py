
def list_zhuan_str(list_old):
    str = ''
    list = list_old
    n = 0
    while n < len(list):
        str += str(list[n])
        n += 1
    return str
#
# def caishuzi(jie):
#
#     # 随机生成无重复数字4位答案
#     import random
#     daan_chongfu = []
#     daan_wuchongfu = []
#     for daan_shuzi in range(100):
#         if len(daan_wuchongfu) < 4:
#             daan_chongfu.append(random.randint(0, 9))
#             daan_wuchongfu = list(set(daan_chongfu))
#
#     # list转str
#     daan_wuchongfu_str = ''
#     daan_wuchongfu_list = daan_wuchongfu
#     n = 0
#     while n < len(daan_wuchongfu_list):
#         daan_wuchongfu_str += str(daan_wuchongfu_list[n])
#         n += 1
#     print(daan_wuchongfu_str)
#
#     # 猜
#     caijici = input("输入猜几次")
#     print("猜数字小游戏开始啦!答案为一个没有重复数字4位数")
#     # jie = input("输入数字")
#
#     # 判断合法性
#     for index in range(int(caijici)):
#         jie = input("输入数字")
#         if jie.isalpha():
#             print("请输入，四位，无重复，正整数")
#         else:
#             if 999 < int(jie) < 9999:
#                 print("good1")
#                 break
#             else:
#                 print("请输入，四位，无重复，正整数")
#
#     # 合法后
#     for index in range(len(int(caijici))):
#         if jie != daan_wuchongfu_str:
#             # 位置对，的数的个数
#             correct_weizhi = 0
#             for index in range(len(jie)):
#                 if int(jie)[index] == daan_wuchongfu_str[index]:
#                     correct_weizhi += 1
#
#             # 数字对，位置不对，的数的个数
#             correct_shuzi = 0
#             for jie_shuzi in jie:
#                 if jie_shuzi in daan_wuchongfu_str:
#                     correct_shuzi += 1
#
#             print(str(correct_weizhi) + "A" + str(correct_shuzi) + "B")
#             jie = input("输入数字")
#     print("答对啦")

if __name__ == "__main__":

    # 可取范围
    fanwei = []
    n = 1
    for index in range(10):
        if n < 10:
            fanwei.append(n)
            n += 1
    # 转str
    fanwei_str = ''
    list = fanwei
    n = 0
    while n < len(list):
        fanwei_str += fanwei_str(list[n])
        n += 1

    print(fanwei_str)


    # caishuzi(input("输入猜几次"))
    # jie = input("输入数字")
    # if jie % 1 == int:
    #     print("a")
    # else:
    #     print("b")

    # jie = input("输入数字")
    # jie_float = float(jie)
    # print(jie_float)
    # jie_chushu = jie_float // 10
    # print(jie_chushu)

    # jie = input("输入数字")



    # jie = input("输入数字")
    # if jie < str(999):
    #     print("xiao yu 999")
    # else:
    #     print("qi ta")

    # 随机生成无重复数字4位答案
    # import random
    # daan_chongfu = []
    # daan_wuchongfu = []
    # for daan_shuzi in range(100):
    #     if len(daan_wuchongfu) < 4:
    #         daan_chongfu.append(random.randint(0, 9))
    #         daan_wuchongfu = list(set(daan_chongfu))
    #
    # # 答案的list转str
    # daan_wuchongfu_str = ''
    # daan_wuchongfu_list = daan_wuchongfu
    # n = 0
    # while n < len(daan_wuchongfu_list):
    #     daan_wuchongfu_str += str(daan_wuchongfu_list[n])
    #     n += 1
    # print(daan_wuchongfu_str)
    #
    # # 猜
    # caijici = input("输入猜几次")
    # print("猜数字小游戏开始啦!答案为一个没有重复数字4位数")
    # # jie = input("输入数字")
    #
    # # 判断合法性
    #
    # # 可取范围
    # fanwei = []
    # n = 1
    # for index in range(10):
    #     if n < 10:
    #         fanwei.append(n)
    #         n += 1
    #
    #
    #
    # for index in range(int(caijici)):
    #     jie = input("输入数字")
    #     if jie in fanwei:
    #         print("good")
    #     else:
    #         print("请输入，四位，无重复，正整数")
    #
    # # 合法后
    # for index in range(len(int(caijici))):
    #     if jie != daan_wuchongfu_str:
    #         # 位置对，的数的个数
    #         correct_weizhi = 0
    #         for index in range(len(jie)):
    #             if int(jie)[index] == daan_wuchongfu_str[index]:
    #                 correct_weizhi += 1
    #
    #         # 数字对，位置不对，的数的个数
    #         correct_shuzi = 0
    #         for jie_shuzi in jie:
    #             if jie_shuzi in daan_wuchongfu_str:
    #                 correct_shuzi += 1
    #
    #         print(str(correct_weizhi) + "A" + str(correct_shuzi) + "B")
    #         jie = input("输入数字")
    # print("答对啦")

    # caijici = input("输入猜几次")
    # print("猜数字小游戏开始啦!答案为一个没有重复数字4位数")


    # caijici = input("输入猜几次")
    #
    # # 判断合法性
    # for index in range(len(caijici)):
    #     jie = input("输入数字")
    #     if jie.isalpha():
    #         print("请输入，四位，无重复，正整数")
    #     else:
    #         if 999 < int(jie) < 9999:
    #             print("good1")
    #             break
    #         else:
    #             print("请输入，四位，无重复，正整数")





    # while isinstance(jie, int):
    #     if 999 < jie < 9999:
    #         print("good")
    #         break
    #     else:
    #         print("请输入，四位，无重复，正整数1")
    #     print("请输入，四位，无重复，正整数2")

# ====================================

    # 判断合法性

    # 可取范围
    # zhengchang = []
    # n = 1
    # for index in range(10):
    #     if n < 10:
    #         zhengchang.append(n)
    #         n += 1
    # for index in range(int(caijici)):
    #     jie = input("输入数字")
    #     if jie.isalpha():
    #         print("不能字母")
    #     else:
    #         if isinstance(jie, float):
    #             print("必须4位正整数1")
    #         else:
    #             if jie < str(999):
    #                 print("必须4位正整数2")
    #             elif jie > str(9999):
    #                 print("必须4位正整数3")
    #             else:

# lise转str
# s = ''
# l = [9, 7, 8, 7]
# n = 0
# while n < len(l):
#     s += str(l[n])
#     n += 1
# print(s)

# 难度1
# def caishuzi(jie):
#     daan = [1, 4, 8, 3]
#
#     # 位置对，的数的个数
#     correct_weizhi = 0
#     for index in range(len(jie)):
#         if jie[index] == daan[index]:
#             correct_weizhi += 1
#
#     # 数字对，位置不对，的数的个数
#     correct_shuzi = 0
#     for shuzi in jie:
#         if shuzi in daan:
#             correct_shuzi += 1
#
#     print(str(correct_weizhi)+"A"+str(correct_shuzi)+"B")

# 难度2 while 替代 for
# def caishuzi(jie):
#
#     # 随机生成无重复数字4位
#     import random
#     daan_chongfu = []
#     daan_wuchongfu = []
#     for daan_shuzi in range(100):
#         if len(daan_wuchongfu) < 4:
#             daan_chongfu.append(random.randint(0, 9))
#             daan_wuchongfu = list(set(daan_chongfu))
#
#     # list转str
#     daan_wuchongfu_str = ''
#     daan_wuchongfu_list = daan_wuchongfu
#     n = 0
#     while n < len(daan_wuchongfu_list):
#         daan_wuchongfu_str += str(daan_wuchongfu_list[n])
#         n += 1
#
#     print(daan_wuchongfu_str)
# for index in range(100):
#     jie = input("输入数字")
#
#     if jie != daan_wuchongfu_str:
#         # 位置对，的数的个数
#         correct_weizhi = 0
#         for index in range(len(jie)):
#             if jie[index] == daan_wuchongfu_str[index]:
#                 correct_weizhi += 1
#
#         # 数字对，位置不对，的数的个数
#         correct_shuzi = 0
#         for jie_shuzi in jie:
#             if jie_shuzi in daan_wuchongfu_str:
#                 correct_shuzi += 1
#
#         print(str(correct_weizhi) + "A" + str(correct_shuzi) + "B")
#     else:
#         print("daduila")

# 难度2 while
# def caishuzi(jie):
#
#     # 随机生成无重复数字4位答案
#     import random
#     daan_chongfu = []
#     daan_wuchongfu = []
#     for daan_shuzi in range(100):
#         if len(daan_wuchongfu) < 4:
#             daan_chongfu.append(random.randint(0, 9))
#             daan_wuchongfu = list(set(daan_chongfu))
#
#     # 答案的list转str
#     daan_wuchongfu_str = ''
#     daan_wuchongfu_list = daan_wuchongfu
#     n = 0
#     while n < len(daan_wuchongfu_list):
#         daan_wuchongfu_str += str(daan_wuchongfu_list[n])
#         n += 1
#     print(daan_wuchongfu_str)
#
#     # 猜
#     jie = input("输入数字")
#
#     # 判断合法性
#     # 四位、无重复、正整数、1到9
#     if jie
#
#     # 合法后
#     while jie != daan_wuchongfu_str:
#          # 位置对，的数的个数
#         correct_weizhi = 0
#         for index in range(len(jie)):
#             if jie[index] == daan_wuchongfu_str[index]:
#                 correct_weizhi += 1
#
#         # 数字对，位置不对，的数的个数
#         correct_shuzi = 0
#         for jie_shuzi in jie:
#             if jie_shuzi in daan_wuchongfu_str:
#                 correct_shuzi += 1
#
#         print(str(correct_weizhi) + "A" + str(correct_shuzi) + "B")
#         jie = input("输入数字")
#
#     print("daduila")