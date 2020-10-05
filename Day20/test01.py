import sys
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.v1 = None   # 숫자 1 입력창 (QLineEdit)
        self.v2 = None   # 숫자 2 입력창 (QLineEdit)
        self.btn = None  # 결과보기 버튼 (QPushButton)
        self.r1 = None   # 덧셈 결과 (QLabel)
        self.r2 = None   # 뺄셈 결과 (QLabel)
        self.r3 = None   # 곱셈 결과 (QLabel)
        self.r4 = None   # 나눗셈 결과 (QLabel)
        self.setWidgets()

    def setWidgets(self):
        self.setWindowTitle('My Calculator')
        self.setGeometry(0, 0, 250, 250)

        # 위젯 세팅
        self.v1 = QLineEdit()  # 숫자 1 입력창 (QLineEdit)
        self.v2 = QLineEdit()  # 숫자 2 입력창 (QLineEdit)
        self.btn = QPushButton()  # 결과보기 버튼 (QPushButton)
        self.r1 = QLabel()  # 덧셈 결과 (QLabel)
        self.r2 = QLabel()  # 뺄셈 결과 (QLabel)
        self.r3 = QLabel()  # 곱셈 결과 (QLabel)
        self.r4 = QLabel()  # 나눗셈 결과 (QLabel)

        self.v1.setPlaceholderText("첫 번째 숫자를 입력하세요.")
        self.v2.setPlaceholderText("두 번째 숫자를 입력하세요.")

        self.btn.setText("결과 보기")
        self.btn.clicked.connect(self.show_result)

        # 작은 레이아웃 생성
        layout = QVBoxLayout()  # V : Vertical (수직방향)
        # H : horizontal (수평방향)

        # 레이아웃에 버튼 위젯 2개 붙이기
        layout.addWidget(self.v1)
        layout.addWidget(self.v2)
        layout.addWidget(self.btn)
        layout.addWidget(self.r1)
        layout.addWidget(self.r2)
        layout.addWidget(self.r3)
        layout.addWidget(self.r4)

        # 윈도우 창의 레이아웃을, 위에서 만든 레이아웃으로 지정
        self.setLayout(layout)

    def show_result(self):
        val1 = float(self.v1.text())
        val2 = float(self.v2.text())
        self.r1.setText("{} + {} = {}".format(val1, val2, val1 + val2))
        self.r2.setText("{} - {} = {}".format(val1, val2, val1 - val2))
        self.r3.setText("{} * {} = {}".format(val1, val2, val1 * val2))
        self.r4.setText("{} / {} = {}".format(val1, val2, val1 / val2))

if __name__ == '__main__':
    a = QApplication(sys.argv)
    my = MyWidget()
    my.show()
    a.exec()