import win32con
import win32gui
# 找出窗体的编号：
QQwin = win32gui . FindWindow("TXGuiFoundation", "QQ")  # 写类和标题，中间逗号隔开
# 控制窗体的位置和大小：
win32gui.SetWindowPos(QQwin, win32con.HWND_TOPMOST, 100,
                      100, 600, 600, win32con.SWP_SHOWWINDOW)
