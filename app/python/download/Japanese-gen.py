import sys
import os
import requests
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox

class JapaneseGenerator(QWidget):
    def __init__(self, folder_path):
        super().__init__()

        self.setWindowTitle("日本語ダウンロード")
        self.setGeometry(100, 100, 300, 400)
        icon = QIcon("ico/161897722.ico")
        self.setWindowIcon(icon)

        layout = QVBoxLayout()

        label = QLabel("日本語の単語リスト：")
        layout.addWidget(label)

        self.word_list = QListWidget()
        layout.addWidget(self.word_list)

        self.download_button = QPushButton("ダウンロード")
        self.download_button.clicked.connect(self.download_selected_word)
        layout.addWidget(self.download_button)

        self.generate_word_list()

        self.setLayout(layout)

        self.folder_path = folder_path

    def generate_word_list(self):
        words = ["admin.ejs", "search.ejs"]

        for word in words:
            self.word_list.addItem(word)

    def download_selected_word(self):
        selected_item = self.word_list.currentItem()
        if selected_item:
            word_name = selected_item.text()
            url = f"https://raw.githubusercontent.com/PhotoVoyage/PhotoVoyage-languages/main/src/languages/Jp/{word_name}"
            local_path = os.path.join(self.folder_path, word_name)
            response = requests.get(url)
            if response.status_code == 200:
                with open(local_path, 'wb') as file:
                    file.write(response.content)
                QMessageBox.information(self, "ダウンロード完了", f"{word_name} がダウンロードされました。保存先: {local_path}")
            else:
                QMessageBox.warning(self, "エラー", f"ダウンロードに失敗しました。ステータスコード: {response.status_code}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    folder_path = sys.argv[1]
    window = JapaneseGenerator(folder_path)
    window.show()
    sys.exit(app.exec_())
