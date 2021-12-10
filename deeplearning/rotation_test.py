import numpy as np
import cv2
import math

src = cv2.imread('C:/Users/sanghui/Desktop/toyproject/zerobase/zerobase_machine_learning/deeplearning/data/rose.bmp')

rad = 20 * math.pi / 180
aff = np.array([
    [math.cos(rad), math.sin(rad), 0],
    [-math.sin(rad), math.cos(rad), 0]
], dtype=np.float32)

cp = (src.shape[1]/ 2, src.shape[0] / 2)
rot = cv2.getRotationMatrix2D(cp, 20, 1)

dst = cv2.warpAffine(src, aff, (0,0))
dst2 = cv2.warpAffine(src, rot, (0,0))
cv2.imshow('src',src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst)

cv2.waitKey()
cv2.destroyAllWindows()