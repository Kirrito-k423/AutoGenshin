import win32gui
import win32con
import re


def reset_window_pos(targetTitle):
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    print(hWndList)
    for hwnd in hWndList:
        clsname = win32gui.GetClassName(hwnd)
        title = win32gui.GetWindowText(hwnd)
        if(re.match("(.)*nox(.)*", clsname, re.IGNORECASE) or re.match("(.)*nox(.)*", title, re.IGNORECASE)):
            print("~~~~~~~~~~~")
            print(clsname)
            print(title)
    if (title.find(targetTitle) >= 0):  # 调整目标窗口到坐标(600,300),大小设置为(600,600)
        print("find it!")
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600,
                              300, 600, 600, win32con.SWP_SHOWWINDOW)
    else:
        print("not find it!")


reset_window_pos("Nox")
