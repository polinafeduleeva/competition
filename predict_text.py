from ultralytics import YOLO
from PIL import Image
import pytesseract

# Подгружается обученная нейронная сеть и tesseract
model = YOLO('weights/best_50.pt')
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'

# Функция для определения текста на картинке
def pred_text(img):
    # нужный объект находится на изображении с помощью нейросети и вырезается
    res = model(img)
    if res:
        img = Image.open(img)
        box = [int(float(elem)) for elem in res[0].boxes.xyxy[0]]
        img.crop(box)
        #  полученное изображение загружается в pytesseract, где определяется текст
        txt = pytesseract.image_to_string(img, lang='eng', config='-c tessedit_char_whitelist=0123456789 --psm 11 --oem 3')

        txt = txt.replace(' ', '')
        txt = txt.replace('\n', '')
        txt = txt.replace('\t', '')
        return txt


if __name__ == '__main__':
    print(pred_text("test/images/20210806_17_07_31_000_wFlY39NOieR2fsNI4wU820Izeog2_F_3456_4608_jpg.rf.1ca3809a0ce2c80b79ca80a65ff10c20.jpg"))

