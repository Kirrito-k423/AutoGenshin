# coding=utf-8
import win32gui
import win32con
import win32api
import re
import pyautogui
import time
import xlrd
import pyperclip


def openMap():
    pyautogui.click(clickPosition.x, clickPosition.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")


class gameState:
    power = 0
    remainedDailyTask = 4
    state = 0


class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'position (%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return position(self.x+other.x, self.y+other.y)


def mouseClick(clickTimes, lOrR, img, reTry):
    if reTry == 1:
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes,
                                interval=0.2, duration=0.2, button=lOrR)
                break
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)
    elif reTry == -1:
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes,
                                interval=0.2, duration=0.2, button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes,
                                interval=0.2, duration=0.2, button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)


def reset_window_pos(x, y, reName):
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    # print(hWndList)

    for hwnd in hWndList:
        clsname = win32gui.GetClassName(hwnd)
        title = win32gui.GetWindowText(hwnd)
        if(re.match("(.)*{}(.)*".format(reName), clsname, re.IGNORECASE) or re.match("(.)*{}(.)*".format(reName), title, re.IGNORECASE)):
            print("~~~~~~~~~~~")
            print(clsname)
            print(title)
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            height = bottom - top
            width = right - left
            print("{} {}".format(height, width))
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x,
                                  y, width, height, win32con.SWP_SHOWWINDOW)
            win32gui.BringWindowToTop(hwnd)
            win32gui.SetForegroundWindow(hwnd)


origin = position(100, 100)
shiftMap = position(144, 130)
reName = "模拟器1"
reset_window_pos(origin.x, origin.y, reName)
clickPosition = origin + shiftMap
print(clickPosition)
# # 鼠标定位到(30,50)
# win32api.SetCursorPos([clickPosition.x, clickPosition.y])
# # 执行左单键击，若需要双击则延时几毫秒再点击一次即可
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP |
#                      win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

# 貌似需要预启动，来获取鼠标
pyautogui.click(clickPosition.x, clickPosition.y, clicks=1,
                interval=0.2, duration=0.2, button="left")
# time.sleep(3)

pyautogui.click(clickPosition.x, clickPosition.y, clicks=1,
                interval=0.2, duration=0.2, button="left")
