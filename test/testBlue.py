from pydoc import cli
import time
# from globalValue import *
import random
import win32api
import win32con
import win32gui
import win32com.client
import re
# from tsjCommonFunc import *
import pyautogui


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
            # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x,
            #                       y, width, height, win32con.SWP_SHOWWINDOW)
            # win32gui.BringWindowToTop(hwnd)
            # # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
            # shell = win32com.client.Dispatch("WScript.Shell")
            # shell.SendKeys('%')
            # win32gui.SetForegroundWindow(hwnd)


reset_window_pos(100, 100, "lue")
