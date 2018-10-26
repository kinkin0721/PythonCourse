#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


# 随机生成一个每一位各不相同的4位数，作为谜底
def make_answer():
    numbers = list()
    for i in range(10):
        numbers.append(i)

    answer = ""
    for i in range(4):
        rand_index = random.randint(0, len(numbers)-1)
        answer += str(numbers[rand_index])
        numbers.remove(numbers[rand_index])

    return answer


# 检查玩家的猜测是否正确
def check_guess(answer, guess):
    return answer == guess


# 计算玩家猜对的数字的个数（不需要检查位置）
# 不用set
def get_right_number_count(answer, guess):
    count = 0
    for num in guess:
        if num in answer:
            count += 1

    return count
# 使用set
# def get_right_number_count(answer, guess):
#     answer_set = set(answer)
#     guess_set = set(guess)
#
#     return len(answer_set & guess_set)


# 计算玩家数字以及位数皆正确的个数
def get_right_number_and_position_count(answer, guess):
    count = 0
    for i in range(4):
        if answer[i] == guess[i]:
            count += 1

    return count


def is_guess_legal(guess):
    if len(guess) != 4:
        print("请输入4位数")
        return False

    for s in guess:
        if ord(s) < 48 or ord(s) > 57:
            print("请不要输入数字以外的字符！")
            return False

    if set(guess) != len(guess):
        print("请不要输入重复数字！")
        return False

    return True


def play_with_single_player_mode():
    print("开始多人模式")
    guess_limit = int(input("请输入可猜次数："))
    answer = make_answer()
    print("猜数字小游戏开始啦!答案为一个没有重复数字4位数")

    while guess_limit > 0:
        guess = input("请输入你的猜测：")

        if not is_guess_legal(guess):
            continue

        if not check_guess(answer, guess):
            count_a = get_right_number_and_position_count(answer, guess)
            count_b = get_right_number_count(answer, guess)
            print(str(count_a) + 'A' + str(count_b) + 'B')
        else:
            print("猜对啦！")
            break

        guess_limit -= 1

    if guess_limit == 0:
        print("太可惜啦，下次加油")


def play_with_multiplayer_mode():
    print("开始单人模式")
    player_count = int(input("请输入玩家人数："))
    answer = make_answer()
    print("猜数字小游戏开始啦!答案为一个没有重复数字4位数")

    while True:
        for i in range(player_count):
            guess = input("Player" + str(i + 1) + "请输入你的猜测：")

            while not is_guess_legal(guess):
                guess = input("Player" + str(i+1) + "请输入你的猜测：")

            if not check_guess(answer, guess):
                count_a = get_right_number_count(answer, guess)
                count_b = get_right_number_and_position_count(answer, guess)
                print(str(count_a) + 'A' + str(count_b) + 'B')
            else:
                print("猜对啦！本局的胜者是：Player" + str(i+1))
                return


if __name__ == "__main__":
    print("请选择游玩模式。单人模式输入1，多人模式输入2")
    play_mode = int(input())
    if play_mode == 1:
        play_with_single_player_mode()
    elif play_mode == 2:
        play_with_multiplayer_mode()



