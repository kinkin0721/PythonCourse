a = int(input("请输入一个数值："))
n = int(input("请输入次数："))

if a == 0:
    print(0)
elif n == 0:
    print(0)
elif n == 1:
    print(a)
else:
    sum = 0
    while n > 0:
        m = n - 1
        b = 0
        while m >= 0:
            b = b + a * 10 ** m
            m = m - 1
        n = n - 1
        sum = sum + b
        print("b =" + str(b))

    print("sum =" + str(sum))
