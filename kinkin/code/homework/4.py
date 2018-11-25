#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


def get_all_chapters(path):
    contents = dict()
    if os.path.exists(path):
        dirs = os.listdir(path)
        for file_name in dirs:
            full_name = os.path.join(path, file_name)
            # 方法一 with open
            with open(full_name, 'r') as f:
                chapter = int(os.path.splitext(file_name)[0])
                contents[chapter] = f.read()
            os.remove(full_name)

            # # 方法二 open close
            # try:
            #     f = open(full_name, 'r')
            #     chapter = int(os.path.splitext(file_name)[0])
            #     contents[chapter] = f.read()
            # finally:
            #     if f:
            #         f.close()
            # os.remove(full_name)

    return contents


if __name__ == "__main__":
    path = 'book'

    # 获取所有每个txt内内容 即每章内容
    content_dict = get_all_chapters(path)

    # 按章节顺序拼接
    content = ''
    for key in sorted(content_dict.keys()):
        content += content_dict[key]

    # 写入book.txt
    with open(os.path.join(path, 'book.txt'), 'w') as file:
        file.write(content)




