#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
FileDropWidget

Simple widget that allows dropping files for opening

"""

from pyqode.qt import QtWidgets, QtCore


class FileDropWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FileDropWidget, self).__init__(parent)
        self.setAcceptDrops(True)

    fileDropped = QtCore.pyqtSignal(str)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                self.fileDropped.emit(str(url.toLocalFile()))
        else:
            event.acceptProposedAction()
