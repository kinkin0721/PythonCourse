#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import random

import cv2
import numpy as np
import matplotlib.pyplot as plt

cmd = None
debug = False
seed = 20181030
alpha = 3.0
path = ''


# OpenCV是以(BGR)的顺序存储图像数据的
# 而Matplotlib是以(RGB)的顺序显示图像的
def bgr_to_rgb(_img):
    return cv2.merge([_img[:, :, 2], _img[:, :, 1], _img[:, :, 0]])


def do_encode(source, water_mark, output_img):
    print('image<{0}> + watermark<{1}> -> image(encoded)<{2}>'.format(source, water_mark, output_img))
    img = cv2.imread(source)
    wm = cv2.imread(water_mark)

    if debug:
        plt.subplot(231), plt.imshow(bgr_to_rgb(img)), plt.title('image')
        plt.xticks([]), plt.yticks([])
        plt.subplot(234), plt.imshow(bgr_to_rgb(wm)), plt.title('watermark')
        plt.xticks([]), plt.yticks([])

    # print img.shape # 高, 宽, 通道
    h, w, c = img.shape
    hwm = np.zeros((int(h * 0.5), w, c))
    if hwm.shape[0] <= wm.shape[0]:
        print("水印图高度大于原图")
        exit(1)
    if hwm.shape[1] <= wm.shape[1]:
        print("水印图宽度大于原图")
        exit(1)
    hwm2 = np.copy(hwm)
    for i in range(wm.shape[0]):
        for j in range(wm.shape[1]):
            for k in range(wm.shape[2]):
                hwm2.itemset((i, j, k), wm[i][j][k])

    random.seed(seed)
    m, n = list(range(hwm.shape[0])), list(range(hwm.shape[1]))
    random.shuffle(m)
    random.shuffle(n)
    for i in range(hwm.shape[0]):
        for j in range(hwm.shape[1]):
            hwm[i][j] = hwm2[m[i]][n[j]]

    rwm = np.zeros(img.shape)
    for i in range(hwm.shape[0]):
        for j in range(hwm.shape[1]):
            rwm[i][j] = hwm[i][j]
            rwm[rwm.shape[0] - i - 1][rwm.shape[1] - j - 1] = hwm[i][j]

    if debug:
        plt.subplot(235), plt.imshow(bgr_to_rgb(rwm)), \
            plt.title('encrypted(watermark)')
        plt.xticks([]), plt.yticks([])

    f1 = np.fft.fft2(img)
    f2 = f1 + alpha * rwm
    _img = np.fft.ifft2(f2)

    if debug:
        plt.subplot(232), plt.imshow(bgr_to_rgb(np.real(f1))), \
            plt.title('fft(image)')
        plt.xticks([]), plt.yticks([])

    img_wm = np.real(_img)

    assert cv2.imwrite(output_img, img_wm, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    # 这里计算下保存前后的(溢出)误差
    img_wm2 = cv2.imread(output_img)
    sum = 0
    for i in range(img_wm.shape[0]):
        for j in range(img_wm.shape[1]):
            for k in range(img_wm.shape[2]):
                sum += np.power(img_wm[i][j][k] - img_wm2[i][j][k], 2)
    miss = np.sqrt(sum) / (img_wm.shape[0] * img_wm.shape[1] * img_wm.shape[2]) * 100
    print('Miss %s%% in save' % miss)

    if debug:
        plt.subplot(233), plt.imshow(bgr_to_rgb(np.uint8(img_wm))), \
            plt.title('image(encoded)')
        plt.xticks([]), plt.yticks([])

    f2 = np.fft.fft2(img_wm)
    rwm = (f2 - f1) / alpha
    rwm = np.real(rwm)

    wm = np.zeros(rwm.shape)
    for i in range(int(rwm.shape[0] * 0.5)):
        for j in range(rwm.shape[1]):
            wm[m[i]][n[j]] = np.uint8(rwm[i][j])
    for i in range(int(rwm.shape[0] * 0.5)):
        for j in range(rwm.shape[1]):
            wm[rwm.shape[0] - i - 1][rwm.shape[1] - j - 1] = wm[i][j]

    if debug:
        assert cv2.imwrite('_bwm.debug.wm.jpg', wm)
        plt.subplot(236), plt.imshow(bgr_to_rgb(wm)), plt.title(u'watermark')
        plt.xticks([]), plt.yticks([])

    if debug:
        plt.show()


def do_decode(fn1, fn2, fn3):
    print('image<%s> + image(encoded)<%s> -> watermark<%s>' % (fn1, fn2, fn3))
    img = cv2.imread(fn1)
    img_wm = cv2.imread(fn2)

    if debug:
        plt.subplot(231), plt.imshow(bgr_to_rgb(img)), plt.title('image')
        plt.xticks([]), plt.yticks([])
        plt.subplot(234), plt.imshow(bgr_to_rgb(img_wm)), plt.title('image(encoded)')
        plt.xticks([]), plt.yticks([])

    random.seed(seed)
    m, n = list(range(int(img.shape[0] * 0.5))), list(range(img.shape[1]))
    random.shuffle(m)
    random.shuffle(n)

    f1 = np.fft.fft2(img)
    f2 = np.fft.fft2(img_wm)

    if debug:
        plt.subplot(232), plt.imshow(bgr_to_rgb(np.real(f1))), \
            plt.title('fft(image)')
        plt.xticks([]), plt.yticks([])
        plt.subplot(235), plt.imshow(bgr_to_rgb(np.real(f1))), \
            plt.title('fft(image(encoded))')
        plt.xticks([]), plt.yticks([])

    rwm = (f2 - f1) / alpha
    rwm = np.real(rwm)

    if debug:
        plt.subplot(233), plt.imshow(bgr_to_rgb(rwm)), \
            plt.title('encrypted(watermark)')
        plt.xticks([]), plt.yticks([])

    wm = np.zeros(rwm.shape)
    for i in range(int(rwm.shape[0] * 0.5)):
        for j in range(rwm.shape[1]):
            wm[m[i]][n[j]] = np.uint8(rwm[i][j])
    for i in range(int(rwm.shape[0] * 0.5)):
        for j in range(rwm.shape[1]):
            wm[rwm.shape[0] - i - 1][rwm.shape[1] - j - 1] = wm[i][j]
    assert cv2.imwrite(fn3, wm)

    if debug:
        plt.subplot(236), plt.imshow(bgr_to_rgb(wm)), plt.title(u'watermark')
        plt.xticks([]), plt.yticks([])

    if debug:
        plt.show()


def is_img(file_name):
    extension = os.path.splitext(file_name)[1]
    if extension.lower() == '.png' \
            or extension.lower() == '.jpg' \
            or extension.lower() == '.jpeg':
        return True
    else:
        return False


def encode_all(path, wm):
    if os.path.exists(path):
        dir_list = os.listdir(path)
        for file_name in dir_list:
            full_name = os.path.join(path, file_name)
            if os.path.isfile(full_name) and is_img(file_name):
                if file_name == wm:
                    continue
                img_with_wm = os.path.join(path, os.path.splitext(file_name)[0] + "_with_wm" + os.path.splitext(file_name)[1])
                do_encode(full_name, os.path.join(path, wm), img_with_wm)
                print("「" + img_with_wm + "」が上手に焼きました")

        print("肉が全部焼きました どうぞ")


if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 2:
        print('Usage: python bwm_new.py <cmd> [arg...] [opts...]')
        print('  cmds:')
        print('    encode <image> <watermark> <image(encoded)>')
        print('           image + watermark -> image(encoded)')
        print('    decode <image> <image(encoded)> <watermark>')
        print('           image + image(encoded) -> watermark')
        print('  opts:')
        print('    --debug,          Show debug')
        print('    --seed <int>,     Manual setting random seed (default is 20160930)')
        print('    --alpha <float>,  Manual setting alpha (default is 3.0)')
        print('    --path,           批量给路径下所有图片打水印')
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd != 'encode' and cmd != 'decode':
        print('Wrong cmd %s' % cmd)
        sys.exit(1)
    if '--debug' in sys.argv:
        debug = True
        del sys.argv[sys.argv.index('--debug')]
    if '--seed' in sys.argv:
        p = sys.argv.index('--seed')
        if len(sys.argv) <= p+1:
            print('Missing <int> for --seed')
            sys.exit(1)
        seed = int(sys.argv[p+1])
        del sys.argv[p+1]
        del sys.argv[p]
    if '--alpha' in sys.argv:
        p = sys.argv.index('--alpha')
        if len(sys.argv) <= p+1:
            print('Missing <float> for --alpha')
            sys.exit(1)
        alpha = float(sys.argv[p+1])
        del sys.argv[p+1]
        del sys.argv[p]
    if '--path' in sys.argv:
        p = sys.argv.index('--path')
        if len(sys.argv) <= p + 1:
            print('Missing <int> for --path')
            sys.exit(1)
        path = sys.argv[p + 1]
        del sys.argv[p + 1]
        del sys.argv[p]
    if path != '':
        if len(sys.argv) < 3:
            print('Missing arg...')
            sys.exit(1)
        fn2 = sys.argv[2]
    else:
        if len(sys.argv) < 5:
            print('Missing arg...')
            sys.exit(1)
        fn1 = sys.argv[2]
        fn2 = sys.argv[3]
        fn3 = sys.argv[4]

if cmd == 'encode':
    if path != '':
        encode_all(path, fn2)
    else:
        do_encode(fn1, fn2, fn3)
elif cmd == 'decode':
    do_decode(fn1, fn2, fn3)

    # encode_all("/Users/kinkin/img/", "wm.png")
    # do_decode("/Users/kinkin/img/hui.png", "/Users/kinkin/img/hui_with_wm.png", "/Users/kinkin/img/hui_from_wm.png")

