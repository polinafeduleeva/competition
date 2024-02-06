from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
from predict_text import pred_text
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 450, 500)
        self.setWindowTitle('тестирование нейронной сети')
        self.img_name = None
        self.label_img = QLabel(self)
        self.label_img.move(10, 10)
        # кнопка, вызывающая диалог для выбора картинки
        self.file_button = QPushButton(self)
        self.file_button.resize(150, 50)
        self.file_button.move(150, 440)
        self.file_button.setText('Загрузить файл')
        self.file_button.clicked.connect(self.choice_file)
        # кнопка, по которой начинается распознавание
        self.file_button = QPushButton(self)
        self.file_button.resize(150, 50)
        self.file_button.move(150, 380)
        self.file_button.setText('Распознать текст')
        self.file_button.clicked.connect(self.predict)

    def choice_file(self):
        self.img_name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        img = QPixmap(self.img_name)
        self.label_img.setPixmap(img)
        self.label_img.resize(img.width(), img.height())
    def predict(self):
        if self.img_name:
            print(pred_text(self.img_name))


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.show()
    sys.exit(app.exec())
