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
        print("back2mainPage…………")
        state = getState()
# def mouseMove(shift):


def receiveJob(jobID):
    clickShift(shiftJobIcon)
    clickShift(shiftJobClassIcon[jobID])
    clickShift(shiftAccIcon)


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
    # 攻击测试
    # simpleAttackTest()

    # 接取任务
    # if checkInfo(const.checkJobReceived) is None:
    #     receiveJob(const.worldJob)

    # # # 检查 - 任务接取完成，地图移动 传送
    go2jobTarget(1)
    completePrint("Big Move Complete!")
    # 微调视角，移动，对话
    go2jobTargetDetail()

    toDoTask()

    # 数字识别
    # jobLoc = checkInfo(const.checkJobReceived)
    # distance = jobDistance()


if __name__ == '__main__':
    if reset_window_pos(origin.x, origin.y, regexName):
        print("not found process! over")
        sys.exit()

    test()
