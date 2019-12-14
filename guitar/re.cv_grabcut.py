#!/usr/bin/env Python
# -*- coding:utf-8 -*-
import cv2
from PIL import Image,ImageFilter
import numpy as np

def resize_image(filepath,width,height):
    img = Image.open(filepath)
    #比率を保存したまま縮小
    img.thumbnail((width,height),resample=Image.BICUBIC)
    return img

IMG_BASE_PATH = "./img/"
filename = "guitar.jpg"
WIDTH = 1000
HEIGHT = 1000
file_path = IMG_BASE_PATH + filename
pillow_img = resize_image(file_path,WIDTH,HEIGHT)
resized_image_path = f'{IMG_BASE_PATH}resized_{filename}'
pillow_img.save(resized_image_path)

img = cv2.imread(resized_image_path)

#引数はX座標、y座標、幅、高さ
rect = (1,1,pillow_img.size[0],pillow_img.size[1])

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fdgModel = np.zeros((1,65),np.float64)

cv2.grabCut(img,mask,rect,bgdModel,fdgModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imwrite('img/test.jpg', img)

#この部分では、画像処理をする近傍の大きさ等を設定する場所である。
#ノイズ除去
ksize=5
#中央値フィルタ
img_mask = cv2.medianBlur(img,ksize)

#output:sample2-3,2-4
cv2.imwrite("noise_guitoar.png",img_mask)


#背景透過
from PIL import Image

#画像の読み込み
org = Image.open("noise_guitoar.png")

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
trans.save('./img/transparent_guitoar.png')

#背景画像生成

#rocketのところを任意の色、画像と組み合わせるようにする
im1 = Image.open('./img/rocket.jpg')
'''
#im1 = Image.new('RGBA', (1, 1), 'lime')
'''
mask_im = Image.open(org).convert('L')

back_im = im1.copy()
back_im.paste(org, (1, 1), org)
back_im.save('rocket_paste_guitoar.jpg', quality=95)
