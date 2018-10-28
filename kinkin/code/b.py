import a


print("我是b")


def hanshua():
    print("我是函数a")


def hanshub():
    print("我是函数b")


def sqr(num):
    return num * num


if __name__ == "__main__":
    hanshua()
    print("我是b 我是main")
    c = 3
    d = sqr(3)
    e = sqr(c)

    print("c = {}, d = {}, e = {}".format(c, d, e))

