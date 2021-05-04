import numpy as np
import cv2

'''
#color설정
blue_color = (255,0,0)
green_color = (0,255,0)
red_color = (0,0,255)
white_color = (255,255,255)

#모두 0으로 되어 있는 빈 Canvas(검정색)
img = np.zeros((384, 384, 3), np.uint8)
'''

'''
#polylines() 테스트

#점,좌표 설정
points1 = np.array([[10,10], [170,10], [20,230]], np.int32)
points2 = np.array([[110,110], [270,110], [300,330]], np.int32)

#그리기
#img = cv2.polylines(img, pts, isClosed, color) -> 디폴트
img = cv2.polylines(img, [points1], False, blue_color, 2) #열린 도형
img = cv2.polylines(img, [points2], True, green_color, 2) #닫힌 도형

cv2.imshow('polylines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#fillConvexPoly() 테스트
#점 좌표 설정
pt1 = np.array([[110,110], [27,110], [300,330], [170,350]], np.int32)

#블록 다각형 그리기
#img = cv2.fillConvexPoly(img, points, color) -> 디폴트
img = cv2.fillConvexPoly(img, pt1, white_color)

cv2.imshow('fillConvexPoly', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
# 점 좌표 설정
pt1 = np.array([[110,110], [270,110], [300,330], [170,170], [150,250]], np.int32)
points2 = np.array([[110,110], [270,110], [300,330]], np.int32)

# 오목 다각형 그리기
img = cv2.fillConvexPoly(img, pt1, white_color)
img = cv2.polylines(img, [points2], True, green_color, 2) #닫힌 도형

cv2.imshow('polylines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# create a black image
img = np.zeros((512,512,3), np.uint8)

# line()
#img = cv2.line(img, (0,0), (511,511), (255,0,0), 5)

# rectangle()
#img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

# circle()
#img = cv2.circle(img, (447,63), 63, (0,0,255), -1)

# ellipse
#img = cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color) -> 디폴트
#img = cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

# polylines
#pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
#img = cv2.polylines(img,[pts],False,(0,255,255))

# font
#font = cv2.FONT_HERSHEY_COMPLEX
#cv2.putText(img, text, org, fontFace, fontScale, color) -> 디폴트값
#cv2.putText(img, "Hello", (10,500), font, 2, (255,255,255), 2, cv2.LINE_AA)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,0),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hello OpenCV!!!',(10,500), font, 2, (255,255,255), 2, cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
