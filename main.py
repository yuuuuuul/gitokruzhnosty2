import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic  # Импортируем uic
sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_ellipse(qp)
            # Завершаем рисование
            qp.end()

    def draw_ellipse(self, qp):
        radius = random.randint(10, 150)
        x = random.randint(10, 250)
        y = random.randint(10, 250)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, 2 * radius, 2 * radius)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = MyWidget()
        ex.show()
        sys.exit(app.exec())
    except:
        print("Exiting")