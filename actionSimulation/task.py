
from job import *


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


def fourBigSkills(num):
    # three other gui
    quickClickAbsolute(absolutePersonSkill[num-1])


def changePerson(num):
    quickClickAbsolute(absolutePerson[num-1])


def combo():
    input = [[attackIcon, 2, const.shortPress],
             [smallSkills, 1, const.longPress],
             [attackIcon, 3, const.shortPress]]
    key_input(input)


def Attack(num):
    colorPrint("{} 塔塔开！！！".format(num), "yellow")
    fly(1, 1, right)
    combo()
    fourBigSkills(num)
    fly(1, 1, forward)
    changePerson(num)
    fly(1, 1, left)


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


def toDoTask():
    while isAttack():
        goBack2Task()
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


def dialogBoxShowed(distance=-1):
    if distance > 3:
        return 1
    elif distance != -1:
        if checkJobDistance() > 3:
            return 1
    location = pyautogui.locateCenterOnScreen(
        dialogBoxImg, region=dialogBoxRegin, confidence=0.8)
    if location is not None:
        quickClickAbsolute(position(location.x, location.y))
        dialog()
        return 0
    else:
        return 1


def moveDependsDistance():
    distance = jobDistance("Small")
    if distance == -1:
        return -1
    else:
        if distance < 10:
            fly(1, 1, forward)
        else:
            jumpDownFunc()
            fly(1, 1, left)
            if distance > 100:
                fly(10, 2, forward)
            elif distance > 30:
                fly(6, 2, forward)
            elif distance > 10:
                fly(3, 2, forward)


def goBack2Task():
    distance = jobDistance("Small")
    if distance == -1:
        return -1
    fineTuningVisualAngle(distance)
    print("tuning FINISHED!!")
    stuckCount = 0
    while dialogBoxShowed(distance):
        stuckCount += 1
        if stuckCount == 8:
            goBack()
            stuckCount = 0
            continue
        moveDependsDistance()
        # input = [['Control', 1, const.shortPress], [
        #     'W', 1, const.longPress]]  # Control ——jump
        # key_input(input)
        if fineTuningVisualAngle(distance) == -1:
            completePrint("It's Task Time!")
            return -1
