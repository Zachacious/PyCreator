#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
DockWidget Template

    A fully functional file browser with drag and drop
    and the ability to open files in the editor.
    The folder button allows you to set the
    current directory or move up one directory.
    The context menu(right click) has basic file operations plus
    the ability to add new files and execute scripts and
    programs.
    
    ~To Do~
    Add new file templates to the New submenu

"""

import os
from pyqode.qt import QtWidgets, QtCore
from pyqode.core import widgets
import utils
from dockTemplate import DockBase
from icons import Icons
# from pylint import lint
# from pylint.reporters.text import TextReporter

# ===-------------------------------------===


class WritableObject(object):
    def __init__(self):
        self.content = []

    def write(self, value):
        self.content.append(value)

    def read(self):
        return self.content

# ===-------------------------------------===


class FileBrowserMenu(widgets.FileSystemContextMenu):
    """
        Class FileBrowserMenu(FileBrowserDock dock = None)

        param: dock - the dock that the menu is for.

        This is the context menu for the file browser.
        It inherits the FileSystemContextMenu from pyqode.core.widgets
        and adds the execute and open actions.
    """
    def __init__(self):
        super(FileBrowserMenu, self).__init__()

        self.OpenAction = QtWidgets.QAction('&Open', self)
        self.OpenAction.setShortcut('Ctrl+Shift+O')
        # self.execAction.setIcon(_icon(
        #     'edit-cut', ':/pyqode-icons/rc/edit-cut.png'))
        self.addAction(self.OpenAction)

        self.addSeparator()

        # actions
        self.execAction = QtWidgets.QAction('&Execute', self)
        self.execAction.setShortcut('Shift+Ctrl+Alt+X')
        # self.execAction.setIcon(_icon(
        #     'edit-cut', ':/pyqode-icons/rc/edit-cut.png'))
        self.addAction(self.execAction)
        self.execAction.triggered.connect(self.execFile)

        # self.addSeparator()

        # self.pylintAction = QtWidgets.QAction('Run P&ylint', self)
        # self.addAction(self.pylintAction)

    @QtCore.pyqtSlot()
    def execFile(self):
        """execFile() -- execute the selected file in the browser."""
        if self.tree_view is not None:  # FileSystemContextMenu.tree_view
            urls = self.tree_view.helper.selected_urls()
            # execute all selected
            for u in urls:
                if os.path.isfile(u):
                    os.startfile(u)

# ===-------------------------------------===


class DirMenu(QtWidgets.QMenu):
    """
    Class DirMenu()
    
    - The context menu for the folder button.
    - action to open a directory and to move up to parent
    folder.
    """
    def __init__(self):
        super(DirMenu, self).__init__()

        # Actions
        self.parentDirAction = QtWidgets.QAction('Parent Directory', self)
        self.addAction(self.parentDirAction)

        self.openDirAction = QtWidgets.QAction('Open &Directory...', self)
        self.addAction(self.openDirAction)


# ===-------------------------------------===

class FileBrowserDock(DockBase):
    """ FileBrowserDock(QtWidgets.QWidget parent = None,
                        Function openFunc = None)

        params: parent - parent widget
               openFunction - function used for open file commands
               
        desc: The dockwidget containing all the elements of the
              of a file browser.
    """

    pylint_finished = QtCore.pyqtSignal(WritableObject)

    def __init__(self, parent=None):
        super(FileBrowserDock, self).__init__(parent)

        self.initDock("File Browser")

        # make sure icons are loaded
        Icons.load()

        # self.openFunction = openFunc

        # tree view
        self.fileTree = widgets.FileSystemTreeView()
        self.fileTree.set_root_path(os.getcwd())
        self.contextMenu = FileBrowserMenu()
        self.fileTree.set_context_menu(self.contextMenu)

        # enable drag and drop
        self.fileTree.setDragEnabled(True)
        self.fileTree.setDragDropMode(
            QtWidgets.QAbstractItemView.DragDrop)
        self.fileTree.viewport().setAcceptDrops(True)
        self.fileTree.setDropIndicatorShown(True)
        # To Do -- not use a private member --
        self.fileTree._fs_model_source.setReadOnly(False)
        self.fileTree.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fileTree.setDefaultDropAction(QtCore.Qt.MoveAction)

        # Folder button
        self.menuHLayout = QtWidgets.QHBoxLayout()
        self.menuHLayout.setContentsMargins(1, 1, 1, 1)
        self.menuHLayout.addStretch(1)
        self.menuBtn = QtWidgets.QPushButton(Icons.folder, "...", self)
        self.menuBtn.setFlat(True)
        self.menuBtn.setStyleSheet("background-color: "
                                   "rgba(255, 255, 255, 0);")
        self.menuHLayout.addWidget(self.menuBtn)
        self.menuVLayout = QtWidgets.QVBoxLayout()
        self.menuVLayout.setContentsMargins(1, 1, 1, 1)
        self.menuVLayout.addLayout(self.menuHLayout)
        self.menuVLayout.addStretch(1)
        self.fileTree.setLayout(self.menuVLayout)

        self.dirContextMenu = DirMenu()
        self.menuBtn.setMenu(self.dirContextMenu)

        self.dirContextMenu.parentDirAction.triggered.connect(
            self.onParentDirClicked)
        self.dirContextMenu.openDirAction.triggered.connect(
            self.onOpenDirClicked)

        # add everything to the dock
        self.contents = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout(self.contents)
        self.layout.addWidget(self.fileTree, 0, 0, 1, 1)
        self.setWidget(self.contents)

        self.fileTree.doubleClicked.connect(self.onOpenItem)
        self.contextMenu.OpenAction.triggered.connect(self.openFile)
        # self.contextMenu.pylintAction.triggered.connect(self.runPyLint)
        # self.hide()

    # global signal
    fileOpenRequest = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot()
    def openFile(self):
        """openFile() -- open selected file in editor."""
        if self.fileTree is not None:
            urls = self.fileTree.helper.selected_urls()
            # Open all selected files
            for u in urls:
                if os.path.isfile(u):  # make sure it is a file
                    self.fileOpenRequest.emit(u)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def onOpenItem(self, index):
        """ onOpenItem(index)"""
        # if self.openFunction != None:
        filePath = self.fileTree.filePath(index)
        self.fileOpenRequest.emit(filePath)
        # self.openFunction(filePath)

    @QtCore.pyqtSlot()
    def onParentDirClicked(self):
        """ Move file browser root up to parent directory."""
        # There has to be a better way to do this
        # if not then shame on python
        path = utils.rectifyPath(self.fileTree.root_path)
        parPath = utils.getParentDir(path)
        if os.path.isdir(parPath):
            self.fileTree.set_root_path(parPath)

    @QtCore.pyqtSlot()
    def onOpenDirClicked(self):
        """ Open a new directory in the file browser"""
        # Open folder dialog -- only allow folders
        path = str(QtWidgets.QFileDialog.getExistingDirectory(
                    self, "Select Directory", self.fileTree.root_path,
                    QtWidgets.QFileDialog.ShowDirsOnly |
                    QtWidgets.QFileDialog.DontUseNativeDialog))
        utils.rectifyPath(path)
        if os.path.isdir(path):
            self.fileTree.set_root_path(path)

    # @QtCore.pyqtSlot()
    # def runPyLint(self):
    #     args = ""
    #     (args, ok) = QtWidgets.QInputDialog.getText(
    #                       self,
    #                       "PyLint Arguments",
    #                       "Input arguments")

    #     argList = []
    #     if args is None:
    #         args = '-j 0'
    #     if ',' in args:
    #         for a in args.split(','):
    #             argList.append(a)
    #     else:
    #         argList.append(args)

    #     argPath = ""
    #     path = ""

    #     if self.fileTree is not None:
    #         urls = self.fileTree.helper.selected_urls()
    #         for u in urls:
    #             path = utils.rectifyPath(u)
    #             print path
    #             if os.path.isfile(path) or os.path.isdir(path):
    #                 # args += path + " "
    #                 argPath += (path + " ")
    #         output = WritableObject()
    #         lint.Run([argPath]+argList, reporter=TextReporter(output),
    #                  exit=False)
    #         self.pylint_finished.emit(output)
