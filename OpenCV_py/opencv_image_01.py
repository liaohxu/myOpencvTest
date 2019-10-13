"""
    针对 图片的 基本操作
"""

import cv2
import numpy as np


def get_image_info(src):
    print(type(src)) # 图像数据的类型 -- numpy.ndarray
    print(src.shape) # 图像数据的维度
    print(src.size) # 图像数据中的 元素个数
    print(src.dtype) # 图像数据元素的 数据类型 -- uint8

    print(src)  # 输出 图像数据， 也是 数组的形式

    pict_data = np.array(src) # 将图像数据 以数组的形式 显示
    print(pict_data)


# 读取 图片
src = cv2.imread("../images/m3m.jpg")

# 设置 显示图片的窗口名称“img”， 并且 窗口大小依图片大小自动调整
cv2.namedWindow("img",cv2.WINDOW_AUTOSIZE)

get_image_info(src)

gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY) #将读取的图像数据转换为 灰度图像

"""保存图像，调用 imwrite(‘保存地址’,图片数据)"""
cv2.imwrite("../images/m3m_to_gray.jpg",gray) # 将 灰度图像数据 保存为图片


def show_all(name,wsrc):
    """图片显示 + 关闭图像窗口"""
    cv2.imshow(name,wsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

show_all("img",gray)