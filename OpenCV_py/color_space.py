import cv2
import numpy as np


def extrace_object_demo():
    capture = cv2.VideoCapture("../videos/myvideo.mp4")
    while True:
        ret , frame = capture.read()
        if ret == False:
            break

        # 提取视频中 绿色颜色， 通过HSV 方法
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # 根据 HSV颜色分量表 中的最大值，最小值， 提取想要获取的颜色 分量值
        lower_hsv = np.array([35,43,46]) # 绿色h,s,v 分量的最小值
        upper_hsv = np.array([77,255,255]) #绿色h,s,v 分量的最大值

        # 通过 inRange() 方法 实现捕捉 视频中 特定颜色， 参数1： hsv图片数据， 参数2： hsv颜色分量最小值数组， 参数3： hsv颜色分量最大值数组
        cv2.inRange(hsv,lower_hsv,upper_hsv)

        cv2.imshow("video",frame)
        c = cv2.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    """色彩空间转换 API"""
    # BGR --> gray  很重要
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)

    # BGR --> hsv  很重要
    # H -- 范围[0,180]
    # S -- 范围[0,255]
    # V -- 范围[0,255]
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",hsv)

    # BGR --> yuv  很重要
    yuv = cv2.cvtColor(image,cv2.COLOR_BGR2YUV)
    cv2.imshow("yuv",yuv)

    # BGR --> ycrcb
    Ycrcb = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
    cv2.imshow("Ycrcb",Ycrcb)



def base_handle():
    """ 基本操作 """
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread("../images/m2m.jpg",1)
cv2.imshow("src",image)  # 原图像

# 彩色图片通道分离： 通过 split()方法
b,g,r = cv2.split(image)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)



color_space_demo(image)
base_handle()