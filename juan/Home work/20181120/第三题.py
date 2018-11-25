#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Student:
    def __init__(self, _id, _name, _chinese, _math, _english):
        self.id = _id
        self.name = _name
        self.chinese = _chinese
        self.math = _math
        self.english = _english


def get_students_data(path):
    students = dict()
    with open(path, 'r') as txt:
        for line in txt:
            list = line.split(',')
            s = Student(list[0], list[1], list[2], list[3], list[4])
            students[s.id] = s
    return students


def average_each(students):
    for key in students:
        nam = students[key].name
        average = (students[key].chinese + students[key].math + students[key].english)/3
        print(str(nam) + "的三课平均分： " + average)
        break


def sort_data(students):
    chinese_max = sorted(students.items(), key=lambda item: item[1].chinese, reverse=True)
    print("Chinese Winner： " + chinese_max[0].name)
    math_max = sorted(students.items(), key=lambda item: item[1].math, reverse=True)
    print("Math Winner： " + math_max[0].name)
    english_max = sorted(students.items(), key=lambda item: item[1].english, reverse=True)
    print("English Winner： " + english_max[0].name)


def sum_s(students):
    for key in students:
        sum_each = students[key].chinese + students[key].math + students[key].english
        return sum_each


if __name__ == "__main__":
    students_dict = get_students_data('student.txt')
    sum_max = sorted(sum_s(students_dict), reverse=True)

    average_each(students_dict)
    sort_data(students_dict)
    print(sum_max[0])



