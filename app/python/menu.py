from PyQt5.QtWidgets import QAction, QMenu
from credits_window import CreditsWindow
from language_download_window import LanguageDownloadWindow

def create_menu(parent):
    menu_bar = parent.menuBar()
    
    # File menu
    file_menu = menu_bar.addMenu('&Settings')
    exit_action = QAction('&Exit', parent)
    exit_action.triggered.connect(parent.close)
    file_menu.addAction(exit_action)
    
    # Languages menu (renamed from Help)
    settings_menu = menu_bar.addMenu('&Languages')

    # Download Language action
    download_language_action = QAction('&Download Language', parent)
    download_language_action.triggered.connect(lambda: show_language_download(parent))
    settings_menu.addAction(download_language_action)
    
    # Credits action
    credits_action = QAction('&Credits', parent)
    credits_action.triggered.connect(lambda: show_credits(parent))
    settings_menu.addAction(credits_action)
    
    return menu_bar

def show_credits(parent):
    credits_window = CreditsWindow("md/credits.md")
    credits_window.exec_()

def show_language_download(parent):
    language_download_window = LanguageDownloadWindow()
    language_download_window.exec_()
