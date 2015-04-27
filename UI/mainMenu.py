#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Main Menu
"""

from icons import Icons
from pyqode.qt import QtWidgets
from pyqode.core import widgets
from dockTemplate import DockBase


class MainMenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent=None):
        super(MainMenuBar, self).__init__(parent)
        self.mainWindow = parent  # parent should be a MainWindow

        self.docks = []

        # sub-menus
        self.openRecMenu = \
            widgets.MenuRecentFiles(self,
                                    self.mainWindow.recent_files_manager)

        # must load icons here
        Icons.load()

        # Actions --
        # file actions
        self.newAct = QtWidgets.QAction(Icons.new, "&New", self)
        self.newAct.setShortcut('Ctrl+N')

        self.openAct = QtWidgets.QAction(Icons.openFile, "&Open", self)
        self.openAct.setShortcut('Ctrl+O')
        self.openRecAct = QtWidgets.QAction("Open &Recent", self)
        self.openRecAct.setMenu(self.openRecMenu)

        self.saveAct = QtWidgets.QAction(Icons.save, "&Save", self)
        self.saveAct.setShortcut('Ctrl+S')
        self.saveAsAct = QtWidgets.QAction(Icons.saveAs, "Save &As...", self)
        self.saveAsAct.setShortcut('Ctrl+Shift+S')
        self.saveAllAct = QtWidgets.QAction(Icons.saveAll, "Save A&ll", self)
        self.saveAllAct.setShortcut('Ctrl+Shift+A')

        self.closeAllAct = QtWidgets.QAction("Close All", self)

        self.exitAct = QtWidgets.QAction("E&xit", self)
        self.exitAct.setShortcut('Alt+F4')

        # tool actions
        self.interpAct = QtWidgets.QAction("&Interpreter Config...", self)
        self.runConfigAct = QtWidgets.QAction(Icons.runConfig,
                                              "Run &Config...", self)
        self.runAct = QtWidgets.QAction(Icons.run, "&Run", self)
        self.runAct.setShortcut('F5')

        # Top-level menus
        self.fileMenu = QtWidgets.QMenu("&File", self)
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.openRecAct)
        self.fileMenu.addAction(self.closeAllAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addAction(self.saveAllAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)
        self.addAction(self.fileMenu.menuAction())  # add to menubar

        self.editMenu = \
            QtWidgets.QMenu("&Edit", self)  # edit menu updated dynamically
        # self.editMenu.addActions(self.mainWindow.editor.actions())
        self.addAction(self.editMenu.menuAction())

        self.toolsMenu = QtWidgets.QMenu("&Tools", self)
        self.toolsMenu.addAction(self.interpAct)
        self.toolsMenu.addAction(self.runConfigAct)
        self.toolsMenu.addAction(self.runAct)
        self.toolsMenu.addSeparator()
        self.addAction(self.toolsMenu.menuAction())

        self.viewMenu = QtWidgets.QMenu("&View", self)
        self.addAction(self.viewMenu.menuAction())

        self.helpMenu = QtWidgets.QMenu("&Help", self)
        self.addAction(self.helpMenu.menuAction())

    def addDock(self, dock):
        assert isinstance(dock, DockBase)
        self.viewMenu.addAction(dock.viewAction)
        self.docks.append(dock)

    def updateViewMenu(self):
        for dock in self.docks:
            dock.updateStatus()
