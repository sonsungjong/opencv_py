import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image     # pip install pillow
# 화면에 텍스트 및 도형넣기

# 검은화면으로 칠하기
img = np.zeros((512, 512, 3), np.uint8)

# BGR [시작높이:끝높이, 시작가로:끝가로], [:] 전체
img[200:300, 100:300] = 255, 0, 0


# 선 긋기 line(경로, (시작높이, 시작가로), (끝높이, 끝가로), (B,G,R), 두께)
# cv2.line(img, (0,0), (300, 300), (0,255,0), 3)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255, 0, 0), 1)      # 전체 선

# 직사각형 그리기
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2)       # 직사각형... 두께를 cv2.FILLED로 주면 전체색칠

# 원
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)    # 가로, 높이, 반지름

# 한글 폰트입력
fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 20)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((110, 120), "여기에 한글텍스트", font=font, fill=(255,255,255,0))
img = np.array(img_pil)

# 글씨쓰기 putText(경로, "텍스트", (가로,높이), 폰트, 글자크기, (B,G,R), 두께)
cv2.putText(img, " OPENCV ENG", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 150, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)