import pytesseract
from PIL import Image


if __name__ == '__main__':
    text = pytesseract.image_to_string(Image.open(
        "D:\\PowerShell\\github\\waterRPA\\genshinRobot\\tmp\\1.png"), lang="osd")
    print(text)
