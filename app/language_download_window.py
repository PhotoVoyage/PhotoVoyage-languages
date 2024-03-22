from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QHBoxLayout, QFileDialog, QMessageBox

class LanguageDownloadWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Download Language")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout(self)

        self.label = QLabel("Select language to download:")
        layout.addWidget(self.label)

        self.language_selector = QComboBox()
        self.language_selector.addItem("Spanish")
        self.language_selector.addItem("Japanese")
        self.language_selector.addItem("Russian")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.language_selector)

        select_folder_button = QPushButton("Select Folder")
        select_folder_button.clicked.connect(self.show_file_dialog)
        button_layout.addWidget(select_folder_button)

        self.download_button = QPushButton("Download")
        self.download_button.setEnabled(False)
        self.download_button.clicked.connect(self.download_language)
        button_layout.addWidget(self.download_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        default_folder = "./PhotoVoyage-main"
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory", default_folder, options=options)

        if folder_path:
            print(f"Selected folder: {folder_path}")
            QMessageBox.information(self, "Folder Selected", f"Selected folder: {folder_path}")
            self.selected_folder = folder_path
            self.download_button.setEnabled(True)
            self.label.setText(f"Select language to download:\nSelected folder: {folder_path}")

    def download_language(self):
        if hasattr(self, 'selected_folder'):
            selected_language = self.language_selector.currentText()
            print(f"Downloading language: {selected_language} to folder: {self.selected_folder}")
        else:
            QMessageBox.warning(self, "No Folder Selected", "Please select a folder before downloading.")

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = LanguageDownloadWindow()
    window.show()
    sys.exit(app.exec_())
