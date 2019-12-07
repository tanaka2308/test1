#!/usr/bin/env Python
# -*- coding:utf-8 -*-

import cv2
import numpy as np

#画像の読み込み
img = cv2.imread('sample.jpg')

#グレースケール変換
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#閾値の設定
threshold_value = 110

#配列の作成（output用）
threshold_img = gray.copy()

#実装（numpy）
threshold_img[gray < threshold_value] = 0
threshold_img[gray >= threshold_value] = 255

#output
cv2.imwrite("sample2-2.png",threshold_img)

#グレースケール変換された画像の読み込み
img = cv2.imread('sample2-2.png')

#この部分では、画像処理をする近傍の大きさ等を設定する場所である。
#ノイズ除去
ksize=3
#中央値フィルタ
img_mask = cv2.medianBlur(img,ksize)
#白黒反転画像
img2 = cv2.bitwise_not(img_mask)

#output:sample2-3,2-4
cv2.imwrite("sample2-3.png",img_mask)
cv2.imwrite("sample2-4.png",img2)


#背景透過
from PIL import Image

#画像の読み込み
org = Image.open("sample2-3.png")

#サイズが同じ画像作成
trans = Image.new('RGBA',org.size,(0,0,0,0))

#縦横のサイズ
width = org.size[0]
height = org.size[1]
#for文で処理
for x in range(width):
    for y in range(height):
        pixel = org.getpixel( (x,y) )

        #白色処理なし
        if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
            continue

        #白色以外の書き込み
        trans.putpixel((x,y),pixel)
trans.save('sample2-5.png')

"""
#省略タイプ
import cv2
import numpy as np
from PIL import Image

#画像の読み込み
img = cv2.imread('sample2-1.png')
#グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#閾値の設定
threshold_value = 110
#配列の作成（output用）
threshold_img = gray.copy()
#実装(numpy)
threshold_img[gray < threshold_value] = 0
threshold_img[gray >= threshold_value] = 255

#ノイズ除去処理
ksize=3
#中央値フィルタ
img_mask = cv2.medianBlur(img,ksize)

#白黒反転画像
img2 = cv2.bitwise_not(img_mask)

#背景透過
# 画像の読み込み
org = Image.open('sample2-3.png')

# サイズが同じ画像作成
trans = Image.new('RGBA', org.size, (0, 0, 0, 0))

#縦横のサイズ
width = org.size[0]
height = org.size[1]
#for文で処理
for x in range(width):
    for y in range(height):
        pixel = org.getpixel( (x, y) )

        # 白色処理なし
        if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
            continue

        # 白色以外の書き込み
        trans.putpixel( (x, y), pixel )

#Output:sample2-2~2-5
cv2.imwrite(f'C:\\Users\\fgdao\\python\\project1\\sample2-2.png',threshold_img)
cv2.imwrite("C:\\Users\\fgdao\\python\\project1\\sample2-3.png",img_mask)
cv2.imwrite("C:\\Users\\fgdao\\python\\project1\\sample2-4.png",img2)
trans.save('sample2-5.png')
"""
