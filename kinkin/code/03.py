#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


def rename(path):
    if os.path.exists(path):
        dir_list = os.listdir(path)
        for file_name in dir_list:
            full_name = os.path.join(path, file_name)
            if os.path.isfile(full_name):
                extension = os.path.splitext(file_name)[1]
                new_name = os.path.splitext(file_name)[0].replace("／", "《") \
                    + "》" + extension
                os.rename(full_name, os.path.join(path, new_name))
            else:
                rename(full_name)


rename("/Users/kinkin/PythonCourse/kinkin/code/rename")





