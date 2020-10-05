import sys
from PyQt5.QtWidgets import *
from random import randint

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.quiz_label = QLabel()
        self.answer_line_edit = QLineEdit()
        self.result_btn = QPushButton()
        self.result_label = QLabel()

        self.setWindowTitle('Gugudan Game!')
        self.setGeometry(0, 0, 300, 100)

        self.n1 = randint(2, 9)
        self.n2 = randint(1, 9)
        self.quiz_label.setText('{} X {}'.format(self.n1, self.n2))

        self.result_btn.setText('결과 확인!')
        self.result_btn.clicked.connect(self.show_result)

        layout = QVBoxLayout()
        layout.addWidget(self.quiz_label)
        layout.addWidget(self.answer_line_edit)
        layout.addWidget(self.result_btn)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.show()

    def show_result(self):
        if self.n1 * self.n2 == int( self.answer_line_edit.text() ):
            self.result_label.setText('정답!!')
            self.n1 = randint(2, 9)
            self.n2 = randint(1, 9)
            self.quiz_label.setText('{} X {}'.format(self.n1, self.n2))
        else:
            self.result_label.setText('땡..')
        self.answer_line_edit.setText('')  # 입력란의 남아있던 텍스트 삭제


if __name__ == '__main__':
    a = QApplication(sys.argv)
    my = MyWidget()
    a.exec()