# coding=utf-8
from pydoc import cli
from sre_parse import State
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
import math
import pytesseract
import easyocr
from termcolor import colored
import os


def errorPrint(message):
    os.system('color')
    print(colored(message, 'red'))


def colorPrint(message, color):
    os.system('color')
    print(colored(message, color))


def passPrint(message):
    os.system('color')
    print(colored(message, 'green'))


def completePrint(message):
    os.system('color')
    print("--------------------------------{}--------------------------------".format(colored(message, 'green')))


def keyExit():
    time.sleep(2)
    input = [['Esc', 1, const.shortPress]]
    key_input(input)


def sleepRandom(seconds):
    time.sleep(round(random.uniform(0, seconds), 2))


def randomShift(pixel):
    return position(random.randint(-pixel, pixel), random.randint(-pixel, pixel))

# 输入文字VK_CODE[word]为要输入的文字码


def jumpDownFunc():
    win32api.keybd_event(VK_CODE[jumpDown], 0, 0, 0)  # 按下键
    win32api.keybd_event(
        VK_CODE[jumpDown], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
    sleepRandom(0.3)


def fly(times, interval, direction):
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
        sleepRandom(interval)
        win32api.keybd_event(
            VK_CODE[direction], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        times -= 1


def key_input(input_words):
    interval = 1
    sleepRandom(interval)
    for word in input_words:
        print("key {}".format(word[0]))
        if word[2] == const.shortPress:
            while word[1]:
                win32api.keybd_event(VK_CODE[word[0]], 0, 0, 0)  # 按下键
                win32api.keybd_event(
                    VK_CODE[word[0]], 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
                sleepRandom(interval)
                word[1] -= 1
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
    time.sleep(2)


def quickClickAbsolute(absolutePos):
    print(absolutePos)
    sleepRandom(0.5)
    absolutePos = absolutePos + randomShift(5)
    pyautogui.click(absolutePos.x, absolutePos.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")


def clickShift(shiftPos):
    clickPosition = origin + shiftPos
    print(clickPosition)
    sleepRandom(1)
    clickPosition = clickPosition + randomShift(15)
    pyautogui.click(clickPosition.x, clickPosition.y, clicks=1,
                    interval=0.2, duration=0.2, button="left")
    time.sleep(2)


def openMap():
    splitLine("openMap")
    clickShift(shiftMap)
    waitPageChangeTo("map")


def openJobPage():
    splitLine("openJobPage")
    clickShift(shiftJobIcon)
    waitPageChangeTo("jobPage")


def exitJobPage():
    splitLine("exitJobPage")
    keyExit()
    waitPageChangeTo("mainPage")


def back2mainPage():
    splitLine("back2mainPage")
    while getState() != "mainPage":
        keyExit()
        print("back2mainPage…………")
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
    clickShift(shiftJobIcon)
    clickShift(shiftJobClassIcon[jobID])
    clickShift(shiftAccIcon)


def checkPicExists(Img, region, confidence):
    # ,region 4-integer tuple of (left, top, width, height))
    location = pyautogui.locateCenterOnScreen(
        Img, region=region, confidence=confidence)
    if location is not None:
        print("{} is Existed ({},{})".format(Img, location.x, location.y))
    else:
        print("{} is NOT Existed".format(Img))
    return location


def checkInfo(type):
    if type == const.checkJobReceived:
        return checkPicExists(checkJobReceivedImg, checkJobReceivedRegion, 0.6)


def jobMapEdgeRegion(part):
    if part == "left":
        left = jobMapLeft-jobMapSearchHalfWidth
        top = jobMapTop - jobMapSearchHalfWidth
        width = 2*jobMapSearchHalfWidth
        height = 2*jobMapSearchHalfWidth + jobMapBottom-jobMapTop
        return (left, top, width, height)
    elif part == "right":
        left = jobMapRight-jobMapSearchHalfWidth
        top = jobMapTop - jobMapSearchHalfWidth
        width = 2*jobMapSearchHalfWidth
        height = 2*jobMapSearchHalfWidth + jobMapBottom-jobMapTop
        return (left, top, width, height)
    elif part == "top":
        left = jobMapLeft-jobMapSearchHalfWidth
        top = jobMapTop - jobMapSearchHalfWidth
        width = 2*jobMapSearchHalfWidth + jobMapRight - jobMapLeft
        height = 2*jobMapSearchHalfWidth
        return (left, top, width, height)
    elif part == "bottom":
        left = jobMapLeft-jobMapSearchHalfWidth
        top = jobMapBottom - jobMapSearchHalfWidth
        width = 2*jobMapSearchHalfWidth + jobMapRight - jobMapLeft
        height = 2*jobMapSearchHalfWidth
        return (left, top, width, height)
    elif part == "center":
        return centerRegion
    elif part == "realCenter":
        return realCenterRegion


def checkJobIconMapPosition(direction):
    if direction == "center" or direction == "realCenter":
        location = checkPicExists(
            jobMapImg2, jobMapEdgeRegion(direction), 0.7)
    else:
        location = checkPicExists(jobMapImg, jobMapEdgeRegion(direction), 0.9)
    if location is not None:
        print("jobIcon is in {} ({},{})".format(
            direction, location.x, location.y))
    return location


def getJobIconMapPosition():
    direction = ["right", "bottom", "left", "top"]
    location = None
    i = 0
    isJobIconInEdge = "edge"
    while location is None and i < len(direction):
        location = checkJobIconMapPosition(direction[i])
        i += 1
    if location is None:
        print("jobIcon is NOT in Edge")
        location = checkJobIconMapPosition("center")
        if location is None:
            print("jobIcon is NOT Finded!!!")
            return [None, "None"]
        else:
            centerLoc = checkJobIconMapPosition("realCenter")
            if centerLoc is None:
                isJobIconInEdge = "outCenter"
            else:
                isJobIconInEdge = "realCenter"
                location = centerLoc
    return [location, isJobIconInEdge]


def scaleXY(x, y):
    bigX = scale.x
    bigY = scale.y
    scaleX = bigX/abs(x)
    scaleY = bigY/abs(y)
    if scaleX > scaleY:
        return scaleY
    else:
        return scaleX


def dragMap(x, y, isScale):
    sleepRandom(1)
    moveDirection = position(-0.5*x, -0.5*y) + randomShift(50)
    print(moveDirection)
    if isScale:
        scaleNum = scaleXY(moveDirection.x, moveDirection.y)
        print(scaleNum)
        moveDirection = 0.5*scaleNum * moveDirection
    print(moveDirection)
    beginPos = mainpageCenter - moveDirection
    finalPos = mainpageCenter + moveDirection
    # 800,900表示鼠标拖拽的起始位置，0.2设置鼠标移动快慢
    pyautogui.moveTo(beginPos.x, beginPos.y, 0.2)
    # 200,200表示鼠标拖拽的终点位置，0.2设置鼠标拖拽的快慢，“easeOutQuad”表示鼠标拖动先快后慢（多种拖拽方式可选）
    pyautogui.dragTo(finalPos.x, finalPos.y, 2, pyautogui.easeOutQuad)


def moveMapforJobIcon():
    trytime = 3
    isJobIconInEdge = "edge"
    while isJobIconInEdge == "edge" or isJobIconInEdge == "outCenter"\
            or isJobIconInEdge == "None":
        [location, isJobIconInEdge] = getJobIconMapPosition()
        if location is not None and isJobIconInEdge == "realCenter":
            return location
        if location is None and isJobIconInEdge == "None":
            # 找不到随机就行
            if trytime > 0:
                trytime -= 1
                location = position(
                    mainpageCenter.x, mainpageCenter.y+100)+randomShift(200)
            else:
                return None
        location = position(location.x, location.y)
        moveDirection = location - mainpageCenter
        if isJobIconInEdge == "outCenter":
            isScale = 0
        else:
            isScale = 0

        print("direction ({},{})".format(moveDirection.x, moveDirection.y))
        dragMap(moveDirection.x, moveDirection.y, isScale)


def posDistance(a, b):
    return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y)


def splitLine(string):
    print("\n")
    print("--------------------------------{}--------------------------------".format(string))
    print("\n")


def getNearestTransport(targetPosition):
    splitLine("getNearestTransport")
    print(targetPosition)
    ans = 2*quarterMainPageHeight
    # Returns a generator that yields (left, top, width, height) tuples for where the image is found on the screen.
    for i in pyautogui.locateAllOnScreen(
            transportImg, region=centerRegion, confidence=0.9):
        x = i[0]+0.5*i[2]
        y = i[1]+0.5*i[3]
        transportlocation = position(x, y)
        print(transportlocation)
        if(posDistance(transportlocation, targetPosition) < posDistance(ans, targetPosition)):
            ans = transportlocation
            print(ans)
    if ans == 2*quarterMainPageHeight:
        return None
    else:
        return ans


def transPort(transportPosition):
    splitLine("transportPosition")
    clickAbsolute(transportPosition)
    transportAccLocation = pyautogui.locateCenterOnScreen(
        transportAccImg, region=transportAccRegion, confidence=0.8)
    if transportAccLocation is not None:
        clickShift(shiftAccIcon)
        return 0
    else:
        transportTextLocation = pyautogui.locateCenterOnScreen(
            transportTextImg, region=transportTextRegion, confidence=0.9)
    if transportTextLocation is None:
        print("no transPort showed?!")
        return -1
    else:
        clickAbsolute(position(transportTextLocation.x,
                               transportTextLocation.y))
        clickShift(shiftAccIcon)
        return 0


def isAttack():
    splitLine("isAttack")
    jobLoc = None
    while jobLoc is None:
        jobLoc = checkInfo(const.checkJobReceived)
        awakeJob()
    im = pyautogui.screenshot(region=(jobLoc.x+15, jobLoc.y-13, 140, 26))
    im.save('./tmp/isAttack.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/isAttack.png')
    print(text)
    passPrint(text[0][1])
    if re.search(r"(解救)|(保护)|(击败)", text[0][1]) is not None:
        return 1
    else:
        return 0


def fourBigSkills():
    # three other gui
    quickClickAbsolute(absolutePerson1Skill)
    quickClickAbsolute(absolutePerson2Skill)
    quickClickAbsolute(absolutePerson3Skill)


def changePerson(num):
    quickClickAbsolute(absolutePerson[num-1])


def combo():
    input = [[attackIcon, 5, const.shortPress],
             [smallSkills, 1, const.longPress],
             [attackIcon, 5, const.shortPress]]
    key_input(input)


def Attack(num):
    colorPrint("塔塔开！！！", "yellow")
    combo()
    fourBigSkills()
    combo()
    changePerson(num)
    fly(1, 1, forward)


def isFindSomeNearDialog():
    splitLine("isFindSomeNearDialog")
    jobLoc = None
    while jobLoc is None:
        jobLoc = checkInfo(const.checkJobReceived)
        awakeJob()
    im = pyautogui.screenshot(region=(jobLoc.x+15, jobLoc.y-13, 140, 26))
    im.save('./tmp/isFindSomeNearDialog.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/isFindSomeNearDialog.png')
    print(text)
    passPrint(text[0][1])
    if re.search(r"(对话)|(寻找)", text[0][1]) is not None:
        return 1
    else:
        return 0


def findSomeNear():
    while dialogBoxShowed():
        fly(1, 1, forward)
    dialog()


def toDoTask():
    while isAttack():
        trytime = 3
        while trytime > 0:
            Attack(trytime)
            trytime -= 1
    while isFindSomeNearDialog():
        findSomeNear()


def jobDistanceFromMainPage():
    splitLine("jobDistanceFromMainPage")
    jobLoc = checkInfo(const.checkJobReceived)
    im = pyautogui.screenshot(region=(jobLoc.x+15, jobLoc.y+13, 140, 70))
    im.save('./tmp/jobDistanceFromMainPage.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/jobDistanceFromMainPage.png')
    print(text)
    if text != []:
        passPrint(text[0][1])
        if re.search(r"\d+", text[0][1]) is not None:
            return int(re.search(r"\d+", text[0][1]).group())
        elif re.search(r"(到达)|(区域)", text[0][1]) is not None:
            completePrint("Get Position！")
            return -1
    reader = easyocr.Reader(['en'])
    text = reader.readtext(
        './tmp/jobDistanceFromMainPage.png')
    print(text)
    if text != []:
        passPrint(text[0][1])
        if re.search(r"\d+", text[0][1]) is not None:
            return int(re.search(r"\d+", text[0][1]).group())
    errorPrint("Ops! recognizeImg failed！")
    return None


def waitPageChangeTo(page):
    while getState() != page:
        time.sleep(1)
        print("waitPageChangeTo {}".format(page))


def jobDistanceFromJobPage():
    splitLine("jobDistanceFromJobPage")
    openJobPage()
    jobPageJobIconLoc = pyautogui.locateCenterOnScreen(
        jobPageJobIconImg, region=jobPageJobIconRegin, confidence=0.8)
    jobPageJobIconLoc = position(jobPageJobIconLoc.x, jobPageJobIconLoc.y)
    wordLoc = jobPageJobIconLoc+wordShiftIconInJobPage
    im = pyautogui.screenshot(region=(wordLoc.x, wordLoc.y, 100, 25))
    im.save('./tmp/jobDistanceFromJobPage.png')
    reader = easyocr.Reader(['en'])
    text = reader.readtext(
        './tmp/jobDistanceFromJobPage.png')
    print(text)
    exitJobPage()
    if text != []:
        passPrint(text[0][1])
        if re.search(r"\d+", text[0][1]) is not None:
            return int(re.search(r"\d+", text[0][1]).group())
    errorPrint("Ops!Ops! recognizeImg failed！")
    return None


def jobDistance(type):
    fly(1, 1, forward)
    if type == "Big":
        exceptAns = 300
    elif type == "Small":
        exceptAns = 10
    distance = jobDistanceFromMainPage()
    if distance is None:
        distance = jobDistanceFromJobPage()
    if distance is None:
        return exceptAns
    else:
        return distance


def checkJobDistance():
    fly(1, 1, forward)
    checkDistance = jobDistanceFromMainPage()
    checkJobDistance2 = jobDistanceFromJobPage()
    if checkJobDistance2 is None:
        checkJobDistance2 = 0
    if checkDistance is None:
        checkDistance = 0
    return max(checkDistance, checkJobDistance2)


def go2jobTargetOne():
    openMap()
    targetPosition = moveMapforJobIcon()
    if targetPosition is not None:
        transportPosition = getNearestTransport(targetPosition)
        if transportPosition is not None:
            transPort(transportPosition)
    else:
        print("Not find job target in Map")
    waitPageChangeTo("mainPage")


def go2jobTarget(maxtime):
    splitLine("go2jobTarget")
    distance = checkJobDistance()
    if maxtime == 0:
        return 0
    elif distance == -1:
        return -1
    elif distance < 300:
        return 0
    else:
        go2jobTargetOne()
        go2jobTarget(maxtime-1)


def awakeJob():
    splitLine("awakeJob")
    clickAbsolute(absoluteAwakeJob)


def fineTuningVisualAngle(distance):
    waitPageChangeTo("mainPage")
    if distance < 50:
        accuracyRank = 4
    else:
        accuracyRank = 4
    location = pyautogui.locateCenterOnScreen(
        jobFineTuningImg, region=jobFineTuningRegin, confidence=0.8)
    if location is None:
        location = pyautogui.locateCenterOnScreen(
            jobFineTuningBigImg, region=jobFineTuningRegin, confidence=0.8)
    if location is None:
        errorPrint("mainPage no location showed?!")
        awakeJob()
        if jobDistance() == -1:
            return -1
        else:
            return 1
    location = position(location.x, location.y)
    if location.y > 650 or location.y < 270 or (location.x > 690 and location.x < 940):
        accuracyRank = 2
    moveDirection = location - mainpageCenter
    if posDistance(location, mainpageCenter) < 3*100*100:
        return 0
    passPrint("fine tuning direction ({},{})".format(
        moveDirection.x, moveDirection.y))
    moveDirection = math.pow(0.5, accuracyRank) * moveDirection
    # print(moveDirection)
    beginPos = mainpageCenter - moveDirection
    finalPos = mainpageCenter + moveDirection
    # 800,900表示鼠标拖拽的起始位置，0.2设置鼠标移动快慢
    pyautogui.moveTo(beginPos.x, beginPos.y, 0.2)
    # 200,200表示鼠标拖拽的终点位置，0.2设置鼠标拖拽的快慢，“easeOutQuad”表示鼠标拖动先快后慢（多种拖拽方式可选）
    pyautogui.dragTo(finalPos.x, finalPos.y, 2, pyautogui.easeOutQuad)
    return 1


def dialogBoxShowed(distance=-1):
    if distance > 3:
        return 1
    elif distance != -1:
        if checkJobDistance() > 3:
            return 1
    location = pyautogui.locateCenterOnScreen(
        dialogBoxImg, region=dialogBoxRegin, confidence=0.8)
    if location is not None:
        clickAbsolute(position(location.x, location.y))
        return 0
    else:
        return 1


def dialog():
    splitLine("dialog")
    time.sleep(2)
    notFinished = 1
    while notFinished:
        sleepRandom(0.5)
        choiceLoc = pyautogui.locateCenterOnScreen(
            inDialogIcon, region=inDialogIconRegin, confidence=0.8)
        # dialogBoxLoc = pyautogui.locateCenterOnScreen(
        #     dialogBoxImg, region=dialogBoxRegin, confidence=0.8)
        quickClickAbsolute(shiftCenter)
        if getState() == "mainPage":
            notFinished = 0
            break
        if choiceLoc is not None:
            quickClickAbsolute(position(choiceLoc.x, choiceLoc.y))
        quickClickAbsolute(absoluteFirstDialogChoice)
    completePrint("Dialog FINISHED!!!")


def goBack():
    jumpDownFunc()
    fly(3, 2, backward)
    fly(3, 3, right)


def go2jobTargetDetail():
    distance = jobDistance("Small")
    if distance == -1:
        return -1
    isNeededTuningAngle = 1
    while isNeededTuningAngle:
        isNeededTuningAngle = fineTuningVisualAngle(distance)
    print("tuning FINISHED!!")
    stuckCount = 0
    while dialogBoxShowed(distance):
        stuckCount += 1
        if stuckCount == 8:
            goBack()
            stuckCount = 0
            continue
        distance = jobDistance("Small")
        jumpDownFunc()
        fly(1, 1, left)
        if distance == -1:
            return -1
        if distance > 100:
            fly(10, 2, forward)
        elif distance > 30:
            fly(6, 2, forward)
        elif distance > 10:
            fly(3, 2, forward)
        else:
            fly(1, 1, forward)
            # input = [['Control', 1, const.shortPress], [
            #     'W', 1, const.longPress]]  # Control ——jump
            # key_input(input)
        isNeededTuningAngle = 1
        while isNeededTuningAngle == 1:
            isNeededTuningAngle = fineTuningVisualAngle(distance)
    dialog()


def getState():
    state = "loading"
    while state == "loading":
        print("state check…………")
        time.sleep(1)
        location = pyautogui.locateCenterOnScreen(
            decideMainIconImg, region=decideMainIconRegin, confidence=0.8)
        if location is not None:
            return "mainPage"
        location = pyautogui.locateCenterOnScreen(
            uniqueJobPageImg, region=uniqueJobPageRegin, confidence=0.8)
        if location is not None:
            return "jobPage"
        autoDialogLoc = pyautogui.locateCenterOnScreen(
            autoDialogImg, region=autoDialogRegin, confidence=0.8)
        if autoDialogLoc is not None:
            return "dialog"
        location = pyautogui.locateCenterOnScreen(
            decideMapExitIconImg, region=decideMapExitIconRegin, confidence=0.8)
        if location is not None:
            return "map"


def simpleAttackTest():
    while 1:
        trytime = 3
        while trytime > 0:
            Attack(trytime)
            trytime -= 1


def test():
    back2mainPage()
    # 攻击测试
    # simpleAttackTest()

    # 接取任务
    # if checkInfo(const.checkJobReceived) is None:
    #     receiveJob(const.worldJob)

    # # # 检查 - 任务接取完成，地图移动 传送
    # go2jobTarget(1)
    # completePrint("Big Move Complete!")
    # # 微调视角，移动，对话
    # go2jobTargetDetail()

    toDoTask()

    # 数字识别
    # jobLoc = checkInfo(const.checkJobReceived)
    # distance = jobDistance()


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
