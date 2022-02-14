
from job import *


def isAttack():
    splitLine("isAttack")
    haveJob = None
    while haveJob is None:
        haveJob = checkJobType()
        awakeJob()
    jobLoc = position(150, 351)
    im = pyautogui.screenshot(region=(jobLoc.x+15, jobLoc.y-13, 140, 26))
    im.save('./tmp/isAttack.png')
    reader = easyocr.Reader(['ch_sim', 'en'])
    text = reader.readtext('./tmp/isAttack.png')
    print(text)
    passPrint(text[0][1])
    if re.search(r"(解救)|(保护)|(击败)|(打倒)", text[0][1]) is not None:
        return 1
    else:
        return 0


def fourBigSkills(num):
    # three other gui
    quickClickAbsolute(absolutePersonSkill[num-1])


def changePerson():
    splitLine("changePerson")
    nextName = characterAttackComboByName[globalTeam.currentName].nextCharacter
    if nextName is None:
        text = readBenchText()
        benchTeam3 = [text[0], text[1], text[2]]
        nextName = benchTeam3[random.randint(0, 2)]
    changeBenchByName(nextName)


def combo(input):
    key_input(input, 0.7)
    time.sleep(2)


def charactorChangeByName(name):
    if globalTeam.currentName == name:
        return 0
    else:
        changeBenchByName(name)


def zhongliBABA():
    passPrint("坚如磐石~~")
    charactorChangeByName("钟离")
    combo(characterSaveComboByName["钟离"].combo)


def currentAttack():
    combo((characterAttackComboByName[globalTeam.currentName]).combo)


def isNotHealth():
    bloodLoc = position(638, 799)
    px = pyautogui.pixel(bloodLoc.x, bloodLoc.y)
    yellowPrint("({},{},{})".format(px[0], px[1], px[2]))
    pxList = (px[0], px[1], px[2])
    green = (150, 215, 34)
    if isArround(pxList, green, 10):
        return 0
    return 1


def someoneSaveMe():
    return 0


def isNeededSave():
    if isNotHealth():
        someoneSaveMe()


def Attack(num=1):
    splitLine("{} 塔塔开！！！".format(num), "yellow")
    fly(1, 0, left)
    fly(1, 0, forward)
    zhongliBABA()
    isNeededSave()
    # fly(1, 0, right)
    changePerson()
    currentAttack()
    # fly(1, 0, forward)
    changePerson()
    currentAttack()
    # fly(1, 0, left)


def isFindSomeNearDialog():
    splitLine("isFindSomeNearDialog")
    haveJob = None
    while haveJob is None:
        haveJob = checkJobType()
        awakeJob()
    jobLoc = position(150, 351)
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
            # fly(1, 1, left)
            if distance > 200:
                fly(20, 2, forward)
            elif distance > 100:
                fly(10, 2, forward)
            elif distance > 30:
                fly(6, 2, forward)
            elif distance > 10:
                fly(3, 2, forward)


def goBack2Task():
    distance = jobDistance("Small")
    if distance == -1:
        return -1
    if distance > 200:
        maxStuckTime = 14
    else:
        maxStuckTime = 10
    fineTuningVisualAngle(distance)
    print("tuning FINISHED!!")
    stuckCount = 0
    while dialogBoxShowed(distance):
        stuckCount += 1
        if stuckCount == maxStuckTime:
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


def isBreakinDialog():
    if getState() == "dialog":
        dialog()
        return 1
    return 0


def fineTuningVisualAngle(distance):
    isNeededTuningAngle = 1
    while isNeededTuningAngle == 1:
        if isBreakinDialog():
            isNeededTuningAngle = -1
            break
        waitPageChangeTo("mainPage")
        if distance < 50:
            accuracyRank = 4
        else:
            accuracyRank = 4
        location = findJobFineTuningImg()

        if location is None:
            errorPrint("mainPage no location showed?!")
            awakeJob()
            if jobDistance("Small") == -1:
                isNeededTuningAngle = -1
                break
            continue
        location = position(location.x, location.y)
        if location.y > 650 or location.y < 270 or (location.x > 690 and location.x < 940):
            accuracyRank = 2
        moveDirection = location - mainpageCenter
        if posDistance(location, mainpageCenter) < 3*100*100:
            isNeededTuningAngle = 0
            break
        passPrint("fine tuning direction ({},{})".format(
            moveDirection.x, moveDirection.y))
        moveDirection = math.pow(0.5, accuracyRank) * moveDirection
        moveScreen(moveDirection)
    return isNeededTuningAngle


def readBenchText():
    # result = {}
    time.sleep(1)
    name = {}
    while len(name) != 3:
        for nameKey, ImgValue in heads.items():
            print(nameKey)
            location = pyautogui.locateCenterOnScreen(
                ImgValue, region=headsRegin, confidence=0.8)
            if location is not None:
                passPrint("yes! the head")
                if nameKey not in name:
                    name[nameKey] = location.y
                    # result[location.y] = nameKey
            else:
                errorPrint("not this head")
    # ans = [result[x] for x in sorted(result)]
    pPrint(sorted(name.items(), key=lambda kv: kv[1]))
    ans = [x for x, y in sorted(name.items(), key=lambda kv: kv[1])]
    pPrint(ans)
    return ans
    # result = []
    # while len(result) != 3:
    #     im = pyautogui.screenshot(region=(1220, 271, 75, 190))
    #     im.save('./tmp/nameOrderInBench.png')
    #     reader = easyocr.Reader(['ch_sim', 'en'])
    #     result = reader.readtext('./tmp/nameOrderInBench.png')
    #     time.sleep(0.2)
    # pPrint(result)
    # return result


def nameOrderInBench(name):
    text = readBenchText()
    if textBelong(text[0], name):
        return 0
    elif textBelong(text[1], name):
        return 1
    elif textBelong(text[2], name):
        return 2
    else:
        return -1


def changeBenchByName(name):
    yellowPrint(name)
    order = nameOrderInBench(name)
    if order == -1:
        errorPrint("{} no charactor in bench".format(name))
        return 0
    clickAbsolute(absolutePerson[order])
    globalTeam.currentName = name
    passPrint(globalTeam.currentName)
    time.sleep(0.2)  # 换人冷却


def confirmTeam():
    splitLine("confirmTeam")
    text = readBenchText()
    firstTeam3 = {text[0], text[1], text[2]}
    yellowPrint(firstTeam3)
    changeBenchByName(text[0])
    text = readBenchText()
    secondTeam3 = {text[0], text[1], text[2]}
    globalTeam.changeNameList(yellowPrint(
        firstTeam3 | secondTeam3), yellowPrint(firstTeam3-secondTeam3))
