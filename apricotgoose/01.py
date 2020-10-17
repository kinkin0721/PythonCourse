# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(str(year) + "is leap year")
#     else:
#         print(str(year) + "is not leap year")


def fibonacci(n):
    arr = []

    n1 = 0
    n2 = 1
    count = 1

    if n == 0:
        return arr
    elif n == 1:
        arr.append(1)
        return arr
    else:
        arr.append(1)
        while count < n:
            nth = n1 + n2
            arr.append(nth)
            n1 = n2
            n2 = nth
            count += 1
        return arr


if __name__ == "__main__":
    # print("Hello world!")

    # count = 6
    #
    # if count == 4:
    #     print("Success")
    # else:
    #     print("Fail")
    #
    # count = 100
    #
    # if count != 4:
    #     print("Success")
    # else:
    #     print(count)
    #
    # isMonday = True
    # isSunday = False
    #
    # today = "Saturday"
    #
    # if today == "Saturday" or "Sunday":
    #     print("Day Off")
    #
    # else:
    #     print("Work")
    #
    # # isMonday = True
    # # isTuesday = False
    # # isWednesday = False
    # # isThursday = False
    # # isFriday = False
    # # isSaturday = False
    # # isSunday = False
    # #
    # # if isSaturday or isSunday:
    # #     print("Day Off")
    # # elif isMonday:
    # #     print("Day 1")
    # # elif isTuesday:
    # #     print("Day 2")
    # # else:
    # #     print("Work")
    #
    # day = [True, False, False, False, False, False, False]
    # if day[0]:
    #     print("isMonday")
    # elif day[2]:
    #     print("isWendsday")
    # else:
    #     print("Other Day")
    #
    # day = [True, False, False, False, False, False, False]
    # for index in range(len(day)):
    #     print(index+1)
    #
    # day = [False, False, False, True, False, False, False]
    # for index in range(len(day)):
    #     if day[index]:
    #         print(str(index+1) + "Yes")
    #     else:
    #         print(str(index+1) + "No")
    #
    # day = [False, False, False, True, False, False, False]
    # for today in day:
    #     print(today)
    #
    # count = 0
    # for today in day:
    #     print(count)
    #     count = count + 1
    #
    # count = 0
    # day = [True, False, False, False, False, False, False]
    # for today in day:
    #     if today:
    #         print(str(count+1) + "Yes")
    #     else:
    #         print(str(count+1) + "No")
    #     count = count + 1
    #
    # sum = 0
    # for idx in range(-1,101):
    #     sum = (sum + idx)
    #
    # print(sum)
    #
    # print(5 // 2)
    #
    # numList = [2, 3, 4, 5, 7, 9, 10, 100]
    # if 8 not in numList:
    #     print("False")
    #
    # else:
    #     print("True")
    #
    # a = [9, 0, 8, 0, 8, 2, 7, 6, 2, 1, 2, 2, 10, 39]
    # count = 0
    # for number in a:
    #     if number == 0:
    #         count += 1
    # print(count)

    # bird = 0
    # for number in a:
    #     if number == 2:
    #         break
    #     bird += 1
    # print(bird)
    #
    # bird = 0
    # dog = 0
    # for number in a:
    #     if number == 2:
    #         dog += 1
    #         if dog == 2:
    #             break
    #     bird += 1
    # print(bird)
#
# def num_print(number):
#         print(number)
#
#
# def find2(n):
#     a = [9, 0, 8, 0, 8, 2, 7, 6, 2, 1, 2, 2, 10, 39]
#
#     count = 0
#     count_for_2 = 0
#     for number in a:
#         if number == 2:
#             count_for_2 += 1
#             if count_for_2 == n:
#                 break
#         count += 1
#     print(count)
#
#     is_leap_year(2018)

    print(fibonacci(5))
#
#
# arr = []
# for index in range(5):
#     arr.append(index + 1)
#     print(arr)
#
# arr = [1, 2, 4, 7, 2, 8, 2, 0, 2, 2, 10]
# while 2 in arr:
#     arr.remove(2)
#
# print(arr)
#
# a = [1, 2, 3, 7, 10, 4]
# sum = 0
# for number in a:
#     sum = (sum + number)
#
# print(sum)