import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout,
    QLCDNumber, QVBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('KSP GUI')

        label_Speed = QLabel('Speed: ')
        label_Dist = QLabel('Dist: ')
        label_Alt = QLabel('Alt:  ')
        speed = 5
        varSpeed = QLCDNumber()
        varSpeed.display(speed)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(label_Speed,1,0)
        grid.addWidget(label_Dist,2,0)
        grid.addWidget(label_Alt,3,0)
        grid.addWidget(varSpeed,1,1)

        self.setLayout(grid)
        self.show()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Tab:
            speed = 10
            #self.grid.addWidget(varSpeed,2,1)
            processEvents()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()