"""
    ROI ： 感兴趣区域
    需求： 实现彩色图片 ROI区域 的灰度显示
           泛洪填充
"""

import cv2
import numpy as np

def fill_color_demo(image):
    """
        彩色图像 漫水填充 算法
    """
    copyImg = image.copy()  # 先拷贝一份
    h,w = image.shape[:2]  # 获取图像 的 高，宽

    # 构建一个掩码层[全 0矩阵]， 如果想要 全图掩码，则必须比原图 上下左右分别大 1，也就是 h+2, w+2 【该掩码层 是个 二维矩阵 单通道，不用 3通道】
    mask = np.zeros([h+2,w+2],np.uint8)

    # 漫水填充 算法
    # 参数1： 想要填充的图层， 参数2： 掩码层， 参数3： 种子点（以哪个像素值为参照）
    # 参数4： 填充颜色（rgb）， 参数5： 以种子点的像素值 为参照 的 下限值，
    # 参数6： 以种子点的像素值 为参照的 上限值， 参数7： 填充方法
    cv2.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv2.FLOODFILL_FIXED_RANGE)

    cv2.imshow("fill_color_demo",copyImg)


def fill_binary():
    """
        自定义纯白图片 填充【二值化填充】
    """
    # 初始化构建一个 全0矩阵， 一个纯黑色图片
    image = np.zeros([400,400,3],np.uint8)
    # 将ROI区域 变成 白色
    image[100:300,100:300,:] = 255
    cv2.imshow("creat_image",image)

    # 构建一个掩码【全 1 单通道矩阵】
    mask = np.ones([402,402],np.uint8)
    # 将 掩码 正中间区域 变成 黑色
    mask[101:301,101:301] = 0

    # 使用 漫水填充算法  只填充 掩码区域内容
    cv2.floodFill(image,mask,(200,200),(0,0,255),cv2.FLOODFILL_MASK_ONLY)
    cv2.imshow("filled_binary",image)


def base_handle():
    """ 基本操作 """
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread("../images/m2m.jpg",1)
cv2.imshow("src",image)  # 原图像

"""
# 获取 ROI区域， 高：50:250,  宽：200:350
face = image[50:250,200:350]
gray = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) # 将 ROI区域转换为 灰度图像

# 将灰度图像 重新放回 彩色图片的区域中， 得通过 通道转换，1 --> 3
backgray = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR) # 灰度图像 变成 3 通道 ，还是灰色图像
image[50:250,200:350] = backgray # 将已经是灰度图像的 ROI区域，与彩色图片融合

cv2.imshow("face",image)
"""
# fill_color_demo(image)

fill_binary()
base_handle()





