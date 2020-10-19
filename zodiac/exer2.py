# exer2_1

n = 0
h = 100
s = 0
while n < 11:
    h = h/2
    s = s + h
    n = n + 1
print(("小球共经过: ") + str(s) + ("米"))
print(("小球反弹高度: ") + str(h) + ("米"))

# exer2_2

a = 1
n = 0
sum = 0
while n<21:
    a = a * (a+1)
    sum = sum + a
    n = n + 1
print(sum)
