
from basicClass import position, const

regexName = "模拟器1"

# 夜神坐标
origin = position(100, 100)
topBarHeight = position(0, 32)
quarterMainPageHeight = position(640, 360)
mainpageCenter = origin + topBarHeight + quarterMainPageHeight
scale = position(600, 500)

shiftMap = position(144, 130)
shiftCenter = position(690, 245)
shiftJobIcon = position(50, 200)
shiftJobClassIcon = [position(68, 161),
                     position(68, 238),
                     position(68, 323),
                     position(68, 403),
                     position(68, 483)]
shiftAccIcon = position(1115, 690)

absoluteAwakeJob = position(184, 351)
absoluteFirstDialogChoice = position(925, 622)

# const
const.longPress = 2333
const.shortPress = 'yahaha'

const.worldJob = 4

const.checkJobReceived = 1
# code https://blog.csdn.net/chang1976272446/article/details/103761029
# https://cxymm.net/article/weixin_39552874/110753639
VK_CODE = {'Esc': 27,
           'W':	87,
           'A':	65,
           'S':	83,
           'D':	68,
           'E':	69,
           'Shift'	: 16,
           'Control'	: 17,
           'Spacebar':	32
           }

# imgPath
checkJobReceivedImg = "./Img/checkJobReceivedImg.png"
checkJobReceivedRegion = (130, 330, 36, 36)
centerRegion = (101, 132, 1280, 720)
transportAccRegion = (1137, 772, 130, 100)
transportTextRegion = (880, 520, 500, 300)
jobFineTuningRegin = (330, 220, 900, 550)  # 1120, 680
dialogBoxRegin = (800, 400, 200, 200)
inDialogIconRegin = (890, 350, 100, 300)
autoDialogRegin = (160, 150, 150, 70)
decideMianIconRegin = (120, 140, 80, 80)
decideMapExitIconRegin = (1270, 140, 120, 100)
jobMapImg = "./Img/jobMapImg.png"
jobMapImg2 = "./Img/jobMapImg2.png"
transportImg = "./Img/transport.png"
transportAccImg = "./Img/transportAcc.png"
transportTextImg = "./Img/transportText.png"
jobFineTuningImg = "./Img/jobFineTuning.png"
dialogBoxImg = "./Img/dialogBox.png"
inDialogIcon = "./Img/inDialogIcon.png"
autoDialogImg = "./Img/autoDialog.png"
decideMianIconImg = "./Img/decideMianIcon.png"
decideMapExitIconImg = "./Img/decideMapExitIcon.png"
jobMapTop = 228
jobMapLeft = 203
jobMapBottom = 755
jobMapRight = 1283
jobMapSearchHalfWidth = 28
