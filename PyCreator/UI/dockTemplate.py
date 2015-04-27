#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Dock Base Class
"""
from pyqode.qt import QtWidgets, QtCore


class DockBase(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super(DockBase, self).__init__(parent)

        self.viewAction = QtWidgets.QAction("", self)
        self.viewAction.triggered.connect(self.toggleView)
        self.viewAction.setCheckable(True)
        self.updateStatus()

    @QtCore.Slot()
    def toggleView(self):
        self.setVisible(not self.isVisible())
        self.updateStatus()

    def updateStatus(self):
        self.viewAction.setChecked(self.isVisible())

    def initDock(self, name):
        self.setWindowTitle(name)
        self.setObjectName(name + '_dock')
        self.viewAction.setText(name)

    # function override from parent
    # makes view action update checked status upon creation
    def setVisible(self, vis):
        super(DockBase, self).setVisible(vis)
        self.updateStatus()
