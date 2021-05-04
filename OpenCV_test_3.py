import cv2

src = cv2.imread('./OpenCV/test.png')
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV) 


contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in contours :
    hull = cv2.convexHull(i, clockwise=True) #윤곽선에서 블록 껍질을 검출(윤곽선, 방향)
    cv2.drawContours(dst, [hull], 0, (0,0,255), 2)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()