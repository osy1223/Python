import numpy as np
import cv2

# 영상 불러오기
src = cv2.imread('./OpenCV/test1.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('image load failed!')
    sys.exit()
    
# 필터 마스크 생성
kernel = np.ones((3, 3), dtype=np.float64) / 9. # 9.이 실수이므로 자동으로 float로 설정되지만 데이터 타입을 지정해주었습니다.
dst = cv2.filter2D(src, -1, kernel) # -1은 입력 영상과 동일한 데이터의 출력 영상 생성

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()