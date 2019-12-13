#!/usr/bin/env Python
# -*- coding:utf-8 -*-
import cv2
from PIL import Image,ImageFilter
import numpy as np

def resize_image(filepath,width,height):
    img = Image.open(filepath)
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
