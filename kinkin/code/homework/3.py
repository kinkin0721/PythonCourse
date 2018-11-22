#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Student:
    def __init__(self, _id, _name, _chinese, _math, _english):
        self.id = id
        self.name = _name
        self.chinese = _chinese
        self.math = _math
        self.english = _english

    def avage(self):
        return (self.chinese + self.math + self.english) / 3


def get_students_data(path):
    students = dict()
    with open(path, 'r') as f:
        for line in f:
            datas = line.split(',')
            s = Student(datas[0], datas[1], datas[2], datas[3], datas[4])
            students[s.id] = s

    return students


if __name__ == "__main__":
    students_dict = get_students_data('student.txt')