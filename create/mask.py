#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFilter, ImageOps


def simpleMask(img1, img2):

    mask_img = Image.open('horse.png').resize(img2.size).convert('L')
    #ネガポジ反転しているため、切り抜きが逆になる
    #mask_img = ImageOps.invert(mask_img)

    back_img = img1.copy()
    back_img.paste(img2, (100, 50), mask_img)
    back_img.save('rocket_pillow_paste_mask_horse.jpg', quality=95)

    return back_img