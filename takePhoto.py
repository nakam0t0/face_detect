# -*- coding: utf-8 -*-
import numpy as np
import cv2
from datetime import date

cap = cv2.VideoCapture(0)
count = 0

while(True):
    # フレームをキャプチャする
    ret, frame = cap.read()

    # 画面に表示する
    cv2.imshow('frame',frame)

    # キーボード入力待ち
    key = cv2.waitKey(1) & 0xFF

    # qが押された場合は終了する
    if key == ord('q'):
        break
    # sが押された場合は保存する
    if key == ord('s'):
        path = "photos/photo" + str(date.today()) + "(" + str(count) + ").jpg"
        cv2.imwrite(path,frame)
        count+=1

# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()
cv2.destroyAllWindows()
