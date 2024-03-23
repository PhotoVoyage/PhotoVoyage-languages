# Japanese-gen.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget

class JapaneseGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("日本語ダウンロード")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        label = QLabel("日本語の単語リスト：")
        layout.addWidget(label)

        self.word_list = QListWidget()
        layout.addWidget(self.word_list)

        self.generate_word_list()

        self.setLayout(layout)

    def generate_word_list(self):
        words = ["こんにちは", "世界", "猫", "犬", "家"]

        for word in words:
            self.word_list.addItem(word)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JapaneseGenerator()
    window.show()
    sys.exit(app.exec_())
