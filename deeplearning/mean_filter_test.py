import cv2
import numpy as np

img = cv2.imread('C:/Users/sanghui/Desktop/toyproject/zerobase/zerobase_machine_learning/deeplearning/data/rose.bmp', cv2.IMREAD_GRAYSCALE)

kernel = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

dst = cv2.filter2D(img, -1, kernel)
dst_blur = cv2.blur(img, (3, 3))

cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.imshow('dst_blur', dst_blur)

cv2.waitKey()

cv2.destroyAllWindows()