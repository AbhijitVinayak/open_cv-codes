import cv2
import numpy as np

global PI
PI=3.141592654

bounding_box=None

class StairDetectorGeoParams:
    def __init__(self):
        # High level bools
        self.show_result= False
        self.debug= False
        self.ignore_invalid= False
        self.fill_invalid= False
        self.use_laplacian= False
        #canny
        self.canny_low_threshold=40
        self.canny_ratio=10
        self.canny_kernel_size=1
        #hough transform
        self.hough_min_line_length=25
        self.hough_max_line_gap=15
        self.hough_threshold=20
        self.hough_rho=8
        self.hough_theta=1
        #filter by slope histogram
        self.filter_slope_hist_bin_width=20
        #filter by hard slope
        self.filter_slope_bandwidth=10
        #merge parameters
        self.merge_max_dist_diff=20
        self.merge_max_angle_diff=30
        self.merge_close_count=10
        #bounding box
        self.minimum_line_num=3

class StairDetectorGeo:
    def __init__(self,input_image):
        self.param=StairDetectorGeoParams()
        self.param_=StairDetectorGeoParams()
        self.lines=Lines()
        setParam(self.param)
        self.tmp_bounding_box=None
        self.input_image=input_image
    def getStairs(bounding_box,param):
        self.src_gray=self.input_image.copy()
        if len(input_image.shape) == 2:
            min=min(self.src_gray)
            max=max(self.src_gray)
            max=cv2.convertScaleAbs(src_gray, src_gray, 255/max)
            if param_.fill_invalid :
                fillByNearestNeighbour(src_gray, src_gray)
            src_rgb=cv2.cvtColor(src_gray, cv2.COLOR_GRAY2RGB)
        else:
            print("Must use grayscale depth image as input ")
            return False
        if param_.use_laplacian :
            laplacianEdgeDetection(src_gray, edge)
        else:
            edge=cannyEdgeDetection(src_gray)
        if param_.ignore_invalid:
            edge=ignoreInvalid(src_gray)
        if param_.debug:
            cv2.imshow("edge image", edge)

        self.lines=houghLine(edge)

        if getBoundingBox(src_rgb, lines, self.tmp_bounding_box):
            if param_.debug:
                print("Found stairs")
            bounding_box= self.tmp_bounding_box
            return True
        else:
            bounding_box.clear()
            return False
    def setParam(param):
        self.param_=self.param
        self.param_.merge_max_angle_diff= self.param_.merge_max_angle_diff*PI/180
        self.param_.filter_slope_bandwidth = self.param_.filter_slope_bandwidth * PI / 180
        self.param_.hough_theta = self.param_.hough_theta * PI / 180
        self.param_.filter_slope_hist_bin_width = self.param_.filter_slope_hist_bin_width * PI / 180
        self.param_.canny_kernel_size = self.param_.canny_kernel_size * 2 + 1
        if self.param_.canny_kernel_size>7:
            self.param_.canny_kernel_size=7
        if self.param_.canny_kernel_size<1:
            self.param_.canny_kernel_size=1
    def drawLines(image, lines):
        for i in range(lines.size()):
            cv2.line(image,lines[i].p1, lines[i].p2, (255,0,0),3,8)

    def drawLinesSlope(image, lines ):
        for i in range(lines.size()):
            putText(image, str(lines[i].t))

def main():
    param= StairDetectorGeoParams()

if __name__= '__main__':
    main()
