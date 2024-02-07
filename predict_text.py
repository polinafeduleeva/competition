from ultralytics import YOLO
from PIL import Image
import os

# Подгружается обученная нейронная сеть и tesseract
model_cut = YOLO('weights/best_50.pt')
model_numbers = YOLO('weights/last_numbers.pt')


# Функция для определения текста на картинке
def pred_text(img):
    # с помощью функции cut_img из изображения вырезается нужный нам кусок с прибором
    img2 = cut_img(img)
    # ненйронная сеть определяет цифры на изображении
    res = model_numbers.predict(img2)
    arr = []
    # результаты преобразуются в массив с элементами типа (класс, x координата левого верхнего угла,
    # у координата левого верхнего угла)
    for i in range(sum([1 for _ in res[0].boxes.xyxy])):
        arr.append((int(res[0].boxes.cls[i]), (float(res[0].boxes.xyxy[i][0]) // 75,
                                               float(res[0].boxes.xyxy[i][1]) // 75)))
    # полученный список сортируется по возрастанию координат
    # функция возвращает последовательность цифр на картинке в виде строки
    return ''.join([str(elem[0]) for elem in sorted(arr, key=lambda x: (x[1][0], 0 - x[1][1]))])


def cut_img(img):
    res = model_cut.predict(img)
    img = Image.open(img)
    if res:
        if res[0]:
            box = [int(float(elem)) for elem in res[0].boxes.xyxy[0]]
            img = img.crop(box)
    return img


def predict_path(dir_path):
    # функция, проходящая по изображениям в папке и сохраняющая результаты распознавания с них в текстовом файле
    f = open('results.txt', 'w')
    for file in os.listdir(dir_path):
        if os.path.isfile(f'{dir_path}/{file}'):
            f.write(file + ' ' + pred_text(f'{dir_path}/{file}') + '\n')
    f.close()


if __name__ == '__main__':
    # код запрашивает папку с изображениями, в выбранной папке проходит по изображениям и распознаёт их
    print('Введите папку с изображениями')
    path = input()
    predict_path(path)
    print('Результаты сохранены в файле results.txt')
