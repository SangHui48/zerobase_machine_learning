import cv2
import numpy as np

src = cv2.imread('C:/Users/sanghui/Desktop/toyproject/zerobase/zerobase_machine_learning/deeplearning/data/scanned.jpg')

w, h = 720, 400

srcQuad = np.array([360, 345])

cv2.imshow('src', src)

cv2.waitKey()
cv2.destroyAllWindows()