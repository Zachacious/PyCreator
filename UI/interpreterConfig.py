#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Interpreter config dialog(modal)
"""

from pyqode.qt import QtWidgets, QtCore
from interpreterForm import Ui_InterpreterDlg
import utils
from settings import Settings


class InterpreterConfigDialog(QtWidgets.QDialog, Ui_InterpreterDlg):
    def __init__(self, parent=None):
        super(InterpreterConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.autoRB.toggled.connect(self.onAutoToggled)
        self.locRB.toggled.connect(self.onLocToggled)
        self.locBtnAction = QtWidgets.QAction("...", self)
        self.locBtn.setDefaultAction(self.locBtnAction)
        self.locBtn.triggered.connect(self.onLocBtn)
        self._loadSettings()
        self._updateWidgets()

    def _loadSettings(self):
        iconfig = Settings().interpreterConfig
        self.locRB.setChecked(iconfig[Settings().IConfigOption])
        self.locLE.setText(iconfig[Settings().IConfigPath])

    @QtCore.pyqtSlot(bool)
    def onAutoToggled(self, toggle):
        self.locRB.setChecked(not toggle)
        self._updateWidgets()

    @QtCore.pyqtSlot(bool)
    def onLocToggled(self, toggle):
        self.autoRB.setChecked(not toggle)
        self._updateWidgets()

    def _updateWidgets(self):
        """Disable the unchecked widget"""
        self.autoLabel.setEnabled(self.autoRB.isChecked())
        self.locLE.setEnabled(self.locRB.isChecked())
        self.locBtn.setEnabled(self.locRB.isChecked())

    @QtCore.pyqtSlot()
    def onLocBtn(self):
        path = QtWidgets.QFileDialog.getOpenFileName(
                    self, "Select python.exe", self.locLE.text(),
                    "Python Interpreter (*.exe)", "*.exe",
                    QtWidgets.QFileDialog.DontUseNativeDialog)
        if path is not None:
            p = utils.rectifyPath(path[0])
            self.locLE.setText(p)

    @staticmethod
    def run(self, parent=None):
        dlg = InterpreterConfigDialog(parent)
        result = dlg.exec_()
        if result == QtWidgets.QDialog.Accepted:
            iconfig = [int(dlg.locRB.isChecked()),
                       str(dlg.locLE.text())]
            Settings().interpreterConfig = iconfig
            return True
        return False
