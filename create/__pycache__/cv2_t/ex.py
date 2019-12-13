#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
OpenCVは画像処理・解析の機能をもつライブラリ
'''
import cv2
import matplotlib.pyplot as plt

#カスケードファイルを指定して検出器を作成
'''
OpenCVには機能の一つに物体検出という機能がある
物体を検出する方法は「物体の特徴を抽出」⇒「抽出した特徴量を学習」⇒「学習データにより物体を検出」
この機械学習された学習データ(XMLファイル)を、カスケード分類器という
'''
'''
cv2.CascadeClassifier()...顔検出
OpenCVにあるxmlファイルを使って顔認証
'''
cascade = cv2.CascadeClassifier("/Users/tanaka/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml")

#画像を読み込んでグレイスケールに変換する（画像認識のほとんどがグレイスケールデータやアルゴリズムを使っているため変換する）
'''
imread()...画像の読み込み
読み込む際に画像を指定の形式に変換できる
これで画像のファイルを読み込むと、色の順番がRGBではなくBGRとなってしまうので注意
'''
img = cv2.imread('hage.png')

'''
cvtColor() - RGBやBGR、HSVなど様々な色空間を相互に変換できる。(下でまた出る)
今回は、BGRからグレイスケールに変換している
'''
'''
グレースケールにする理由

多くの画像処理アルゴリズムは単一チャネル（グレースケール）画像のみを対象とする
人間の視覚特性として色差成分よりも、輝度成分に対して強い感度を持っている
計算量削減・作業メモリ削減のために、扱うデータが3チャネルよりも1チャネルの方が好ましい
なお、単一チャネルのグレイスケール画像のみから、
カラー画像（3チャネル画像）を復元することは 原理的に不可能 。
一般にグレイスケール画像という場合、カラー画像から「色差」という情報を削ぎ落とし、
主成分である「輝度」情報のみに要約したものを指す。

「画像処理でグレースケール変換するケース」としては、例えばどんな処理がある？

色情報を利用する必要が無く、空間情報（オブジェクト形状など）に着目するアルゴリズムでは、
グレースケール変換を行う。
'''
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#顔認識を実行
'''
判定画像(読み込んだ画像)全体から一部を切り取って様々な基準で判定していく。
1回でも「顔でない」と判定されれば、後続の判定は行わず、次の画像の一部に対して
判定器にかけていけいます。全判定をしないことにより、顔検出処理の高速化を実現しています
(個々の判定精度は低いですが、多く重ねることにより全体として精度を保ちます)。
'''
'''
#image – CV_8U 型の行列．ここに格納されている画像中から物体が検出されます
#objects – 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
#scaleFactor – 各画像スケールにおける縮小量を表します
#minNeighbors – 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要があります
#flags – このパラメータは，新しいカスケードでは利用されません．古いカスケードに対しては，cvHaarDetectObjects 関数の場合と同じ意味を持ちます
#minSize – 物体が取り得る最小サイズ．これよりも小さい物体は無視されます
'''
face_list = cascade.detectMultiScale(img_gray,minSize=(150,150))

'''
正直どうやって座標を求めているのかよくわかりませんので後で調べる
'''
'''
face_list: [[155 127 247 247]]
顔を認識した座標(左上(155,127)と右下(247,247)の座標？)
'''
print("face_list:",face_list)

#結果を確認
'''
顔の判定を行った際に判定箇所がなかった場合"０"？
quit()で終了
'''
if len(face_list) == 0:
    print("失敗")
    quit()

#認識した部分に印をつける

for (x,y,w,h) in face_list:
    print("顔の座標＝",x,y,w,h)
    red = (0,0,255)             #色の指定 今回は赤で囲むため(0,0,255)
    cv2.rectangle(img,(x,y),(x+w,y+h),red,thickness=20) #顔を赤四角で囲む

#認識下部分に印をつける
'''
imwrite(filename, img[, params]) で画像をファイルへ出力
imshow(winname, mat) で画像の表示
winname – 作成されるトラックバーの親として用いられるウィンドウの名前
cvtColor(img,cv2.COLOR_BGR2RGB) - これでBGRからRGBに戻している
'''
cv2.imwrite("face-detect.png",img)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()