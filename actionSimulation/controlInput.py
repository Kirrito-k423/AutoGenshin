from pydoc import cli
import time
from globalValue import *
import random
import win32api
import win32con
import win32gui
import win32com.client
import re
from tsjCommonFunc import *
import pyautogui


def reset_window_pos(x, y, reName):
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    # print(hWndList)
    count=0
    for hwnd in hWndList:
        clsname = win32gui.GetClassName(hwnd)
        title = win32gui.GetWindowText(hwnd)
        if(re.match("(.)*{}(.)*".format(reName), clsname, re.IGNORECASE) or re.match("(.)*{}(.)*".format(reName), title, re.IGNORECASE)):
            count+=1
            print("~~~~~~~~~~~")
            print(clsname)
            print(title)
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            height = bottom - top
            width = right - left
            print("y {} x {}".format(height, width))
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x,
                                  y, width, height, win32con.SWP_SHOWWINDOW)
            win32gui.BringWindowToTop(hwnd)
            # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(hwnd)
    if count==0:
        return 0
    else:
        return 1


def keyExit():
    input = [['Esc', 1, const.shortPress]]
    key_input(input)


def randomShift(pixel):
    return position(random.randint(-pixel, pixel), random.randint(-pixel, pixel))

# 输入文字VK_CODE[word]为要输入的文字码


def jumpDownFunc():
    win32api.keybd_event(VK_CODE[jumpDown], 0, 0, 0)  # 按下键
    win32api.keybd_event(
        VK_CODE[jumpDown], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
    sleepRandom(0.3)


def fly(times, interval, direction):
    colorPrint("fly {}".format(times), "yellow")
    while times:
        win32api.keybd_event(VK_CODE[direction], 0, 0, 0)  # 按下键
        win32api.keybd_event(VK_CODE[jump], 0, 0, 0)  # 按下键
        sleepRandom(0.3)
        win32api.keybd_event(
            VK_CODE[jump], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        sleepRandom(0.3)
        win32api.keybd_event(VK_CODE[jump], 0, 0, 0)  # 按下键
        sleepRandom(0.3)
        win32api.keybd_event(
            VK_CODE[jump], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        sleepRandom(0.3+interval)
        win32api.keybd_event(
            VK_CODE[direction], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        times -= 1


def goBack():
    jumpDownFunc()
    fly(3, 2, backward)
    fly(3, 3, right)


def key_input(input_words,    interval=1):
    sleepRandom(interval)
    for word in input_words:
        print("key {}".format(word[0]))
        if word[2] == const.shortPress:
            tmp = word[1]
            while tmp:
                print("shortTimes {}".format(tmp))
                win32api.keybd_event(VK_CODE[word[0]], 0, 0, 0)  # 按下键
                sleepRandom(0.1)
                win32api.keybd_event(
                    VK_CODE[word[0]], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
                sleepRandom(interval)
                tmp -= 1
        elif word[2] == const.longPress:
            win32api.keybd_event(VK_CODE[word[0]], 0, 0, 0)  # 按下键
            time.sleep(word[1])
            win32api.keybd_event(
                VK_CODE[word[0]], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
            sleepRandom(interval)


def clickAbsolute(absolutePos):
    print(absolutePos)
    sleepRandom(1)
    absolutePos = absolutePos + randomShift(5)
    pyautogui.click(absolutePos.x, absolutePos.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")
    mouseMoveAway()


def quickClickAbsolute(absolutePos):
    print(absolutePos)
    sleepRandom(0.5)
    absolutePos = absolutePos + randomShift(5)
    pyautogui.click(absolutePos.x, absolutePos.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")
    mouseMoveAway()


def clickShift(shiftPos):
    clickPosition = origin + shiftPos
    print(clickPosition)
    sleepRandom(1)
    clickPosition = clickPosition + randomShift(15)
    pyautogui.click(clickPosition.x, clickPosition.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")
    mouseMoveAway()


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


def randomDragMode():
    modenum = random.randint(0, 4)
    mode = [pyautogui.easeInQuad,
            pyautogui.easeOutQuad,
            pyautogui.easeInOutQuad,
            pyautogui.easeInBounce,
            pyautogui.easeInElastic]
    return mode[modenum]


def moveScreen(moveDirection, dragtime=1):
    # print(moveDirection)
    beginPos = mainpageCenter - moveDirection
    finalPos = mainpageCenter + moveDirection
    # 800,900表示鼠标拖拽的起始位置，0.2设置鼠标移动快慢
    dragtime = Random(dragtime)
    dragmode = randomDragMode()
    pyautogui.moveTo(beginPos.x, beginPos.y, 0.1)
    # 200,200表示鼠标拖拽的终点位置，0.2设置鼠标拖拽的快慢，“easeOutQuad”表示鼠标拖动先快后慢（多种拖拽方式可选）
    pyautogui.dragTo(finalPos.x, finalPos.y, dragtime, dragmode)


def mouseClear():
    clickShift(shiftCenter)
    pyautogui.moveTo(1, 1, 0.1)


def mouseMoveAway():
    pyautogui.moveTo(1, 1, 0.1)
