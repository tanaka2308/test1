#!/usr/bin/env Python
# -*- coding:utf-8 -*-
import cv2
import numpy as np

#画像の読み込み
img = cv2.imread("sample2.jpg")

#グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#閾値の設定
threshold_value = 150

#配列の作成（output用）
threshold_img = gray.copy()

#実装(numpy)
threshold_img[gray < threshold_value] = 0
threshold_img[gray >= threshold_value] = 255

#Output
cv2.imwrite("sample2-2.jpg",threshold_img)
