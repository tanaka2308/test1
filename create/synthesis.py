#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFilter


def synthesis(img1, img2):

    #円形の白黒マスク作成
    mask_img = Image.new("L", img2.size, 0)         #白黒に
    draw = ImageDraw.Draw(mask_img)                 #ImageDrawオブジェクトの生成
    draw.ellipse((140, 50, 260, 170), fill=255)     #円形にする

    mask_im_blur = mask_img.filter(ImageFilter.GaussianBlur(10))    #ブラーをあてる
    mask_im_blur.save('mask_circle_blur.jpg', quality=95)           #一応保存

    back_img = img1.copy()      #消えないようにback_imgにrocket.jpgのコピーを取る
    back_img.paste(img2, (0,0), mask_im_blur)        #rocket.jpgにlena.jpgを貼りつける
    back_img.save('rocket_pillow_paste.jpg', quality=95)    #保存

    return back_img