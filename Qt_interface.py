from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
from predict_text import pred_text
import sys
import os


WINDOW_W = 650
WINDOW_H = 700


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, WINDOW_W, WINDOW_H)
        self.setWindowTitle('тестирование нейронной сети')
        self.img_name = None
        self.label_img = QLabel(self)

        self.status_label = QLabel(self)
        self.status_label.resize(500, 30)
        self.status_label.move(200, 10)
        self.status_label.setText('Загрузите файл для распознавания')

        self.res_label = QLabel(self)
        self.res_label.resize(500, 30)
        self.res_label.move(200, 490)
        # кнопка, вызывающая диалог для выбора картинки
        self.file_button = QPushButton(self)
        self.file_button.resize(250, 50)
        self.file_button.move(200, 640)
        self.file_button.setText('Загрузить файл')
        self.file_button.clicked.connect(self.choice_file)
        # кнопка, по которой начинается распознавание
        self.file_button = QPushButton(self)
        self.file_button.resize(250, 50)
        self.file_button.move(200, 580)
        self.file_button.setText('Распознать текст')
        self.file_button.clicked.connect(self.predict)

    def choice_file(self):
        # открывается диалог с выбором картинки. Для удобства картинка отображается в окне приложения
        self.img_name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        try:
            if not os.path.isfile(self.img_name):
                raise Exception
            img = QPixmap(self.img_name)
            w, h = img.width(), img.height()
            img = img.scaled(int(0.1 * w), int(0.1 * h))
            self.label_img.setPixmap(img)
            self.label_img.resize(img.width(), img.height())
            self.label_img.move((WINDOW_W - img.width()) // 2, 50)
            self.status_label.setText('Изображение успешно загружено')
            self.res_label.setText('')
        except Exception:
            self.status_label.setText('Выбранный файл некорректен')

    def predict(self):
        # Если изображение выбрано - запускается распознавание, иначе - надпись "изображение не выбрано"
        if self.img_name:
            self.res_label.setText(f'Результат - {pred_text(self.img_name)}')
        else:
            self.status_label.setText("Изображение не выбрано")


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec())
