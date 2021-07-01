import cv2
# 이미지 비디오와 웹캠을 읽는 방법

# cv2.imread로 이미지 파일읽기
img = cv2.imread("Resources/lena.png")

# 표시하려면 imshow
cv2.imshow("Output", img)
# 지연 ms, 0은 무한
cv2.waitKey(0)