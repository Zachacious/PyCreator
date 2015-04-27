#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Main UI

- ~To Do~
Type Description

"""

from pyqode.qt import QtCore, QtGui, QtWidgets
from pyqode.python.widgets import PyInteractiveConsole
from pyqode.core.widgets.outline import OutlineTreeWidget
from pyqode.core.widgets import SplittableCodeEditTabWidget
from fileDropWidget import FileDropWidget

class MainUI(object):
    def setupUi(self, MainWindow):
        """ setupUi(QMainWindow MainWindow)
        
            -Creates all the ui components for MainWindow.
            -MainWindow will be the object that Inherits this class.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(":/icons/pyqode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # MainWindow.setWindowIcon(icon)
        
        # central widget
        self.centralwidget = FileDropWidget(MainWindow)  
        self.centralwidget.setObjectName("centralwidget")
        
        # main layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        
        # Splittable Tabs
        self.tabWidget = SplittableCodeEditTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # menubar
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 27))
        # self.menubar.setObjectName("menubar")
        # self.menuFile = QtWidgets.QMenu(self.menubar)
        # self.menuFile.setObjectName("menuFile") 
        # self.menuPython_interpreter = QtWidgets.QMenu(self.menuFile)
        # self.menuPython_interpreter.setObjectName("menuPython_interpreter")
        # self.menuEdit = QtWidgets.QMenu(self.menubar)
        # self.menuEdit.setObjectName("menuEdit")
        # self.menuModes = QtWidgets.QMenu(self.menubar)
        # self.menuModes.setObjectName("menuModes")
        # self.menuPanels = QtWidgets.QMenu(self.menubar)
        # self.menuPanels.setObjectName("menuPanels")
        # self.menu = QtWidgets.QMenu(self.menubar)
        # self.menu.setObjectName("menu")
        # MainWindow.setMenuBar(self.menubar)
        
        # statusbar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # toolbar
        # self.toolBar = QtWidgets.QToolBar(MainWindow)
        # self.toolBar.setObjectName("toolBar")
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        # dock widgets
        # self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        # self.dockWidget.setObjectName("dockWidget")
        # self.dockWidgetContents = QtWidgets.QWidget()
        # self.dockWidgetContents.setObjectName("dockWidgetContents")
        # 
        # self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        # self.gridLayout_2.setObjectName("gridLayout_2")
        # 
        # self.interactiveConsole = PyInteractiveConsole(self.dockWidgetContents)
        # self.interactiveConsole.setObjectName("interactiveConsole")
        # 
        # self.gridLayout_2.addWidget(self.interactiveConsole, 0, 0, 1, 1)
        # self.dockWidget.setWidget(self.dockWidgetContents)
        # MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        # 
        # self.dockWidgetOutline = QtWidgets.QDockWidget(MainWindow)
        # self.dockWidgetOutline.setObjectName("dockWidgetOutline")
        # self.dockWidgetContents_2 = QtWidgets.QWidget()
        # self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        # self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        # self.gridLayout_3.setObjectName("gridLayout_3")
        # self.widgetOutline = OutlineTreeWidget(self.dockWidgetContents_2)
        # self.widgetOutline.setObjectName("widgetOutline")
        # self.gridLayout_3.addWidget(self.widgetOutline, 0, 0, 1, 1)
        # self.dockWidgetOutline.setWidget(self.dockWidgetContents_2)
        # MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetOutline)
        
        #actions
        # self.actionNew = QtWidgets.QAction(MainWindow)
        # # icon1 = QtGui.QIcon()
        # # icon1.addPixmap(QtGui.QPixmap(":/icons/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # #self.actionNew.setIcon(icon1)
        # #self.actionNew.setIconVisibleInMenu(True)
        # self.actionNew.setObjectName("actionNew")
        # 
        # self.actionOpen = QtWidgets.QAction(MainWindow)
        # # icon2 = QtGui.QIcon()
        # # icon2.addPixmap(QtGui.QPixmap(":/icons/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # # self.actionOpen.setIcon(icon2)
        # # self.actionOpen.setIconVisibleInMenu(True)
        # self.actionOpen.setObjectName("actionOpen")
        # 
        # self.actionSave = QtWidgets.QAction(MainWindow)
        # # icon3 = QtGui.QIcon()
        # # icon3.addPixmap(QtGui.QPixmap(":/icons/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # # self.actionSave.setIcon(icon3)
        # # self.actionSave.setIconVisibleInMenu(True)
        # self.actionSave.setObjectName("actionSave")
        # 
        # self.actionSave_as = QtWidgets.QAction(MainWindow)
        # # icon4 = QtGui.QIcon()
        # # icon4.addPixmap(QtGui.QPixmap(":/icons/document-save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # # self.actionSave_as.setIcon(icon4)
        # # self.actionSave_as.setIconVisibleInMenu(True)
        # self.actionSave_as.setObjectName("actionSave_as")
        # 
        # self.actionQuit = QtWidgets.QAction(MainWindow)
        # # icon5 = QtGui.QIcon()
        # # icon5.addPixmap(QtGui.QPixmap(":/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # # self.actionQuit.setIcon(icon5)
        # # self.actionQuit.setIconVisibleInMenu(True)
        # self.actionQuit.setObjectName("actionQuit")
        # 
        # self.actionAbout = QtWidgets.QAction(MainWindow)
        # # icon6 = QtGui.QIcon()
        # # icon6.addPixmap(QtGui.QPixmap(":/icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # # self.actionAbout.setIcon(icon6)
        # # self.actionAbout.setIconVisibleInMenu(True)
        # self.actionAbout.setObjectName("actionAbout")
        # 
        # self.actionRun = QtWidgets.QAction(MainWindow)
        # # icon7 = QtGui.QIcon()
        # # icon7.addPixmap(QtGui.QPixmap(":/icons/Gnome-Media-Playback-Start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # # self.actionRun.setIcon(icon7)
        # # self.actionRun.setIconVisibleInMenu(True)
        # self.actionRun.setObjectName("actionRun")
        # 
        # self.actionConfigure_run = QtWidgets.QAction(MainWindow)
        # # icon8 = QtGui.QIcon()
        # # icon8.addPixmap(QtGui.QPixmap(":/icons/Gnome-System-Run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # # self.actionConfigure_run.setIcon(icon8)
        # # self.actionConfigure_run.setIconVisibleInMenu(True)
        # self.actionConfigure_run.setObjectName("actionConfigure_run")
        # 
        # self.actionPython_2 = QtWidgets.QAction(MainWindow)
        # self.actionPython_2.setObjectName("actionPython_2")
        # 
        # self.actionPython_3 = QtWidgets.QAction(MainWindow)
        # self.actionPython_3.setObjectName("actionPython_3")
        # 
        # self.menuFile.addAction(self.actionNew)
        # self.menuFile.addAction(self.actionOpen)
        # self.menuFile.addAction(self.actionSave)
        # self.menuFile.addAction(self.actionSave_as)
        # self.menuFile.addSeparator()
        # self.menuFile.addAction(self.actionConfigure_run)
        # self.menuFile.addAction(self.actionRun)
        # self.menuFile.addSeparator()
        # self.menuFile.addAction(self.menuPython_interpreter.menuAction())
        # self.menuFile.addSeparator()
        # self.menuFile.addAction(self.actionQuit)
        # self.menu.addAction(self.actionAbout)
        # self.menubar.addAction(self.menuFile.menuAction())
        # self.menubar.addAction(self.menuEdit.menuAction())
        # self.menubar.addAction(self.menuModes.menuAction())
        # self.menubar.addAction(self.menuPanels.menuAction())
        # self.menubar.addAction(self.menu.menuAction())
        # self.toolBar.addAction(self.actionNew)
        # self.toolBar.addAction(self.actionOpen)
        # self.toolBar.addSeparator()
        # self.toolBar.addAction(self.actionSave)
        # self.toolBar.addAction(self.actionSave_as)
        # self.toolBar.addSeparator()
        # self.toolBar.addAction(self.actionConfigure_run)
        # self.toolBar.addAction(self.actionRun)

        # self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "PyCreator"))
        # self.menuFile.setTitle(_translate("MainWindow", "File"))
        # self.menuPython_interpreter.setTitle(_translate("MainWindow", "Python interpreter"))
        # self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        # self.menuModes.setTitle(_translate("MainWindow", "Modes"))
        # self.menuPanels.setTitle(_translate("MainWindow", "Panels"))
        # self.menu.setTitle(_translate("MainWindow", "?"))
        # self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        # self.toolBar.setToolTip(_translate("MainWindow", "Configure run action for current editor"))
        # #self.dockWidget.setWindowTitle(_translate("MainWindow", "Run output"))
        # #self.dockWidgetOutline.setWindowTitle(_translate("MainWindow", "Structure"))
        # self.actionNew.setText(_translate("MainWindow", "New"))
        # self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        # self.actionOpen.setText(_translate("MainWindow", "Open"))
        # self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        # self.actionSave.setText(_translate("MainWindow", "Save"))
        # self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        # self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        # self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        # self.actionQuit.setText(_translate("MainWindow", "Quit"))
        # self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        # self.actionAbout.setText(_translate("MainWindow", "About"))
        # self.actionAbout.setShortcut(_translate("MainWindow", "F1"))
        # self.actionRun.setText(_translate("MainWindow", "Run"))
        # self.actionRun.setToolTip(_translate("MainWindow", "Run current script"))
        # self.actionConfigure_run.setText(_translate("MainWindow", "Configure run"))
        # self.actionPython_2.setText(_translate("MainWindow", "Python 2"))
        # self.actionPython_3.setText(_translate("MainWindow", "Python 3"))
