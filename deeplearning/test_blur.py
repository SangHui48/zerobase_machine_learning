import numpy as np
import cv2
import sys

src = cv2.imread('C:/Users/sanghui/Desktop/toyproject/zerobase/zerobase_machine_learning/deeplearning/data/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image is not Found')
    sys.exit()

cv2.imshow('src', src)

for ksize in (3, 5 ,7):
    dst = cv2.blur(src, (ksize, ksize))

    desc = f'Mean : {ksize} x {ksize}'
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyWindow()
