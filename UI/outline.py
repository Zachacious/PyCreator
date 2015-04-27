#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
OutlineDock
"""

from pyqode.qt import QtWidgets
from pyqode.core import widgets
from dockTemplate import DockBase


class OutlineDock(DockBase):
    def __init__(self, parent=None):
        super(OutlineDock, self).__init__(parent)
        self.initDock("Outline")

        self.outlineTree = widgets.OutlineTreeWidget()

        # add everything to the dock
        self.contents = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout(self.contents)
        self.layout.addWidget(self.outlineTree, 0, 0, 1, 1)
        self.setWidget(self.contents)
