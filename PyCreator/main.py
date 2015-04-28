#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
DeliciousPy

- ~To Do~
Type Description

"""

def main():
    import logging
    import sys
    from pyqode.qt.QtWidgets import QApplication
    from UI import MainWindow

    # Logging
    filename = None
    if sys.platform == 'win32':
        filename = 'PyCreator.log'
        logging.basicConfig(level=logging.INFO, filename=filename)  # save log to file

    app = QApplication(sys.argv)

    # ~To Do~
    # create a function to set the style by passing in the app object
    # or load style sheet from file?
    app.setStyle('Fusion')  # Needed to make dark theme look right

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
