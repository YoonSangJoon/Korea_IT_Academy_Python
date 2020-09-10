import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()  # 부모모양 객체를 생성 (QWidget 객체)
        self.setUI()

    def setUI(self):
        self.setWindowTitle('My Gui')
        self.setGeometry(0, 0, 250, 500)
        # 윈도우 창에 넣을 버튼 2개 생성
        self.b1 = QPushButton()
        self.b2 = QPushButton()

        self.b1.setText("Button #1")
        self.b2.setText("Button #2")

        # 레이아웃 생성
        self.l = QVBoxLayout()  # V : Vertical (수직방향)
        # H : horizontal (수평방향)

        # 레이아웃에 버튼 위젯 2개 붙이기
        self.l.addWidget(self.b1)
        self.l.addWidget(self.b2)

        # 윈도우 창의 레이아웃을, 위에서 만든 레이아웃으로 지정
        self.setLayout(self.l)



a = QApplication(sys.argv)
my = MyWindow()
my.show()
a.exec()