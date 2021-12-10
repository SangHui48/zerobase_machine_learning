import numpy as np
import cv2

src = cv2.imread('C:/Users/sanghui/Desktop/toyproject/zerobase/zerobase_machine_learning/deeplearning/data/cat.bmp')

aff = np.array([
    [1, 0, 200],
    [0, 1, 100]
], dtype=np.float32)

if src is None:
    print('Image is not loaded!')

dst = cv2.warpAffine(src, aff, (0,0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()