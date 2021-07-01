import cv2
import numpy as np
# 이미지 선변경

# 이미지 경로읽기 imread, 비디오 경로읽기 VideoCapture
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5), np.uint8)

# BGR 로 색상변경 cvtColor
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# 화면에 표시 imshow
cv2.imshow("Origin", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dialation", imgDialation)
cv2.imshow("Erode", imgEroded)

cv2.waitKey(0)