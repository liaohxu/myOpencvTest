"""
    图片数据 维度操作
    imgs.shape --> [,,3]  表示 图片的 高， 宽， 通道数
"""

import cv2
import numpy as np


def access_shape(image):
    """操作图片数据的维度，以及数组内的每个元素"""
    print(image.shape) # 图片的大小 维度

    height = image.shape[0] # 图片的高
    width = image.shape[1] # 图片的宽
    channels = image.shape[2] # 图片的 通道数
    print("图片的宽度： {}, 高度： {}, 通道数: {}".format(width,height,channels))

    # 循环获取这个数组的元素
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c] # 将image图片数据的 每一个数 赋值给一个变量
                image[row,col,c] = 255 - pv # 由于像素大小范围从 0-255,所以，用 255分别减去 遍历出来的每一个数值，重新赋值给 原数组对应的位置

    cv2.imshow("new",image)


def create_image():
    """自己创建一个 3通道图片"""
    imge = np.zeros([400,400,3],np.uint8)

    imge[:,:,0] = np.ones([400,400]) * 255 #蓝色
    imge[:,:,1] = np.ones([400,400]) * 255 #绿色
    imge[:,:,2] = np.ones([400,400]) * 255 #红色


def inverse(image):
    """ opencv中 自带api """
    dst = cv2.bitwise_not(image) # 像素取反的 api
    cv2.imshow("dst",dst)


def show_all():
    """将显示，关闭功能封装为函数"""
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 读取图片数据
src = cv2.imread("../images/m1m.jpg")
cv2.imshow("src",src)

# 获取cpu转的圈数
t1 = cv2.getTickCount()

# access_shape(src)
inverse(src)
t2 = cv2.getTickCount()
time = (t2-t1)/cv2.getTickFrequency()
print("转变耗时： {}".format(time))

show_all()



