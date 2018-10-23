
def caishuzi(jie):
    # 随机生成无重复数字4位
    import random

    daan_chongfu = []
    daan_wuchongfu = []
    for daan_shuzi in range(100):
        if len(daan_wuchongfu) < 4:
            daan_chongfu.append(random.randint(0, 9))
            daan_wuchongfu = list(set(daan_chongfu))

    print(daan_wuchongfu)

    # 位置对，的数的个数
    correct_weizhi = 0
    for index in range(len(jie)):
        if jie[index] == daan_wuchongfu[index]:
            correct_weizhi += 1

    # 数字对，位置不对，的数的个数
    correct_shuzi = 0
    for jie_shuzi in jie:
        if jie_shuzi in daan_wuchongfu:
            correct_shuzi += 1

    print(str(correct_weizhi)+"A"+str(correct_shuzi)+"B")


if __name__ == "__main__":

    caishuzi([5, 6, 7, 8])



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