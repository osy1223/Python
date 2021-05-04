import cv2
import numpy as np

'''
img = cv2.imread('./OpenCV/test.png', 0)

kernel = np.ones((5,5), np.uint8)
# result = cv2.erode(src, kernel) => 디폴트
# result = cv2.dilate(src, kernel) => 디폴트
# result = cv2.morphologyEx(src, op, kernel) -> 디폴트
result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#cv2.imshow('Source', img)
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
def morph():
    img = cv2.imread('./OpenCV/alp.jpg', cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread('./OpenCV/a.PNG', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('./OpenCV/b.PNG', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5,5), np.uint8)

    #erosion = cv2.erode(img, kernel)
    #dilation = cv2.dilate(img, kernel)

    #opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    #closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

    grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, kernel)

    #cv2.imshow('original', img)
    #cv2.imshow('ersoion', erosion)
    #cv2.imshow('dilation', dilation)

    cv2.imshow('grad', grad)
    cv2.imshow('tophat', tophat)
    cv2.imshow('blackhat', blackhat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

morph()
'''

def makeKernel():
    M1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    M2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    M3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

    print('M1 : \n', M1)
    print('M2 : \n', M2)
    print('M3 : \n', M3)

makeKernel()