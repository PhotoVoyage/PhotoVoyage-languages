# Russian-gen.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget
from PyQt5.QtGui import QIcon

class RussianGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Русская загрузка")
        self.setGeometry(100, 100, 300, 400)
        icon = QIcon("ico/161897722.ico")
        self.setWindowIcon(icon)

        layout = QVBoxLayout()

        label = QLabel("Список слов на русском:")
        layout.addWidget(label)

        self.word_list = QListWidget()
        layout.addWidget(self.word_list)

        self.generate_word_list()

        self.setLayout(layout)

    def generate_word_list(self):
        words = ["NONE ❌"]

        for word in words:
            self.word_list.addItem(word)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RussianGenerator()
    window.show()
    sys.exit(app.exec_())
