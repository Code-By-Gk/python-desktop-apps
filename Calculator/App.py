import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

def calculate(expression):
    try:
        result = str(eval(expression))
    except:
        result = "Error"
    return result

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Calculator")
    window.setFixedSize(300, 400)
    window.setStyleSheet("""
        QWidget {
            background-color: #f0f0f0;
        }
        QLineEdit {
            background: white;
            border: 2px solid #888;
            border-radius: 8px;
            font-size: 28px;
            padding: 10px;
        }
        QPushButton {
            background-color: #e0e0e0;
            border: none;
            font-size: 20px;
            border-radius: 8px;
        }
        QPushButton:pressed {
            background-color: #b0b0b0;
        }
    """)

    layout = QGridLayout()
    window.setLayout(layout)

    display = QLineEdit()
    display.setAlignment(Qt.AlignRight)
    display.setReadOnly(True)
    layout.addWidget(display, 0, 0, 1, 4)

    btn_7 = QPushButton('7')
    btn_7.setFixedHeight(50)
    layout.addWidget(btn_7, 1, 0)
    btn_7.clicked.connect(lambda: display.setText(display.text() + '7'))

    btn_8 = QPushButton('8')
    btn_8.setFixedHeight(50)
    layout.addWidget(btn_8, 1, 1)
    btn_8.clicked.connect(lambda: display.setText(display.text() + '8'))

    btn_9 = QPushButton('9')
    btn_9.setFixedHeight(50)
    layout.addWidget(btn_9, 1, 2)
    btn_9.clicked.connect(lambda: display.setText(display.text() + '9'))

    btn_div = QPushButton('/')
    btn_div.setFixedHeight(50)
    layout.addWidget(btn_div, 1, 3)
    btn_div.clicked.connect(lambda: display.setText(display.text() + '/'))

    btn_4 = QPushButton('4')
    btn_4.setFixedHeight(50)
    layout.addWidget(btn_4, 2, 0)
    btn_4.clicked.connect(lambda: display.setText(display.text() + '4'))

    btn_5 = QPushButton('5')
    btn_5.setFixedHeight(50)
    layout.addWidget(btn_5, 2, 1)
    btn_5.clicked.connect(lambda: display.setText(display.text() + '5'))

    btn_6 = QPushButton('6')
    btn_6.setFixedHeight(50)
    layout.addWidget(btn_6, 2, 2)
    btn_6.clicked.connect(lambda: display.setText(display.text() + '6'))

    btn_mul = QPushButton('*')
    btn_mul.setFixedHeight(50)
    layout.addWidget(btn_mul, 2, 3)
    btn_mul.clicked.connect(lambda: display.setText(display.text() + '*'))

    btn_1 = QPushButton('1')
    btn_1.setFixedHeight(50)
    layout.addWidget(btn_1, 3, 0)
    btn_1.clicked.connect(lambda: display.setText(display.text() + '1'))

    btn_2 = QPushButton('2')
    btn_2.setFixedHeight(50)
    layout.addWidget(btn_2, 3, 1)
    btn_2.clicked.connect(lambda: display.setText(display.text() + '2'))

    btn_3 = QPushButton('3')
    btn_3.setFixedHeight(50)
    layout.addWidget(btn_3, 3, 2)
    btn_3.clicked.connect(lambda: display.setText(display.text() + '3'))

    btn_sub = QPushButton('-')
    btn_sub.setFixedHeight(50)
    layout.addWidget(btn_sub, 3, 3)
    btn_sub.clicked.connect(lambda: display.setText(display.text() + '-'))

    btn_0 = QPushButton('0')
    btn_0.setFixedHeight(50)
    layout.addWidget(btn_0, 4, 0)
    btn_0.clicked.connect(lambda: display.setText(display.text() + '0'))

    btn_dot = QPushButton('.')
    btn_dot.setFixedHeight(50)
    layout.addWidget(btn_dot, 4, 1)
    btn_dot.clicked.connect(lambda: display.setText(display.text() + '.'))

    btn_clear = QPushButton('C')
    btn_clear.setFixedHeight(50)
    layout.addWidget(btn_clear, 4, 2)
    btn_clear.clicked.connect(display.clear)

    btn_add = QPushButton('+')
    btn_add.setFixedHeight(50)
    layout.addWidget(btn_add, 4, 3)
    btn_add.clicked.connect(lambda: display.setText(display.text() + '+'))

    btn_equal = QPushButton('=')
    btn_equal.setFixedHeight(50)
    layout.addWidget(btn_equal, 5, 0, 1, 4)
    btn_equal.clicked.connect(lambda: display.setText(calculate(display.text())))

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
