


if __name__ == "__main__":

    import os
    # 每一txt的路径和名字
    module_path = os.path.dirname(__file__)
    path = module_path + '/book/'

    allFileName = os.listdir(path)

    # for循环，每一txt，加在一起生成list，并删除
    count = 0
    n = 0
    result = []
    for index in allFileName:
        fileName = path + str(allFileName[n])
        book = open(fileName)
        bookRead = book.read()
        result.append(bookRead)
        os.remove(fileName)
        count += 1
        n += 1

    resultBook = open('resultBook.txt', 'w')
    resultBook.write(''.join(result))
    resultBook.close()

    print('done')



    # result = open(fileName)


    # bookRead = book.read()
    # print(bookRead)


    # result = []
    # os.write(result, )

    # for index in allFileName:
    #     result.append()

    # result = []
    #
    # for file in fileName:
    #     result =


    # book_txt = open('/book/1.txt')
    # print(book_txt)


