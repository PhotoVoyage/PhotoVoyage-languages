from PyQt5.QtWidgets import QAction, QMenu

def create_menu(parent):
    menu_bar = parent.menuBar()
    
    # Settings
    file_menu = menu_bar.addMenu('&Settings')
    exit_action = QAction('&Exit', parent)
    exit_action.triggered.connect(parent.close)  # Connect the action to the parent's close function
    file_menu.addAction(exit_action)
    
    # languages menu
    settings_menu = menu_bar.addMenu('&languages')
    download_language_action = QAction('&Download Language', parent)
    settings_menu.addAction(download_language_action)
    credits_action = QAction('&Credits', parent)
    settings_menu.addAction(credits_action)
    
    return menu_bar
