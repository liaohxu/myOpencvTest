"""
    针对 摄像头，视频的 基础操作
    思路：
        1，创建 视频（摄像头）对象
        2，循环读取 每一帧的数据
        3，显示每一帧的数据
        4，自定义 关闭视频按钮
        5，关闭窗口
"""

# 导入 cv2模块
import cv2


def video_demo():
    """
        针对 摄像头，视频的操作
    :return:
    """
    """打开摄像头，实现视频"""
    capture = cv2.VideoCapture(0) # 创建一个 摄像头对象（读取计算机的摄像头），参数：表示第几个摄像头

    while True: #循环操作
        ret,frame = capture.read()  #通过摄像头 读取内容， 两个返回值： ret- 表示是否连接成功， frame- 表示每一帧的数据

        frame = cv2.flip(frame,1) # 将每一帧的数据进行反转，使得图像能够按正常 方向显示

        cv2.imshow("video",frame) #通过 imshow() 进行展示 参数1：窗口名称， 参数2：每一帧的 数据
        c = cv2.waitKey(50)
        if c == 27: # 表示 当键盘中assice码 是 27(Esc)的时候
            break


def show_all():
    """
        将我们每次要用的 方法进行封装
    :return:
    """
    cv2.waitKey(0) # 表示等待多久关闭窗口， 0：表示按键盘任意键关闭， >0的整数：表示 过多少毫秒 自动关闭
    cv2.destroyAllWindows() # 表示 关闭所有窗口


# 直接调用 函数
video_demo()
show_all()