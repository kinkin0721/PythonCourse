

if __name__ == "__main__":

    # 输入文本
    shuRu_str = input("输入:")

    # 倒入敏感词txt
    minGanCi_txt = open('filtered_words.txt')
    minGanCi_str = minGanCi_txt.read()
    minGanCi_txt.close()
    minGanCi_list = minGanCi_str.split()

    # 判断敏感词在文本里吗
    for minganci in minGanCi_list:
        if minganci in shuRu_str:
            # 该敏感词文本长度
            starsNumber = len(minganci)
            # 输出几个*号
            starsWord = '*' * starsNumber
            # 用*号替换敏感词
            shuRu_str = shuRu_str.replace(minganci, starsWord)

    print(shuRu_str)

    # shuRu = input("输入:")
    # shuRuSet = set(shuRu)
    #
    # minGanCiTxt = open('filtered_words.txt')
    # minGanCi = minGanCiTxt.read()
    # # minGanCiStr = str(minGanCi)
    # # print(minGanCiStr)
    # minGanCiSet = set(minGanCi)
    #
    # if shuRuSet & minGanCiSet:
    #     jiaoJi = shuRuSet.intersection(minGanCiSet)
    #     jiaoJiStr = str(jiaoJi)
    #     print(type(jiaoJi))
    #     print(jiaoJiStr)
    #     print(str.replace(jiaoJiStr, "*"))
    #     # print(jiaoJi)
    #     # print(shuRuSet)
    # else:
    #     print(shuRu)

    # shuRu_str = input("输入:")
    # shuRu_list = list(shuRu_str)
    #
    # print(shuRu_list)

    # shuRu_list = ['北京啊\n']
    #
    # minGanCi_txt = open('filtered_words.txt')
    #
    # # minGanCi_str = minGanCi_txt.read()
    # minGanCi_list = minGanCi_txt.readlines()
    #
    #
    # # print(minGanCi_str)
    # print(shuRu_list)
    # print(minGanCi_list)
    #
    # if shuRu_list[0] in minGanCi_list:
    #     print('you')
    # else:
    #     print('wu')

    # 【str法】
    # shuRu_str = input("输入:")
    #
    # print(type(shuRu_str))
    # print(shuRu_str)
    #
    # minGanCi_txt = open('filtered_words.txt')
    # minGanCi_str = minGanCi_txt.read()
    #
    # print(type(minGanCi_str))
    # print(minGanCi_str)
    #
    # if shuRu_str in minGanCi_str:
    #     print('you')
    # else:
    #     print('wu')

    # 输入
    # shuRu_str = input("输入:")

    # print(type(shuRu_str))
    # print(shuRu_str)

    # 读txt
    # minGanCi_txt = open('filtered_words.txt')
    # minGanCi_str = minGanCi_txt.read()
    # minGanCi_list = minGanCi_str.split()
    # minGanCi_str = str(minGanCi_list)
    # print(type(minGanCi_str2))
    # print(minGanCi_str)

    # 判断输入在不在txt里
    # if set(shuRu_str) & set(minGanCi_str):
    #     jiaoJi_set = set(shuRu_str) & set(minGanCi_str)
    #     jiaoji_str = str(jiaoJi_set)
    #     # print(type(jiaoji_str))
    #     shuRu_with_minGanZi = minGanCi_str.__contains__(jiaoji_str)
    #     print(shuRu_with_minGanZi)
    # else:
    #     print('wu')

    # for index in range(len(minGanCi_list)):
    #     if minGanCi_list[index] in shuRu_str:
    #         print(minGanCi_list[index])
    #         shuRu_str = shuRu_str.replace('str(minGanCi_list[index])', '****')
    #
    # print(shuRu_str)

    # if minGanCi_list[0] in shuRu_str:
    #     print('you')
    # print('you'+ str(minGanCi_str.find(shuRu_str)))
    # else:
    #     print('wu')
    # print('wu'+ str(minGanCi_str.find(shuRu_str)))

    # print(minGanCi_str)
    # print(minGanCi_str2)
    # print(minGanCi_list)

    # import re