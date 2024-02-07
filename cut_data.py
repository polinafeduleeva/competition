import os
from predict_text import cut_img


def cut_data(path, new_path):
    # Функция для подготовки датасета под нейросеть для определения цифр
    files = os.listdir(path)
    i = 1
    for file in files:
        print(i)
        img = cut_img(f'{path}/' + file)
        img.save(f'{new_path}/{i}.jpg')
        i += 1


if __name__ == '__main__':
    cut_data('glucometer_images', 'new_data')
