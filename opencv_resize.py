# -*- coding: utf-8 -*-
import cv2

# 画像の読み込み
img = cv2.imread("hoge.png", 1)

# 読み込んだ画像の高さと幅を取得
height = img.shape[0]
width = img.shape[1]

# 画像のサイズを変更
 # 第一引数：サイズを変更する画像
 # 第二引数：変更後の幅
 # 第三引数：変更後の高さ
resized_img = cv2.resize(img,(width/2, height/2))


cv2.imwrite("resized_hoge.png", resized_img)

# cv2.imshow("img", resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
