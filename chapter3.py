import cv2
import numpy as np
# 크기변경, 잘라내기

# x축은 오른쪽이 +, y축은 아래쪽이 +
img = cv2.imread("Resources/lambo.png")
print(img.shape)    # (높이, 가로, BGR) 출력

# 사이즈변경 resize(경로, (가로, 높이))
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)    # (높이, 가로, BGR) 출력

# 이미지 잘라내기 [시작높이:끝높이, 시작가로:끝가로]
imgCropped = img[0:200, 200:500]    # img이미지가 높이 0~200, 가로 200~500 만큼 잘림

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)