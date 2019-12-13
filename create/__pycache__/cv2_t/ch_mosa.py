#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
from mosaic import mosaic as mosaic

#カスケードファイルを指定して検出器を作成
cascade = cv2.CascadeClassifier("/Users/tanaka/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml")

#画像を読み込んでグレイスケールに変換する（画像認識のほとんどがグレイスケールデータやアルゴリズムを使っているため変換する）
img = cv2.imread('hage.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#顔検出を実行
face_list = cascade.detectMultiScale(img_gray,minSize=(150,150))
if len(face_list) ==0: quit()

#認識した部分の画像にモザイクをかける
for (x,y,w,h) in face_list:
    '''
    mosaic関数の呼び出し
    戻り値-モザイク画像
    '''
    img = mosaic(img,(x,y,x+w,y+h),10)

cv2.imwrite("hage_mosa.png",img)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
