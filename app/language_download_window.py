from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QHBoxLayout

class LanguageDownloadWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Download Language")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout(self)

        label = QLabel("Select language to download:")
        layout.addWidget(label)

        self.language_selector = QComboBox()
        self.language_selector.addItem("Spanish")
        self.language_selector.addItem("Japanese")
        self.language_selector.addItem("Russian")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.language_selector)

        download_button = QPushButton("Download")
        download_button.clicked.connect(self.download_language)
        button_layout.addWidget(download_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def download_language(self):
        selected_language = self.language_selector.currentText()
        # Aquí agregarías la lógica para descargar el idioma seleccionado
        print(f"Downloading language: {selected_language}")
        self.close()
