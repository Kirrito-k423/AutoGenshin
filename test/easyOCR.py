

import easyocr
from tsjCommonFunc import *
import sys
sys.path.append(
    "D:\\PowerShell\\github\\waterRPA\\genshinRobot")
# this needs to run only once to load the model into memory


def onece():
    result = reader.readtext(
        './jobDistanceFromJobPage2.png', detail=0)
    print(result)
    if result != []:
        print(result[0])


reader = easyocr.Reader(['en'], gpu=False)
testTime(10, onece)
