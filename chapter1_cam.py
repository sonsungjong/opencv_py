import cv2

# VideoCapture() 에 웹캠ID를 입력
webcam = cv2.VideoCapture(0)
# 가로
webcam.set(3, 640)
# 세로
webcam.set(4, 480)
# 밝기를 100으로
webcam.set(10, 100)

while True:
    success, img = webcam.read()
    cv2.imshow("MyWebCam!", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ver3.7.9