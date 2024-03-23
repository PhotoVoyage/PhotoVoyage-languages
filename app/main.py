import sys
import markdown
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextBrowser, QMessageBox, QWidget, QAction, QDialog, QLabel, QLineEdit, QPushButton
from menu import create_menu
import uuid
import hashlib

class LicenseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Enter License')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel('Enter License Key:')
        self.license_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(self.license_edit)

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.submitLicense)
        layout.addWidget(submit_button)

        generate_button = QPushButton('Generate License')
        generate_button.clicked.connect(self.generateLicense)
        layout.addWidget(generate_button)

        self.setLayout(layout)

    def submitLicense(self):
        license_key = self.license_edit.text()
        # Here you should validate the license key.
        # For simplicity, let's assume the license key is valid if it's not empty.
        if license_key:
            # Aquí deberías comparar la clave ingresada con la clave generada
            if license_key == MiVentana.generated_license_key:
                self.accept()
            else:
                QMessageBox.warning(self, 'Invalid License', 'Please enter a valid license key.')
        else:
            QMessageBox.warning(self, 'Invalid License', 'Please enter a valid license key.')

    def generateLicense(self):
        # Generar la clave y almacenarla en la variable de clase
        MiVentana.generated_license_key = generate_license_key()
        self.license_edit.setText(MiVentana.generated_license_key)  # Mostrar la clave generada en el campo de texto
        QMessageBox.information(self, 'New License Generated', 'A new license has been generated. Remember, licenses are for one-time use only.')

def generate_license_key():
    # Genera un UUID único
    unique_id = str(uuid.uuid4())

    # Aplica una función hash a UUID para obtener una clave más corta
    hashed_id = hashlib.sha256(unique_id.encode()).hexdigest()

    # Formatea la clave para que sea más legible o con un formato específico si lo deseas
    formatted_key = '-'.join(hashed_id[i:i+4] for i in range(0, len(hashed_id), 4))

    return formatted_key

class MiVentana(QMainWindow):
    generated_license_key = None  # Variable de clase para almacenar la clave generada

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
            with open('md/introduction-app.md', 'r', encoding='utf-8') as file:
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

        # Prompt for license key
        license_dialog = LicenseDialog(self)
        if license_dialog.exec_() == QDialog.Accepted:
            # User entered a valid license key
            print("License validated. Allowing access...")
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
