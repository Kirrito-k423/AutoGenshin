from controlInput import *


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


def checkInfo(type):
    if type == const.checkJobReceived:
        return checkPicExists(checkJobReceivedImg, checkJobReceivedRegion, 0.6)


def checkPicExists(Img, region, confidence):
    # ,region 4-integer tuple of (left, top, width, height))
    location = pyautogui.locateCenterOnScreen(
        Img, region=region, confidence=confidence)
    if location is not None:
        passPrint("{} is Existed ({},{})".format(Img, location.x, location.y))
    else:
        errorPrint("{} is NOT Existed".format(Img))
    return location


def waitPageChangeTo(page):
    while getState() != page:
        print("waitPageChangeTo {}".format(page))


def posDistance(a, b):
    return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y)


def awakeJob():
    splitLine("awakeJob")
    quickClickAbsolute(absoluteAwakeJob)


def getState():
    state = "loading"
    while state == "loading":
        print("state check…………")
        location = pyautogui.locateCenterOnScreen(
            decideMainIconImg, region=decideMainIconRegin, confidence=0.8)
        if location is not None:
            state = "mainPage"
            break
        location = pyautogui.locateCenterOnScreen(
            uniqueJobPageImg, region=uniqueJobPageRegin, confidence=0.8)
        if location is not None:
            state = "jobPage"
            break
        autoDialogLoc = pyautogui.locateCenterOnScreen(
            autoDialogImg, region=autoDialogRegin, confidence=0.8)
        if autoDialogLoc is not None:
            state = "dialog"
            break
        location = pyautogui.locateCenterOnScreen(
            dialogXImg, region=dialogXRegin, confidence=0.8)
        if location is not None:
            state = "dialogX"
            break
        location = pyautogui.locateCenterOnScreen(
            decideMapExitIconImg, region=decideMapExitIconRegin, confidence=0.8)
        if location is not None:
            state = "map"
            break
    colorPrint("{} is state".format(state), "cyan")
    return state
