# coding=utf-8
from task import *
from map import *
import sys


def back2mainPage():
    splitLine("back2mainPage")
    state = getState()
    while state != "mainPage":
        if state == "dialog":
            dialog()
        else:
            keyExit()
        time.sleep(1.5)
        print("back2mainPage…………")
        state = getState()
# def mouseMove(shift):


def receiveJob(jobID):
    openJobPage()
    clickShift(shiftJobClassIcon[jobID])
    if checkJobReceivedFromJobPage() == True:
        clickShift(shiftAccIcon)
    else:
        keyExit()
    waitPageChangeTo("mainPage")


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
    elif distance < 200:
        return 0
    else:
        go2jobTargetOne()
        go2jobTarget(maxtime-1)


def go2jobTargetDetail():
    goBack2Task()


def simpleAttackTest():
    while 1:
        trytime = 3
        while trytime > 0:
            Attack(trytime)
            trytime -= 1


def test():
    back2mainPage()
    confirmTeam()
    while True:
        # 接取任务
        if checkJobType() is None:
            receiveJob(const.mainJob)
        if checkJobType() is not None:
            # # # 检查 - 任务接取完成，地图移动 传送
            isGet2Task = go2jobTarget(1)
            completePrint("Big Move Complete!")
            # 微调视角，移动，对话
            if isGet2Task != -1:
                go2jobTargetDetail()
            # 具体任务
            toDoTask()
        time.sleep(2)
        back2mainPage()

    # 攻击测试
        # simpleAttackTest()


if __name__ == '__main__':
    if reset_window_pos(origin.x, origin.y, regexName):
        print("not found process! over")
        sys.exit()

    # test()
    Attack()
