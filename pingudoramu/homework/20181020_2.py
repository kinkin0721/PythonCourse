# 例子
# def my_range(n):
#     idx = list()
#     count = 0
#     while count < n:
#         idx.append(count)
#         count += 1
#
#     return idx

# 错1
# def my_range(start, end, step):
#     shulie = []
#     count = 0
#     if count <= start:
#     count = start
#     while count < end:
#         shulie.append(count)
#         count += step
#
#     return shulie

# 错2
# def my_range(start, end, step):
#     shulie = []
#     # count = 0
#     # if count <= start:
#     count = start
#     while count < end:
#         shulie.append(count)
#         if step >=0:
#             count += step
#         else:
#             count -= step
#
#     return shulie

def my_range(start, end, step):
    shulie = []
    count = start
    if step >= 0:
        while count < end:
            shulie.append(count)
            count += step
    else:
        while count > end:
            shulie.append(count)
            count += step

    return shulie


if __name__ == "__main__":

    my_range(-3, -13, -3)

    # 测试
    # print(my_range(-3, -13, -3))


