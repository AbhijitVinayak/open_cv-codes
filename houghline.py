import cv2
import numpy as np

img = cv2.imread('image.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray= cv2.GaussianBlur(gray, (5,5),0)
#cv2.imshow('blur',gray)
edges = cv2.Canny(gray,15,30,apertureSize = 3)
cv2.imshow('canny',edges)
#edges=cv2.Canny(gray, 80, 120)
# lines= cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1)
lines = cv2.HoughLinesP(edges,rho= 1, theta= np.pi/180,threshold=40,minLineLength=100,maxLineGap=20)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
'''
for line in lines[0]:
    pt1= (line[0], line[1])
    pt2= (line[2], line[3])
    cv2.line(img, pt1, pt2, (0,0,255), 3)'''

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
