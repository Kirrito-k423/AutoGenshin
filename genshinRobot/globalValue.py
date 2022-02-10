
from basicClass import position, const

regexName = "模拟器1"

# 夜神坐标
origin = position(100, 100)
topBarHeight = position(0, 32)
quarterMainPageHeight = position(640, 360)
mainpageCenter = origin + topBarHeight + quarterMainPageHeight

shiftMap = position(144, 130)
shiftCenter = position(690, 245)
shiftJobIcon = position(50, 200)
shiftJobClassIcon = [position(68, 161),
                     position(68, 238),
                     position(68, 323),
                     position(68, 403),
                     position(68, 483)]
shiftAccIcon = position(1115, 690)

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
jobMapImg = "./Img/jobMapImg.png"
jobMapTop = 228
jobMapLeft = 203
jobMapBottom = 755
jobMapRight = 1283
jobMapSearchHalfWidth = 28
