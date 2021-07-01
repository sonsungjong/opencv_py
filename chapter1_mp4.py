import cv2

# 비디오 경로를 읽기
cap = cv2.VideoCapture("Resources/test_video.mp4")

# 비디오 이미지는 시퀀스이므로 각 프레임을 모두 살펴보기위해 imshow를 while문에서 사용
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    # 지연을 추가하고 q라는 키워드를 계속 찾게함
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

