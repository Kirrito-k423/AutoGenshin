from atomAction import *
import easyocr
import re


def fixEasyOCRNumberResult(string):
    ans = ''
    for word in string:
        if word in easyOCRFix:
            ans += easyOCRFix[word]
        else:
            ans += word
    return ans[:-1]+'m'


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
        if re.search(r"(到达)|(区域)", text[0][1]) is not None:
            completePrint("Get Position！")
            return -1
        else:
            text = fixEasyOCRNumberResult(text[0][1])
            colorPrint(text, 'magenta')
            if re.search(r"\d+", text) is not None:
                return int(re.search(r"\d+", text).group())

    reader = easyocr.Reader(['en'])
    text = reader.readtext(
        './tmp/jobDistanceFromMainPage.png')
    print(text)
    if text != []:
        passPrint(text[0][1])
        text = fixEasyOCRNumberResult(text[0][1])
        colorPrint(text, 'magenta')
        if re.search(r"\d+", text) is not None:
            return int(re.search(r"\d+", text).group())
    errorPrint("Ops! recognizeImg failed！")
    return None


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
        text = fixEasyOCRNumberResult(text[0][1])
        colorPrint(text, 'magenta')
        if re.search(r"\d+", text) is not None:
            return int(re.search(r"\d+", text).group())
    errorPrint("Ops!Ops! recognizeImg failed！")
    return None


def jobDistance(type):
    # fly(1, 1, forward) 由于有手动修正，准确率不需要通过变位置来提高了
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
    # fly(1, 1, forward)
    checkDistance = jobDistanceFromMainPage()
    checkJobDistance2 = jobDistanceFromJobPage()
    if checkJobDistance2 is None:
        checkJobDistance2 = 0
    if checkDistance is None:
        checkDistance = 0
    return max(checkDistance, checkJobDistance2)
