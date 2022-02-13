

from tsjCommonFunc import *
import easyocr
import sys
sys.path.append(
    "D:\\PowerShell\\github\\waterRPA\\actionSimulation")
# this needs to run only once to load the model into memory


def onece():
    result = reader.readtext(
        './jobDistanceFromJobPage2.png', detail=0)
    print(result)
    if result != []:
        print(result[0])


reader = easyocr.Reader(['en'])
testTime(10, onece)
