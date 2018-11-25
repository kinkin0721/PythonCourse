#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rand_char():
    ln = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789' + '9876543210'
    basic_string = list(ln)
    return random.sample(basic_string,4)


def rand_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))


def picture_draw():
    height=60
    width=240
    image=Image.new('RGB',(width,height),(255,255,255))
    font=ImageFont.truetype("/Library/Fonts/Arial.ttf", 36)
    draw=ImageDraw.Draw(image)
    for i in range(width):
        for j in range(height):
            draw.point((i, j), fill=rand_color())

    for i in range(4):
        draw.text((60*i+10, 19), rand_char()[i], font=font, fill=(random.randint(30, 120), random.randint(30, 120),
                                                              random.randint(30, 120)))

    image=image.filter(ImageFilter.BLUR)
    image.save('PHOTO.jpg', 'jpeg')
    image.show()


if __name__ == '__main__':
    picture_draw()

