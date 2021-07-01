import cv2
import numpy as np
# 이미지 결합

img = cv2.imread('Resources/lena.png')

horizontal = np.hstack((img, img))  # 가로로 합치기
vertical = np.vstack((img, img))    # 세로로 합치기

cv2.imshow("Horizontal", horizontal)
cv2.imshow("Vertical", vertical)

cv2.waitKey(0)