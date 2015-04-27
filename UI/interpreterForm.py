# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './PyCook\UI\interpreterForm.ui'
#
# Created: Wed Apr 22 22:33:58 2015
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InterpreterDlg(object):
    def setupUi(self, InterpreterDlg):
        InterpreterDlg.setObjectName("InterpreterDlg")
        InterpreterDlg.setWindowModality(QtCore.Qt.ApplicationModal)
        InterpreterDlg.resize(345, 203)
        InterpreterDlg.setWindowFilePath("")
        InterpreterDlg.setSizeGripEnabled(False)
        InterpreterDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(InterpreterDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(InterpreterDlg)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.autoWidget = QtWidgets.QWidget(self.groupBox)
        self.autoWidget.setObjectName("autoWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.autoWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.autoRB = QtWidgets.QRadioButton(self.autoWidget)
        self.autoRB.setChecked(True)
        self.autoRB.setObjectName("autoRB")
        self.verticalLayout_2.addWidget(self.autoRB)
        self.autoLabel = QtWidgets.QLabel(self.autoWidget)
        self.autoLabel.setObjectName("autoLabel")
        self.verticalLayout_2.addWidget(self.autoLabel)
        self.verticalLayout_4.addWidget(self.autoWidget)
        self.locWidget = QtWidgets.QWidget(self.groupBox)
        self.locWidget.setObjectName("locWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.locWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.locRB = QtWidgets.QRadioButton(self.locWidget)
        self.locRB.setObjectName("locRB")
        self.verticalLayout_3.addWidget(self.locRB)
        self.locHLayout = QtWidgets.QHBoxLayout()
        self.locHLayout.setObjectName("locHLayout")
        self.locLE = QtWidgets.QLineEdit(self.locWidget)
        self.locLE.setObjectName("locLE")
        self.locHLayout.addWidget(self.locLE)
        self.locBtn = QtWidgets.QToolButton(self.locWidget)
        self.locBtn.setObjectName("locBtn")
        self.locHLayout.addWidget(self.locBtn)
        self.verticalLayout_3.addLayout(self.locHLayout)
        self.verticalLayout_4.addWidget(self.locWidget)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(InterpreterDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(InterpreterDlg)
        self.buttonBox.accepted.connect(InterpreterDlg.accept)
        self.buttonBox.rejected.connect(InterpreterDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(InterpreterDlg)

    def retranslateUi(self, InterpreterDlg):
        _translate = QtCore.QCoreApplication.translate
        InterpreterDlg.setWindowTitle(_translate("InterpreterDlg", "Interpreter Config"))
        self.groupBox.setTitle(_translate("InterpreterDlg", "Python Interpreter Location"))
        self.autoRB.setText(_translate("InterpreterDlg", "Automatic(default) "))
        self.autoLabel.setText(_translate("InterpreterDlg", "Use environmental variable to automatically find python.exe"))
        self.locRB.setText(_translate("InterpreterDlg", "Locate python.exe manually"))
        self.locBtn.setText(_translate("InterpreterDlg", "..."))

