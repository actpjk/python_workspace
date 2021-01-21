import time
from PIL import ImageGrab # python 이미지 라이브러리

time.sleep(5) # 5초 사용자 준비 시간

for i in range(1, 11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save('screenshot{}.png'.format(i)) # 파일로 저장
    time.sleep(2)
