# def jiecheng(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jiecheng(n - 1)
#
#
# n = input("number: ")
# print(jiecheng(int(n)))


# def cal():
#     l = [2, 5, 6, 7, 8, 9, 2, 9, 9]
#     zuidazhi = l[0]
#     zuixiaozhi = l[0]
#     he = 0
#     for num in l:
#         if num > zuidazhi:
#             zuidazhi = num
#         if num < zuixiaozhi:
#             zuixiaozhi = num
#         he = he + num
#     return zuidazhi, zuixiaozhi, he / len(l)
#
#
# print(cal())


# def sanweishu():
#     arr = [1, 2, 3, 4]
#     jieguo = []
#     for diyiwei in arr:
#         for dierwei in arr:
#             for disanwei in arr:
#                 if diyiwei == dierwei or dierwei == disanwei or diyiwei == disanwei:
#                     continue
#                 jieguo.append(100 * diyiwei + 10 * dierwei + disanwei)
#     return jieguo
#
#
# print(sanweishu())


# def sanweishu():
#     arr = [1, 2, 3, 4]
#     jieguo = []
#     for diyiwei in arr:
#         for dierwei in arr:
#             if diyiwei == dierwei:
#                 continue
#             for disanwei in arr:
#                 if dierwei == disanwei or diyiwei == disanwei:
#                     continue
#                 jieguo.append(100 * diyiwei + 10 * dierwei + disanwei)
#     return jieguo
#
#
# print(sanweishu())


# def frk():
#     tongji = dict()
#     zifuchuan = input("qingshuru:")
#     for zimu in zifuchuan:
#         if zimu not in tongji:
#             tongji[zimu] = 1
#         else:
#             tongji[zimu] = tongji[zimu] +1
#     zuidapinlv = "0"
#     for zimu in tongji:
#         if zuidapinlv not in tongji:
#             zuidapinlv = zimu
#             continue
#         if tongji[zimu] > tongji[zuidapinlv]:
#             zuidapinlv = zimu
#     return zuidapinlv
#
#
# print(frk())


l = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 4, 4, 6, 6, 8, 8, 12, 12, 13]
def quchu():
    newl = []
    for idx in range(len(l)):
        if l[idx] != l[idx - 1]:
           newl.append(l[idx])
        else:
            continue
    return newl

print(quchu())