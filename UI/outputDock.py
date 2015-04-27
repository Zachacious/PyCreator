#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
OutPut Dock
"""
from pyqode.python.widgets import PyInteractiveConsole
from pyqode.qt import QtWidgets
from dockTemplate import DockBase


class OutputDock(DockBase):
    def __init__(self, parent=None):
        super(OutputDock, self).__init__(parent)
        self.initDock("Output")

        self.iconsole = PyInteractiveConsole(self)
        self.iconsole.setLineWrapMode(self.iconsole.WidgetWidth)

        self.contents = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout(self.contents)
        self.layout.addWidget(self.iconsole, 0, 0, 1, 1)
        self.setWidget(self.contents)
