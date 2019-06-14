import cv2
import numpy as np

img = cv2.imread('stairs.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
#edges=cv2.Canny(gray, 80, 120)
minLineLength = 100
maxLineGap = 10
# lines= cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
'''
for line in lines[0]:
    pt1= (line[0], line[1])
    pt2= (line[2], line[3])
    cv2.line(img, pt1, pt2, (0,0,255), 3)
'''
cv2.imwrite('houghlines5.jpg',img)
