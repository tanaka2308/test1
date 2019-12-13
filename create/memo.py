Pillow, NumPy, OpenCVの基本的な違いと使い分け

https://note.nkmk.me/python-image-processing-pillow-numpy-opencv/

Pillow, NumPy, OpenCVのそれぞれの位置づけは

Pillow(PIL): 画像処理ライブラリ
NumPy: 数値計算ライブラリ
OpenCV: コンピュータビジョンライブラリ

なので、得意分野・守備範囲に違いがある。
基本的には以下のように使い分けられる。

Pillow(PIL)
リサイズやトリミングなどの基本的な処理を行いたい場合

画像に別の画像を貼り付ける
２枚の画像を合成する
複数の画像を連結（結合）する
透過png画像を作成
ネガポジ反転（画素値を逆転）
円形や正方形のサムネイル画像を作成
図形描画
アニメーションgifを作成


NumPy ( + Pillow or OpenCV)
画素値ごとに算術演算などの処理を行いたい場合
画像をNumPyの配列ndarrayとして読み込んで計算・操作する
NumPy単体で画像ファイルを読み込むことはできないので、PillowやOpenCVなどと併用する

画像をNumPy配列ndarrayとして読み込むと、
NumPyの機能を使って様々な画像処理を行うことができる。
特に各画素値に対して算術演算を行う処理が簡単に書ける。

単色化
ネガポジ反転（画素値の反転）
減色処理
二値化処理
ガンマ補正
グラデーション画像生成


OpenCV
ndarrayの処理に加えて、顔認識などコンピュータビジョン系の処理を行いたい場合
画像から何かを認識したり検出したりする場合はOpenCVを使う。豊富な機能がある。

顔検出（顔認識）
モザイク処理
図形描画
複数の画像を連結（結合）する