# Spanish-gen.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget

class SpanishGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Descargar Archivos")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        label = QLabel("Archivos traducidos")
        layout.addWidget(label)

        self.word_list = QListWidget()
        layout.addWidget(self.word_list)

        self.generate_word_list()

        self.setLayout(layout)

    def generate_word_list(self):
        palabras = ["404.ejs", "error.ejs", "login.ejs"]

        for palabra in palabras:
            self.word_list.addItem(palabra)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpanishGenerator()
    window.show()
    sys.exit(app.exec_())
