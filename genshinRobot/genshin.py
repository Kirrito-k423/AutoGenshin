# coding=utf-8
from pydoc import cli
from typing import final
import win32gui
import win32con
import win32api
import win32com.client
import re
import pyautogui
import time
import random
import ctypes
import sys
import xlrd
import pyperclip
from globalValue import *


def keyExit():
    time.sleep(2)
    input = [['Esc', 1, const.shortPress]]
    key_input(input)


def sleepRandom(seconds):
    time.sleep(round(random.uniform(0, seconds), 2))


def randomShift(pixel):
    return position(random.randint(-pixel, pixel), random.randint(-pixel, pixel))

# 输入文字VK_CODE[word]为要输入的文字码


def key_input(input_words):
    sleepRandom(1)
    for word in input_words:
        print("key {}".format(word[0]))
        if word[2] == const.shortPress:
            while word[1]:
                win32api.keybd_event(VK_CODE[word[0]], 0, 0, 0)  # 按下键
                win32api.keybd_event(
                    VK_CODE[word[0]], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
                sleepRandom(1)
                word[1] -= 1
        elif word[2] == const.longPress:
            win32api.keybd_event(VK_CODE[word[0]], 0, 0, 0)  # 按下键
            time.sleep(word[1])
            win32api.keybd_event(
                VK_CODE[word[0]], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
            sleepRandom(1)


def click(shiftPos):
    clickPosition = origin + shiftPos
    print(clickPosition)
    sleepRandom(1)
    clickPosition = clickPosition + randomShift(15)
    pyautogui.click(clickPosition.x, clickPosition.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")


def openMap():
    click(shiftMap)


# def mouseMove(shift):

def mouseMove(x, y):
    sleepRandom(1)
    centerPos = origin + shiftCenter + randomShift(15)
    moveDirection = position(x, y) + randomShift(15)
    beginPos = centerPos - moveDirection
    finalPos = centerPos + moveDirection
    print(centerPos)
    # 800,900表示鼠标拖拽的起始位置，0.2设置鼠标移动快慢
    pyautogui.moveTo(beginPos.x, beginPos.y, 0.2)
    # 200,200表示鼠标拖拽的终点位置，0.2设置鼠标拖拽的快慢，“easeOutQuad”表示鼠标拖动先快后慢（多种拖拽方式可选）
    pyautogui.dragTo(finalPos.x, finalPos.y, 2, pyautogui.easeOutQuad)
    # pyautogui.click(centerPos.x, centerPos.y)  # 鼠标移动到
    # ctypes.windll.user32.SetCursorPos(
    #     centerPos.x, centerPos.y)  # Mouse moves to
    # pyautogui.dragRel(x, y)  # drag mouse 10 pixels down
    # moveDirection = position(x, y) + randomShift(15)
    # time.sleep(3)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,
    #                      0, 0, 0, 0)  # 左键按下
    # sleepRandom(0.5)
    # win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE +
    #                      win32con.MOUSEEVENTF_MOVE, moveDirection.x, moveDirection.y, 0, 0)
    # sleepRandom(0.5)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,
    #                      0, 0, 0, 0)
# def mouseMove(x, y):
#     sleepRandom(1)
#     centerPos = origin + shiftCenter + randomShift(15)
#     print(centerPos)
#     win32api.SetCursorPos([centerPos.x, centerPos.y])  # 鼠标移动到
#     moveDirection = position(x, y) + randomShift(15)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,
#                          centerPos.x, centerPos.y, 0, 0)  # 左键按下
#     sleepRandom(0.5)
#     # win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE +
#     #                      win32con.MOUSEEVENTF_MOVE, moveDirection.x, moveDirection.y, 0, 0)
#     finalPos = centerPos + moveDirection
#     sleepRandom(0.5)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,
#                          finalPos.x, finalPos.y, 0, 0)


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
            # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(hwnd)
            return 0
    return 1


def receiveJob(jobID):
    click(shiftJobIcon)
    click(shiftJobClassIcon[jobID])
    click(shiftAccIcon)


def test():
    # 攻击测试
    # input = [['Spacebar', 1, const.shortPress], ['E', 4, const.longPress]]
    # key_input(input)

    # 地图操作
    # openMap()
    # keyExit()

    # 视角移动
    # mouseMove(100, 0)

    # 接取任务
    receiveJob(const.worldJob)


if __name__ == '__main__':
    if reset_window_pos(origin.x, origin.y, regexName):
        print("not found process! over")
        sys.exit()

    test()

    # # 鼠标定位到(30,50)
    # win32api.SetCursorPos([clickPosition.x, clickPosition.y])
    # # 执行左单键击，若需要双击则延时几毫秒再点击一次即可
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP |
    #                      win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    # 貌似需要预启动，来获取鼠标
    # pyautogui.click(clickPosition.x, clickPosition.y, clicks=1,
    # interval=0.2, duration=0.2, button="left")
    # time.sleep(3)

    # pyautogui.click(clickPosition.x, clickPosition.y, clicks=1,
    #                 interval=0.2, duration=0.2, button="left")
