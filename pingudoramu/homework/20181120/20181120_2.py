
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont


def yanZhengMa_def():

    alpha_list= list(range(65, 91)) + list(range(97, 123)) + list(range(48, 58))
    yanZhengMa_list = chr(random.choice(alpha_list))
    return str(yanZhengMa_list)

    # 没用
    # # 验证码里出现的所有数字字母，在ASCII的序号
    # alpha_list= list(range(65, 91)) + list(range(97, 123))
    #
    # # 随机4个ASCII的序号
    # yanZhengMaAlpha_list = []
    # for count in range(4):
    #     yanZhengMaAlpha_list.append(random.choice(alpha_list))
    #
    # # 随机的4个ASCII序号，转字母or数字
    # yanZhengMa_list = []
    # n = 0
    # for count in range(4):
    #     yanZhengMa_list.append(chr(yanZhengMaAlpha_list[n]))
    #     n = n + 1
    #
    # return str(yanZhengMa_list)


def bgColor_def():

    bgColor_list = []
    for index in range(3):
        bgColor_list.append(random.randint(64, 255))
    return tuple(bgColor_list)

    # 法二
    # bgColor = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    # return bgColor


def fontColor_def():

    fontColor_list = []
    for index in range(3):
        fontColor_list.append(random.randint(32, 127))
    return tuple(fontColor_list)

    # 法二
    # fontColor = (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    # return fontColor


if __name__ == "__main__":

    print(yanZhengMa_def())

    print(bgColor_def())
    print(fontColor_def())

    # 创建空白图片
    width = 240
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建字体
    font = ImageFont.truetype('Arial Bold.ttf', 36)
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(image)

    # 画背景
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=bgColor_def())

    # 画四个字
    count = 0
    for count in range(4):
        draw.text((60 * count + 10, 10), yanZhengMa_def(), fill=(fontColor_def()), font=font)
        count = count + 1

    # 模糊
    image = image.filter(ImageFilter.BLUR)

    # 保存图片
    image.save('yanZhengMa.jpg', 'jpeg')