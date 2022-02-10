import win32con
import win32gui
import time
import math
# 找出窗体的编号：
QQwin = win32gui . FindWindow("TXGuiFoundation", "QQ")  # 写类和标题，中间逗号隔开
# 控制窗体的位置和大小：
while True:
    SE = 0.0  # 弧度
    while SE - 3.1415926535 * 2 < 0.0000001:  # 浮点数运算存在误差
        time.sleep(0.1)
        SE += 0.1
        newx = int(400+400*math.cos(SE))  # 圆心加半径
        newy = int(400+400*math.sin(SE))  # 圆心加半径
        win32gui.SetWindowPos(QQwin, win32con.HWND_TOPMOST, newx,
                              newy, 600, 600, win32con.SWP_SHOWWINDOW)
