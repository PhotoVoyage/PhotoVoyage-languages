import sys
import markdown
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextBrowser, QMessageBox, QWidget
from menu import create_menu

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('PhotoVoyage languages')

        layout = QVBoxLayout()
        
        # Add the menu to the window
        create_menu(self)

        # Upload Markdown content from the file
        try:
            with open('introduction-app.md', 'r', encoding='utf-8') as file:
                markdown_content = file.read()
        except FileNotFoundError:
            QMessageBox.critical(self, 'Error', 'The "introduction-app.md" file was not found.')
            markdown_content = "I'm sorry but it seems that the app intro message was not found, please talk to the development team to fix this as soon as possible"

        # Convert Markdown content to HTML
        html_content = markdown.markdown(markdown_content)

        # Display HTML content in a QTextBrowser
        text_browser = QTextBrowser()
        text_browser.setOpenExternalLinks(True)
        text_browser.setHtml(html_content)

        layout.addWidget(text_browser)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
