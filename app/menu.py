from PyQt5.QtWidgets import QAction, QMenu

def create_menu(parent):
    menu_bar = parent.menuBar()
    
    # File menu
    file_menu = menu_bar.addMenu('&File')
    new_action = QAction('&New', parent)
    file_menu.addAction(new_action)
    
    # Edit menu
    edit_menu = menu_bar.addMenu('&Edit')
    cut_action = QAction('&Cut', parent)
    edit_menu.addAction(cut_action)
    copy_action = QAction('&Copy', parent)
    edit_menu.addAction(copy_action)
    paste_action = QAction('&Paste', parent)
    edit_menu.addAction(paste_action)
    
    return menu_bar
