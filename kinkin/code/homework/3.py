#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Student:
    def __init__(self, _id, _name, _chinese, _math, _english):
        self.id = int(_id)
        self.name = _name
        self.chinese = int(_chinese)
        self.math = int(_math)
        self.english = int(_english)
  
    def avage(self):
        return (self.chinese + self.math + self.english) / 3

    def sum(self):
        return self.chinese + self.math + self.english


def get_students_data(path):
    students = dict()
    with open(path, 'r') as f:
        for line in f:
            datas = line.strip().split(',')
            s = Student(datas[0], datas[1], datas[2], datas[3], datas[4])
            students[s.id] = s

    return students


def max(students_dict, course):
    max = 0
    zuigaofen_tongxue = 0
    if course == 'chinese':
        for key in students_dict:
            s = students_dict[key]
            if s.chinese > max:
                max = s.chinese
                zuigaofen_tongxue = s.id

    return zuigaofen_tongxue


if __name__ == "__main__":
    students_dict = get_students_data('student.txt')

    for key in students_dict:
        s = students_dict[key]
        print('{}的平均分: {}'.format(s.name, s.avage()))

    students_dict[1].name


