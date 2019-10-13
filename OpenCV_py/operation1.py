"""
    需求： 图片数组 中的 逻辑运算 【0-255】
    既是: 数组内数据的  与  或  非[ 取反，255-?]
"""

import cv2


def logic_and_demo(m1,m2):
    """
        两个图片数据 逻辑运算  与 ， 调用 bitwise_and() 方法
    """
    dst = cv2.bitwise_and(m1,m2)
    print(dst)
    cv2.imshow("logic_and_demo",dst)


def logic_or_demo(m1,m2):
    """
        两个图片数据 逻辑运算  或 ， 调用 bitwise_or() 方法
    """
    dst = cv2.bitwise_or(m1,m2)
    print(dst)
    cv2.imshow("logic_or_demo",dst)


def logic_not_demo(m1):
    """
        单个图片数据逻辑运算  非【取反，255 - ？】 ， 调用 bitwise_not() 方法
    """
    dst = cv2.bitwise_not(m1)
    print(dst)
    cv2.imshow("logic_not_demo",dst)


def base_handle():
    """ 基本操作 """
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image1 = cv2.imread("../images/m2m.jpg",1)
image2 = cv2.imread("../images/m4m.jpg",1)

print(image1.shape)
print(image2.shape)

cv2.imshow("m2m",image1)
cv2.imshow("m4m",image2)

# 与
logic_and_demo(image1,image2)

# 或
logic_or_demo(image1,image2)

# 非
logic_not_demo(image1)


base_handle()