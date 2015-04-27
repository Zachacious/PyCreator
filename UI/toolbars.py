#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Main ToolBars
"""
from pyqode.qt import QtWidgets, QtCore
from mainMenu import MainMenuBar
from pyqode.core.api.code_edit import CodeEdit
from icons import Icons


class ToolBars(object):

    @classmethod
    def initFileBar(cls, fBar, menuBar):
        assert isinstance(fBar, QtWidgets.QToolBar)
        assert isinstance(menuBar, MainMenuBar)
        fBar.clear()
        fBar.setIconSize(QtCore.QSize(16, 16))
        fBar.addAction(menuBar.newAct)
        fBar.addAction(menuBar.openAct)
        fBar.addAction(menuBar.saveAct)
        fBar.addAction(menuBar.saveAsAct)
        fBar.addAction(menuBar.saveAllAct)

    @classmethod
    def initEditBar(cls, eBar, editor):
        if editor is not None:
            assert isinstance(eBar, QtWidgets.QToolBar)
            assert isinstance(editor, CodeEdit)
            eBar.clear()
            eBar.setIconSize(QtCore.QSize(16, 16))
            eBar.addActions(editor.actions())
            # add a few specific icons
            for action in eBar.actions():
                if action.iconText() == 'Show documentation':
                    action.setIcon(Icons.doc)
                elif action.iconText() == "Comment/Uncomment":
                    action.setIcon(Icons.comment)
                elif action.iconText() == "Go to assignments":
                    action.setIcon(Icons.gotoAssign)
                elif action.iconText() == "Duplicate line":
                    action.setIcon(Icons.dupLine)

    @classmethod
    def initToolsBar(cls, tBar, menuBar):
        assert isinstance(tBar, QtWidgets.QToolBar)
        assert isinstance(menuBar, MainMenuBar)
        tBar.clear()
        tBar.setIconSize(QtCore.QSize(16, 16))
        tBar.addAction(menuBar.runConfigAct)
        tBar.addAction(menuBar.runAct)
