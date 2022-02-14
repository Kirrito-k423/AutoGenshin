
from basicClass import position, const, job, team, COMBO

# regexName = "模拟器1"
regexName = "BlueStacks"

# 攻击按键映射
attackIcon = 'Spacebar'
smallSkills = 'E'
maxSkills = 'R'
forward = 'W'
backward = 'S'
right = 'D'
left = 'A'
jump = 'Control'
jumpDown = attackIcon

globalJob = job("None")
globalTeam = team(None)
# 夜神坐标
origin = position(100, 100)
topBarHeight = position(0, 32)
quarterMainPageHeight = position(640, 360)
mainpageCenter = origin + topBarHeight + quarterMainPageHeight
scale = position(600, 500)


# 位置
shiftMap = position(144, 130)
shiftCenter = position(690, 245)
shiftJobIcon = position(50, 200)
shiftJobClassIcon = [position(68, 161),
                     position(68, 238),
                     position(68, 323),
                     position(68, 403),
                     position(68, 483)]
shiftAccIcon = position(1115, 690)

absoluteAwakeJob = position(151, 351)
absoluteFirstDialogChoice = position(925, 622)
absolutedialogX = position(1320, 171)
absolutePersonSkill = [position(1164, 295),
                       position(1164, 368),
                       position(1164, 443)]
absolutePerson = [position(1320, 295),
                  position(1164, 368),
                  position(1164, 443)]

# 相对偏移
wordShiftIconInJobPage = position(-380, 0)

# const
const.longPress = 2333
const.shortPress = 'yahaha'
const.mainJob = 1
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
           'R': 0x52,
           'Shift'	: 16,
           'Control'	: 17,
           'Spacebar':	32
           }
easyOCRFix = {'O': '0', 'o': '0',
              'l': '1', 'I': '1',
              'D': '2',
              'B': '3',
              'S': '5',
              'G': '6',
              'T': '7',
              'g': '9',
              'e': '12'}

characterAttackComboByName = {"钟离": COMBO("钟离", [[smallSkills, 1, const.longPress], [attackIcon, 1, const.shortPress], [maxSkills, 1, const.shortPress]], None),
                              "行秋": COMBO("行秋", [[attackIcon, 1, const.shortPress], [smallSkills, 1, const.shortPress], [maxSkills, 1, const.shortPress]], "香菱"),
                              "香菱": COMBO("香菱", [[attackIcon, 1, const.shortPress], [smallSkills, 1, const.shortPress], [maxSkills, 1, const.shortPress]], "钟离"),
                              "菲谢尔": COMBO("菲谢尔", [[smallSkills, 1, const.shortPress]], "钟离")}
# 奶 盾角色combo
characterSaveComboByName = {"钟离": COMBO("钟离盾来", [[smallSkills, 1, const.longPress], [
                                        attackIcon, 1, const.shortPress], [maxSkills, 1, const.shortPress]], None)}
# imgPath
checkJobReceivedImg = "./Img/checkJobReceivedImg.png"
checkJobReceivedRegion = (130, 330, 36, 36)
checkJobReceivedGoldDiamondImg = "./Img/CheckJobReceivedGoldDiamond.png"
checkJobReceivedMainImg = "./Img/checkJobReceivedMain.png"
centerRegion = (101, 132, 1280, 720)
realCenterRegion = (540, 350, 530, 260)
transportAccRegion = (1137, 772, 130, 100)
chaseRegin = (1127, 765, 200, 65)
transportTextRegion = (880, 400, 500, 350)
jobFineTuningRegin = (330, 220, 900, 550)  # 1120, 680
dialogBoxRegin = (800, 400, 200, 200)
inDialogIconRegin = (890, 350, 100, 300)
autoDialogRegin = (160, 150, 150, 70)
decideMainIconRegin = (120, 140, 80, 80)
decideMapExitIconRegin = (1270, 140, 120, 100)
jobPageJobIconRegin = (560, 180, 140, 600)
uniqueJobPageRegin = (120, 750, 100, 100)
dialogXRegin = (1292, 150, 80, 80)
jobMapImg = "./Img/jobMapImg.png"
jobMapGoldImg = "./Img/jobMapImgGold.png"
jobMapMainImg = "./Img/jobMapImgMain.png"
jobMapImg2 = "./Img/jobMapImg2.png"
jobMapGoldImg2 = "./Img/jobMapImg2Gold.png"
jobMapMainImg2 = "./Img/jobMapImg2Main.png"
transportImg = "./Img/transport.png"
sevenStatueImg = "./Img/sevenStatue.png"
transportAccImg = "./Img/transportAcc.png"
transportTextImg = "./Img/transportText.png"
jobFineTuningImg = "./Img/jobFineTuning.png"
jobFineTuningGlodImg = "./Img/jobFineTuningGlod.png"
jobFineTuningMainImg = "./Img/jobFineTuningMain.png"
dialogBoxImg = "./Img/dialogBox.png"
inDialogIcon = "./Img/inDialogIcon.png"
autoDialogImg = "./Img/autoDialog.png"
decideMainIconImg = "./Img/decideMianIcon.png"
decideMapExitIconImg = "./Img/decideMapExitIcon.png"
jobPageJobIconImg = "./Img/jobPageJobIcon.png"
jobPageJobIconGoldImg = "./Img/jobPageJobIconGold.png"
jobPageJobIconMainImg = "./Img/jobPageJobIconMain.png"
jobFineTuningBigImg = "./Img/jobFineTuningBig.png"
jobFineTuningBigGlodImg = "./Img/jobFineTuningBigGlod.png"
jobFineTuningBigMainImg = jobFineTuningMainImg
uniqueJobPageImg = "./Img/uniqueJobPage.png"
dialogXImg = "./Img/dialogX.png"
chaseImg = "./Img/chase.png"
stopChaseImg = "./Img/stopChase.png"
jobMapTop = 228
jobMapLeft = 203
jobMapBottom = 755
jobMapRight = 1283
jobMapSearchHalfWidth = 28
