#Python练习01 基础

1.输入a和n，求s=a+aa+aaa+...na...，a表示数值，n表示数量，如a=3，n=5，则求出3+33+333+3333+33333的值
```python
a = int(input("请输入一个数值："))
n = int(input("请输入次数："))
```

2.斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。<em>给出项数n，求从第0项到第n项的总和sum。</em>如n=4,则sum=0+1+1+2+3=7

3.打印出所有的“水仙花数”，所谓“水仙花数”是指一个<em>三位数</em>，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方

4.输入某年某月某日，判断这一天是这一年的第几天？
```python
year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
```

5.质数（Prime number），又称素数，指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数。输入一个数，判断该数字是否是质数。

6.输入一个奇数，然后判断最少几个9除于该数的结果为整数。如输入13，999999 / 13 = 76923， 则答案为6。
