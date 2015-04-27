#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
DeliciousPy

- ~To Do~
Type Description

"""


import logging
import sys
from pyqode.qt.QtWidgets import QApplication
from PyCreator.UI import MainWindow

# Logging
filename = None
if sys.platform == 'win32':
    filename = 'PyCreator.log'
logging.basicConfig(level=logging.INFO, filename=filename)  # save log to file


# create and exec main qt app
if __name__ == '__main__':

    app = QApplication(sys.argv)

    # ~To Do~
    # create a function to set the style by passing in the app object
    # or load style sheet from file?
    app.setStyle('Fusion')  # Needed to make dark theme look right

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
