from statistics import mean

if __name__ == "__main__":

    # 拆成每个人
    txt = open('student.txt')
    txt_str = txt.read()
    txt_str2 = txt_str.strip()
    txtLine_str = txt_str2.replace('\n', ',')
    oneStudent_list = txtLine_str.split(',')

    # 键值对
    name_keys = oneStudent_list[1::5]
    print('名字key:' + str(name_keys))
    chinese_values = oneStudent_list[2::5]
    chinese_values = list(map(int, chinese_values))
    print('语文成绩values:' + str(chinese_values))
    math_values = oneStudent_list[3::5]
    math_values = list(map(int, math_values))
    print('数学成绩values:' + str(math_values))
    english_values = oneStudent_list[4::5]
    english_values = list(map(int, english_values))
    print('英语成绩values:' + str(english_values))
    # all_values =

    # all_values = sum(str(oneStudent_list[4::5]))
    # all_values2 = list(map(int, all_values))
    # oneStudent_list2 = list(map(int, oneStudent_list))
    # all_values = sum(list)

    # print(data2)

    # 字典
    student_dict = dict()
    chinese_dict = dict()
    math_dict = dict()
    english_dict = dict()
    all_dict = dict()

    chinese_dict = dict(zip(name_keys, chinese_values))
    print('chinese_dict:' + str(chinese_dict))
    math_dict = dict(zip(name_keys, math_values))
    print('math_dict:' + str(math_dict))
    english_dict = dict(zip(name_keys, english_values))
    print('english_dict:' + str(english_dict))

    # 各科成绩最好的人
    max_chinese = max(chinese_dict, key=chinese_dict.get)
    print('语文第一名:' + max_chinese)
    max_math = max(math_dict, key=math_dict.get)
    print('数学第一名:' + max_math)
    max_english = max(english_dict, key=english_dict.get)
    print('英语第一名:' + max_english)

    # student_values = [chinese_values, math_values, english_values]
    # student_dict = dict(zip(name_keys, student_values))
    # print('student_values:' + str(student_values))

    # avg = sum(int(str(student_values)))/len(int(str(student_values)))
    # print(type(avg))
    # print(avg)

    # avgStudent_dict = {}
    # for k,v in student_dict.__iter__():
    #     avgStudent_key = sum(student_values)/(len(student_values))
    #
    #     print(avgStudent_key)

    # ～～～～～～～～～～字典好像列错了～～～～～～～～～～

    # # 拆成每个人
    # txt = open('student.txt')
    # txt_str = txt.read()
    # txt_str2 = txt_str.strip()
    # txtLine_str = txt_str2.replace('\n', ',')
    # oneStudent_list = txtLine_str.split(',')
    #
    # # 键值对
    # name_keys = oneStudent_list[1::5]
    # print('名字key:' + str(name_keys))
    # chinese_values = oneStudent_list[2::5]
    # print('语文成绩values:' + str(chinese_values))
    # math_values = oneStudent_list[3::5]
    # print('数学成绩values:' + str(math_values))
    # english_values = oneStudent_list[4::5]
    # print('英语成绩values:' + str(english_values))
    # # all_values =
    #
    # # all_values = sum(str(oneStudent_list[4::5]))
    # # all_values2 = list(map(int, all_values))
    # # oneStudent_list2 = list(map(int, oneStudent_list))
    # # all_values = sum(list)
    #
    # # print(data2)
    #
    # # 字典
    # student_dict = dict()
    # chinese_dict = dict()
    # math_dict = dict()
    # english_dict = dict()
    # all_dict = dict()
    #
    # chinese_dict = dict(zip(name_keys, chinese_values))
    # print('chinese_dict:' + str(chinese_dict))
    # math_dict = dict(zip(name_keys, math_values))
    # print('math_dict:' + str(math_dict))
    # english_dict = dict(zip(name_keys, english_values))
    # print('english_dict:' + str(english_dict))
    #
    # # avg
    # # for k,v in chinese_dict.iteritems():
    #
    # # 成绩最好的人
    # max_chinese = max(chinese_dict, key=chinese_dict.get)
    # print('语文第一名:' + max_chinese)
    # max_math = max(math_dict, key=math_dict.get)
    # print('数学第一名:' + max_math)
    # max_english = max(english_dict, key=english_dict.get)
    # print('英语第一名:' + max_english)


    # ～～～～～～～～～～old～～～～～～～～～～

    # count = 0
    # nameCount = 0
    # for count in range(len(oneStudent_list)):
    #
    #     count += 1
    #     nameCount += 5

    # # keys和values
    # name_keys = []
    # chinese_values = []
    # math_values = []
    # english_values = []
    # all_values = []
    #
    # count = 0
    # nameCount = 1
    # chineseCount = 2
    # mathCount = 3
    # englishCount = 4
    #
    # for count in oneStudent_list:
    #     name_keys.append(oneStudent_list[nameCount])
    #     chinese_values.append(oneStudent_list[chineseCount])
    #     math_values.append(oneStudent_list[mathCount])
    #     english_values.append(oneStudent_list[englishCount])
    #
    #     chineseCount = chineseCount + 5
    #     mathCount = mathCount + 5
    #     englishCount = englishCount + 5
    #     #
    #     # count = count + 1
    #     nameCount = nameCount + 5
    #
    # # name_keys = ['1', '2', '3', '4']
    # # chinese_values = [78, 30, 89, 88]
    #
    # chinese_dict = dict(zip(name_keys, chinese_values))

    # chinese_dict = dict(zip(name_keys, chinese_values))

    # max_chinese = max(zip(chinese_dict.keys(), chinese_dict.values()))

    # prices = {
    #     'ACME': 45.23,
    #     'AAPL': 612.78,
    #     'IBM': 205.55,
    #     'HPQ': 37.20,
    #     'FB': 10.75
    # }
    # min_price = max(zip(prices.keys(), prices.values()))
    # print(min_price)

    # n = 1
    # for n in range(len(student_list)):
    #     student_dict['name'] = student_list[n]
    #     print(student_dict)
    #     n = n + 4

    # student1_dict = dict()
    #
    # student1_dict['name'] = 'nn'

    # student_dict = {student_list[0]:student_list[1], }

    # print(name_keys)
    # print(chinese_values)
    # print(math_values)
    # print(english_values)
    # count = 5
    # print(type(oneStudent_list[count+1]))
    # #
    # print(oneStudent_list[count+1])

    # print(oneStudent_list)
    # print(max_chinese)
    # print(max_math)
    # print(max_english)
    #
    # print(oneStudent_list[6])
    # print(oneStudent_list[7])
    # print(oneStudent_list[2])
    # print(oneStudent_list)
    #
    # print(type(chinese_values))

    # # 生成dict
    # count = 0
    # nameCount = 1
    # chineseCount = 2
    # mathCount = 3
    # englishCount = 4
    # for count in range(len(oneStudent_list)):
    #     student_dict = dict()
    #     student_dict['name'] = oneStudent_list[nameCount]
    #     student_dict['chinese'] = oneStudent_list[chineseCount]
    #     student_dict['mathCount'] = oneStudent_list[mathCount]
    #     student_dict['englishCount'] = oneStudent_list[englishCount]
    #     print(student_dict)
    #
    #     nameCount = nameCount + 5
    #     chineseCount = chineseCount + 5
    #     mathCount = mathCount + 5
    #     englishCount = englishCount + 5
    #
    #     count = count + 1

