from PyQt5.QtWidgets import QAction, QMenu
from credits_window import CreditsWindow

def create_menu(parent):
    menu_bar = parent.menuBar()
    
    # File menu
    file_menu = menu_bar.addMenu('&Settings')
    exit_action = QAction('&Exit', parent)
    exit_action.triggered.connect(parent.close)
    file_menu.addAction(exit_action)
    
    # Languages menu (renamed from Help)
    settings_menu = menu_bar.addMenu('&Languages')
    download_language_action = QAction('&Download Language', parent)
    settings_menu.addAction(download_language_action)
    
    # Credits action
    credits_action = QAction('&Credits', parent)
    credits_action.triggered.connect(lambda: show_credits(parent))
    settings_menu.addAction(credits_action)
    
    return menu_bar

def show_credits(parent):
    credits_window = CreditsWindow("md/credits.md")
    credits_window.exec_()
