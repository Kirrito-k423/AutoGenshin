from termcolor import colored
import os
import time
import random
import plotille


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


def splitLine(string):
    print("\n")
    print("--------------------------------{}--------------------------------".format(string))
    print("\n")


def histogramsPrint(data, type="vertical"):
    if type == "vertical":
        print(plotille.histogram(data))
    else:
        print(plotille.hist(data))


def sleepRandom(seconds):
    time.sleep(round(random.uniform(0, seconds), 2))


def testTime(whileTimes, function):
    histogramsData = []
    begin = time.time()
    while whileTimes:
        beforeFunction = time.time()
        function()
        afterFunction = time.time()
        deltatime = afterFunction - beforeFunction
        colorPrint("delta time ONECE {}".format(
            deltatime), "yellow")
        histogramsData.append(deltatime)
        whileTimes -= 1
    end = time.time()
    colorPrint("ALL {}".format(end-begin), "red")
    histogramsPrint(histogramsData, "horizontal")
