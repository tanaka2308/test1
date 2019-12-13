#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2

'''
モザイクをかけるための関数が入ったコード
'''
def mosaic(img,rect,size):

    (x1,y1,x2,y2) = rect        #今回はそれぞれ 155,127,247,247
    w = x2 - x1                 #顔認証をした、横幅　247-155
    h = y2 - y1                 #顔認証をした、縦幅　247-127
    i_rect = img[y1:y2,x1:x2]   #画像の切り取り

    #一度縮小して拡大する
    '''
    dst = cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    引数
    src: 入力画像
    dsize: 出力サイズ
    dst: 出力画像
    fx: x 方向の倍率
    fy: y 方向の倍率
    interpolation: 補完方法
    cv2.INTER_NEAREST: 最近傍補間
    cv2.INTER_LINEAR: バイリニア補間 (デフォルト)
    cv2.INTER_CUBIC: バイキュービック補間
    cv2.INTER_AREA: 平均画素法
    cv2.INTER_LANCZOS4: Lanczos 補間
    返り値
    dst: 出力画像

    ---cv2.INTER_AREA---
    平均画素法は、別名で面積平均法とも呼ばれ、ピクセルの面積比を考慮して平均して補間する方法で、
    通常は縮小専用として使われている手法です。
    得られる画質の割に、処理速度が比較的高速です。拡大した場合、画像によっては
    最近傍法とほぼ同様となりますが、縮小した場合、わずかにぼやけますが、自然で滑らかな画質を得られます。
    モアレを避けることができる。

    ---モアレ---
    規則正しい繰り返し模様を複数重ね合わせた時に、それらの周期のずれにより視覚的に発生する縞模様のこと
    画像の画素解像度と模様の周波数のずれが原因で縞模様が発生すること
    '''
    #顔検出範囲であるi_rectを、幅size,高さsize (10,10)にサイズ変更
    i_small = cv2.resize(i_rect,(size,size))

    #サイズ(10, 10)にした顔検出範囲の画像i_smallを、
    #(10,10)のサイズで幅w,高さh(顔認証範囲の元の大きさ)に平均画素法？
    i_mos = cv2.resize(i_small,(w,h),interpolation=cv2.INTER_AREA)
    #モザイク部分を数えると[10＊10]にしっかりなってました。
    # https://blog.imind.jp/entry/2019/05/06/224816
    #最近傍補間 バイリニア補間（デフォルト）平均画素法
    #バイキュービック補間 Lanczos法の補間 etc... 種類についてはおいおい調べる

    #モザイク画像を重ねる
    img2 = img.copy()           #imgをコピー
    img2[y1:y2,x1:x2] = i_mos   #顔認証した箇所に当てはめる
    return img2
