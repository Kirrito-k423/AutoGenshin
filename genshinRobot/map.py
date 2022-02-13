
from atomAction import *


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


def clickJobIconMap2Move(location):
    location = position(location.x, location.y)
    clickAbsolute(location)
    time.sleep(2)


def moveMapforJobIcon():
    trytime = 3
    isJobIconInEdge = "edge"
    while isJobIconInEdge == "edge" or isJobIconInEdge == "outCenter"\
            or isJobIconInEdge == "None":
        [location, isJobIconInEdge] = getJobIconMapPosition()
        clickJobIconMap2Move(location)
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
