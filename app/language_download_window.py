from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QHBoxLayout, QFileDialog

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
        download_button.clicked.connect(self.show_file_dialog)
        button_layout.addWidget(download_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def show_file_dialog(self):
        selected_language = self.language_selector.currentText()

        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        default_folder = "./PhotoVoyage-main"
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory", default_folder, options=options)

        if folder_path:
            print(f"Selected folder: {folder_path}")
