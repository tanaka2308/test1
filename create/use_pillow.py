#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageFilter

#import paste
#import composite
#import synthesis
#import mask
#import concat
#import invert
import make_shape

im1 = Image.open('rocket.jpg')
im2 = Image.open('lena.jpg')


#画像の上に画像を貼り付けるのみ
#img = paste.simplePaste(im1, im2)

#マスク画像、半分透過
#img = composite.simpleComposite(im1, im2)

#マスク画像、馬の形にマスク
#img = mask.simpleMask(im1, im2)

#画像の連結
#img = concat.get_concat_h(im1, im2)    #画像を横並びに貼る
#img = concat.get_concat_v(im1, im2)    #画像を縦並びに貼る

#ネガポジ反転のみ
#img = invert.simpleInvert(im1)    #ネガポジ反転

#マスク、ブラー
#img = synthesis.synthesis(im1, im2)

#画像の変形
img = make_shape.makeShape()


#表示
img.show()
