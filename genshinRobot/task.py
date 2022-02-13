
from job import *
import math


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
        state = getState()
        if state == "mainPage":
            notFinished = 0
            break
        elif state == "dialogX":
            quickClickAbsolute(absolutedialogX)
        if choiceLoc is not None:
            quickClickAbsolute(position(choiceLoc.x, choiceLoc.y))
        quickClickAbsolute(absoluteFirstDialogChoice)
    completePrint("Dialog FINISHED!!!")


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
        if jobDistance("Small") == -1:
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
