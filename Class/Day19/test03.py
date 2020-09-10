"""

    pyQt : c++ 의 qt 라이브러리를 python으로도 사용할 수 있게
            변환한 라이브러리

    => UI 구현 (User Interface)
        버튼, 체크박스, 텍스트 필드

"""
import sys
from PyQt5.QtWidgets import (QInputDialog, QApplication, QPushButton)


def a():
    print("클릭됨~")

app = QApplication(sys.argv)

# d = QInputDialog()
# d.setTextValue("메롱")
# d.show()

btn = QPushButton()
btn.setWindowTitle("나의 버튼 창")
btn.setGeometry(200, 100, 150, 400) # (left, top, width, height)
                                    # left : 맨 왼쪽에서 몇 pixel 떨어졌는지
                                    # top : 맨 위쪽에서 몇 pixel
                                    # width : 위젯의 너비 pixel
                                    # height : 위젯의 높이 pixel
btn.setText("클릭해보세요!")
btn.clicked.connect(a)

btn.show()

app.exec()