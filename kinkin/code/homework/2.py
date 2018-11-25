#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string


# 随机验证码
def rand_code():
    elements = string.ascii_letters + string.digits

    code = ''
    for idx in range(4):
        code += random.choice(elements)

    return code


# 随机颜色
def rand_color1():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def rand_color2():
    return random.randint(0, 127), random.randint(0, 127), random.randint(0, 127)


def make_verification_code():
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height))
    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rand_color1())
    # 输出文字:
    code = rand_code()
    for i in range(4):
        draw.text((60 * i + 10, 10), code[i], font=font, fill=rand_color2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


if __name__ == "__main__":
    make_verification_code()
