#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFilter


def simplePaste(img1, img2):

    back_img = img1.copy()      #消えないようにback_imgにrocket.jpgのコピーを取る
    back_img.paste(img2, (0,0))        #rocket.jpgにlena.jpgを貼りつける
    back_img.save('rocket_pillow_paste.jpg', quality=95)    #保存

    return back_img