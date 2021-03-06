import numpy as np
import cv2
import sys
import math
import statistics
from shapely.geometry import LineString
import operator
def main():
    src=cv2.imread('./imagesRGB/RGB133.png')
    #src=cv2.imread('stair4.jpg')
    gray= cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray',gray)
    #gray=cv2.bitwise_not(gray)
    gray=cv2.Sobel(gray, cv2.CV_8U, 0, 1, ksize=5)
    #cv2.imshow("biwise",gray)
    bw=cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    #bw= cv2.inRange(gray,230,255)
    cv2.imshow('binary', bw)
    horizontal=np.copy(bw)
    cols = horizontal.shape[1]
    horizontal_size = cols // 30
    # Create structure element for extracting horizontal lines through morphology operations
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    # Apply morphology operations
    horizontal = cv2.erode(horizontal, horizontalStructure)
    horizontal = cv2.dilate(horizontal, horizontalStructure)
    kernel = np.ones((5,5),np.uint8)
    horizontal= cv2.dilate(horizontal,kernel,iterations=1)
    horizontal= cv2.erode(horizontal,horizontalStructure,iterations=2)
    # Show extracted horizontal lines
    cv2.imshow('horizontal',horizontal)

    '''
    lines= cv2.HoughLinesP(horizontal,1,math.pi/180,1, 150, 50)

    cv2.imshow("horizontal", horizontal)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(src, (x1,y1),(x2,y2),(0,255,0),2)
    '''
    lines=cv2.HoughLines(horizontal,1,math.pi/70,250)
    rhofilter=np.copy(src)
    lines_points = []
    #print(lines.shape)
    if lines is not None:
        lines= np.reshape(lines, [-1,2])
        lines_sorted=lines[lines[:,0].argsort()]
        rho_window=11

        rho_median_arr=[]
        theta_median_arr=[]
        temp_list=[]
        pos=0
        for i in range(0,len(lines_sorted)-1):
            if abs(lines_sorted[i][0] - lines_sorted[i+1][0]) <= rho_window:
                temp_list.append(lines_sorted[i])
            else:
                temp_list.append(lines_sorted[i])
                if len(temp_list) %2 == 0:
                    index = len(temp_list)//2 -1
                else:
                    index = len(temp_list)//2
                rho_median_arr.append(temp_list[index][0])
                theta_median_arr.append(temp_list[index][1])
                del temp_list[:]
        i = len(lines_sorted)-1
        temp_list.append(lines_sorted[i])
        if len(temp_list) %2 == 0:
            index = len(temp_list)//2 -1
        else:
            index = len(temp_list)//2

        rho_median_arr.append(temp_list[index][0])
        theta_median_arr.append(temp_list[index][1])



        for i in range(len(rho_median_arr)):
            rho = rho_median_arr[i]
            theta = theta_median_arr[i]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            lines_points.append([(x1,y1),(x2,y2)])
            cv2.line(rhofilter,(x1,y1),(x2,y2),(0,0,255),2)
            #print(rho,theta)
    cv2.imshow('With filter',rhofilter)
    '''
    no_med=np.copy(src)
    lines=cv2.HoughLines(horizontal,1,math.pi/180,200)
    for value in lines:
        rho = value[0][0]
        theta =value[0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        lines_points.append([(x1,y1),(x2,y2)])
        #cv2.line(no_med,(x1,y1),(x2,y2),(0,0,255),2)
    '''
    col=np.copy(src)
    num_lines= len(lines_points)
    cornerpoints=[]
    final_lines=[]

    i=0
    while i< num_lines:
        C1 = lines_points[i]
        for j in range(i+1,num_lines):
            C2 = lines_points[j]
            line1 = LineString(C1)
            line2 = LineString(C2)
            intersect_point = line1.intersection(line2)
            if intersect_point.type == "Point" and intersect_point.x <= src.shape[1] and intersect_point.x>=0 and intersect_point.y <= src.shape[0] and intersect_point.y >= 0:

                '''
                rho1=lines[i][1][0]
                rho2=lines[j][1][0]
                theta1=lines[i][1][1]
                theta2=lines[j][1][1]
                rho=(rho1+rho2)/2
                theta=(theta1+theta2)/2
                '''
                x1_coord=int((list(line1.coords)[0][0]+list(line2.coords)[0][0])/2)
                y1_coord=int((list(line1.coords)[0][1]+list(line2.coords)[0][1])/2)
                x2_coord=int((list(line1.coords)[1][0]+list(line2.coords)[1][0])/2)
                y2_coord=int((list(line1.coords)[1][1]+list(line2.coords)[1][1])/2)
            #final_lines.append([rho,theta])
                print(i,j)
                cv2.line(col, (x1_coord,y1_coord), (x2_coord, y2_coord),(255,0,0),2)
                i=i+1
                break
            cv2.line(col,(int(list(line1.coords)[0][0]),int(list(line1.coords)[0][1])),(int(list(line1.coords)[1][0]),int(list(line1.coords)[1][1])),(255,0,0),2)
        i=i+1
            #final_lines.append([lines[i][1][0],lines[i][1][1]])


    #cv2.imshow('Without filter',no_med)
    cv2.imshow('Collinear', col)


    final=cv2.bitwise_and(col,col, mask=horizontal)
    cv2.imshow('final',final)

    cv2.waitKey(0)
    return 0

if __name__ == "__main__":
    main()
