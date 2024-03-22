import base64
import markdown
import os
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextBrowser
from PyQt5.QtGui import QImage, QPixmap, QDesktopServices
from PyQt5.QtCore import QUrl

class CreditsWindow(QDialog):
    def __init__(self, markdown_file_path):
        super().__init__()

        self.setWindowTitle("Credits")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)

        # Read the Markdown content from the file
        with open(markdown_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        # Convert Markdown content to HTML
        html_content = markdown.markdown(
            markdown_content, extensions=['markdown.extensions.extra', 'markdown.extensions.admonition'])

        # Modify image paths to use base64 encoding
        html_content = self.modify_image_paths(html_content, os.path.dirname(markdown_file_path))

        # Display HTML content in a QTextBrowser
        text_browser = QTextBrowser(self)
        text_browser.setOpenExternalLinks(True)

        # Set custom resource loader
        text_browser.setHtml(html_content)
        text_browser.anchorClicked.connect(self.open_link)

        layout.addWidget(text_browser)
        self.setLayout(layout)

    def modify_image_paths(self, html_content, base_path):
        def image_loader(match):
            image_path = match.group(2)
            if not image_path.startswith(('http://', 'https://')):
                full_path = os.path.join(base_path, image_path)
                with open(full_path, 'rb') as f:
                    image_data = f.read()
                image_data_base64 = base64.b64encode(image_data).decode('utf-8')
                image_extension = os.path.splitext(image_path)[1][1:]
                return f'<img src="data:image/{image_extension};base64,{image_data_base64}"{match.group(3)}>'
            return match.group(0)

        import re
        pattern = r'<(img)\s+src="([^"]+)"([^>]*)>'
        return re.sub(pattern, image_loader, html_content)

    def open_link(self, url):
        if url.scheme() == 'file':
            QDesktopServices.openUrl(QUrl(url.toString()))
