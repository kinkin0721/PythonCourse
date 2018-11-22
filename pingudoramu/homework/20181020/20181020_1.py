
def fibonacci(th):

    shulie = []
    if th == 0:
        print("不可以0")
    elif th == 1:
        shulie.append(0)
        return shulie
    else:
        shulie.append(0)
        shulie.append(1)
        n1 = 0
        n2 = 1
        count = 2

        while count < th:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
            shulie.append(nth)

        return shulie

if __name__ == "__main__":

    fibonacci(4)

    # print(fibonacci(4))

    # 测试
    # th = 1
    #
    # shulie = []
    # if th == 0:
    #     print("不可以0")
    # elif th == 1:
    #     shulie.append(0)
    #     print(shulie)
    # else:
    #     shulie.append(0)
    #     shulie.append(1)
    #     n1 = 0
    #     n2 = 1
    #     count = 2
    #
    #     while count < th:
    #         nth = n1 + n2
    #         n1 = n2
    #         n2 = nth
    #         count += 1
    #         shulie.append(nth)
    #
    #     print(shulie)