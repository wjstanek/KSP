import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('KSP GUI')

        label = QLabel('Speed: ' + str(speed))

        self.show()

def main(sensorData):
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    pass
