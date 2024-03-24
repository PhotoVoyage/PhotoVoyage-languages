# Spanish-gen.py

import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon

class SpanishGenerator(QWidget):
    def __init__(self, folder_path):  # Añade folder_path como argumento
        super().__init__()

        self.setWindowTitle("Descargar Archivos")
        self.setGeometry(100, 100, 300, 400)
        icon = QIcon("ico/161897722.ico")
        self.setWindowIcon(icon)

        layout = QVBoxLayout()

        label = QLabel("Archivos traducidos")
        layout.addWidget(label)

        self.word_list = QListWidget()
        layout.addWidget(self.word_list)

        self.download_button = QPushButton("Descargar")
        self.download_button.clicked.connect(self.download_file)
        layout.addWidget(self.download_button)

        self.generate_word_list()

        self.setLayout(layout)

        self.folder_path = folder_path  # Guarda la ruta seleccionada

    def generate_word_list(self):
        palabras = ["404.ejs", "error.ejs", "login.ejs"]

        for palabra in palabras:
            self.word_list.addItem(palabra)

    def download_file(self):
        selected_item = self.word_list.currentItem()
        if selected_item:
            file_name = selected_item.text()
            url = f"https://raw.githubusercontent.com/PhotoVoyage/PhotoVoyage-languages/main/src/languages/Es/{file_name}"
            response = requests.get(url)
            if response.status_code == 200:
                local_path = os.path.join(self.folder_path, file_name)  # Utiliza la ruta seleccionada
                with open(local_path, 'wb') as f:
                    f.write(response.content)
                QMessageBox.information(self, "Descarga Exitosa", f"El archivo '{file_name}' se ha descargado exitosamente.")
            else:
                QMessageBox.warning(self, "Error", f"No se pudo descargar el archivo '{file_name}'")
        else:
            QMessageBox.warning(self, "Error", "Por favor selecciona un archivo para descargar")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    folder_path = sys.argv[1]  # Recibe la ruta seleccionada como argumento
    window = SpanishGenerator(folder_path)
    window.show()
    sys.exit(app.exec_())
