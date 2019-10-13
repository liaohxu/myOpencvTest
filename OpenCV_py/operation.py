"""
    需求： 图片数组 中的 算术运算 【0-255】
    既是: 数组内数据的  + - × /
"""

import cv2


def add_demo(m1,m2):
    """
        两个图片数据相加， 调用 add() 方法， 范围[0-255],越界值：取 255
    """
    dst = cv2.add(m1,m2)
    print(dst)
    cv2.imshow("add_demo",dst)


def subtract_demo(m1,m2):
    """
        两个图片数据相减， 调用 subtract() 方法， 范围[0-255]，越界值：取 0
    """
    dst = cv2.subtract(m1,m2)
    print(dst)
    cv2.imshow("subtract_demo",dst)


def multiply_demo(m1,m2):
    """
        两个图片数据相除， 调用 multiply() 方法， 范围[0-255]，越界值：取 255
    """
    dst = cv2.multiply(m1,m2)
    print(dst)
    cv2.imshow("multiply",dst)


def divide_demo(m1,m2):
    """
        两个图片数据相除， 调用 divide() 方法， 范围[0-255]，越界值：取 0
    """
    dst = cv2.divide(m1,m2)
    print(dst)
    cv2.imshow("divide_demo",dst)


def other(m1,m2):
    """
        求两个图片 均值，方差 调用 mean()只求均值， meanStdDev()可同时得到 均值 和 方差
    """
    M1, dev1 = cv2.meanStdDev(m1)
    M2, dev2 = cv2.meanStdDev(m2)

    # 均值
    print(M1)
    print(M2)

    # 方差
    print(dev1)
    print(dev2)


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

# 算术相加
add_demo(image1,image2)

# 算术相减
subtract_demo(image1,image2)

# 算术相乘
multiply_demo(image1,image2)

# 算术相除
divide_demo(image1,image2)

# 均值和 方差
other(image1,image2)


base_handle()