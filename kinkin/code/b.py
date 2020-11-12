# import a

print("name=" + __name__)
print("我是b.py")


def funa():
    print("我是函数a")


def funb():
    print("我是函数b")


def sqr(num):
    return num * num


if __name__ == "__main__":
    funa()
    print("我是b 我是main")
    c = 3
    d = sqr(3)
    e = sqr(c)
    print("c = {}, d = {}, e = {}".format(c, d, e))


print("我是b after main")

