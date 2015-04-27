#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
MainWindow

- ~To Do~
Type Description

"""

import os
import sys
from pyqode.core.api import TextHelper
from pyqode.qt import QtCore
from pyqode.qt import QtWidgets
from pyqode.core import widgets
from pythonEditor import PythonEditor
from pyqode.core.widgets import TextCodeEdit
from pyqode.python import modes
from main_ui import MainUI
from settings import Settings
from fileBrowser import FileBrowserDock, WritableObject
from outline import OutlineDock
from mainMenu import MainMenuBar
import utils
from interpreterConfig import InterpreterConfigDialog
from outputDock import OutputDock
from toolbars import ToolBars
from fileDropWidget import FileDropWidget
from pyqode.core.widgets import SplittableCodeEditTabWidget


class MainWindow(QtWidgets.QMainWindow, MainUI):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyCreator")
        self.setObjectName("MainWindow")
        self.resize(1000, 700)

        # filedropwidget allows file drops on main window
        self.centralwidget = FileDropWidget(self)
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

        self.setCentralWidget(self.centralwidget)

        # statusbar
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # tabWidget
        self.tabWidget.register_code_edit(PythonEditor)
        self.tabWidget.register_code_edit(TextCodeEdit)
        self.tabWidget.current_changed.connect(self.on_current_tab_changed)
        self.tabWidget.last_tab_closed.connect(self.on_last_tab_closed)

        # Output Dock
        self.outputDock = OutputDock()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.outputDock)
        self.outputDock.iconsole.open_file_requested.connect(self.open_file)
        self.outputDock.iconsole.process_finished.connect(
            self.on_process_finished)

        # File Browser Dock
        self.fileBrowser = FileBrowserDock()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.fileBrowser)
        self.fileBrowser.fileOpenRequest.connect(self.open_file)
        self.fileBrowser.pylint_finished.connect(self.pylintFinished)

        # Outline Dock
        self.outlineTreeDock = OutlineDock()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.outlineTreeDock)

        # Handle file drops on main widget
        self.centralwidget.fileDropped.connect(self.onFileDropped)

        self.recent_files_manager = widgets.RecentFilesManager(
             'Zach Moore', 'PyCreator')

        # menuBar setup
        self.menuBar = MainMenuBar(self)
        self.setMenuBar(self.menuBar)
        # menu connections
        self.menuBar.newAct.triggered.connect(self.on_new)
        self.menuBar.openAct.triggered.connect(self.on_open)
        self.menuBar.openRecMenu.open_requested.connect(self.open_file)
        self.menuBar.closeAllAct.triggered.connect(
            self.tabWidget.main_tab_widget.close_all)
        self.menuBar.saveAct.triggered.connect(self.on_save)
        self.menuBar.saveAsAct.triggered.connect(self.on_save_as)
        self.menuBar.saveAllAct.triggered.connect(self.on_save_all)
        self.menuBar.exitAct.triggered.connect(
            QtWidgets.QApplication.instance().quit)
        self.menuBar.runConfigAct.triggered.connect(self.on_configure_run)
        self.menuBar.runAct.triggered.connect(self.on_run)
        self.menuBar.interpAct.triggered.connect(self.onInterpConfig)

        self.setup_status_bar_widgets()
        self.on_current_tab_changed()

        # add docks to view menu
        self.menuBar.addDock(self.outlineTreeDock)
        self.menuBar.addDock(self.outputDock)
        self.menuBar.addDock(self.fileBrowser)

        # toolbars
        self.fileBar = QtWidgets.QToolBar(self)
        self.fileBar.setObjectName("filebar")
        ToolBars.initFileBar(self.fileBar, self.menuBar)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.fileBar)
        self.toolsBar = QtWidgets.QToolBar(self)
        self.toolsBar.setObjectName("toolsbar")
        ToolBars.initToolsBar(self.toolsBar, self.menuBar)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolsBar)
        self.editBar = QtWidgets.QToolBar(self)
        self.editBar.setObjectName("editbar")
        ToolBars.initEditBar(self.editBar, self.tabWidget.current_widget())
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.editBar)

        self.restoreWinState()
        # must update view menu to get correct states
        self.menuBar.updateViewMenu()

    def restoreWinState(self):
        state = Settings().mainWindowState
        self.restoreState(state[Settings.MWState])
        self.resize(state[Settings.MWSize])
        self.move(state[Settings.MWPosition])
        if state[Settings.MWMaximized]:
            self.showMaximized()

    def setup_status_bar_widgets(self):
        self.lbl_interpreter = QtWidgets.QLabel()
        self.lbl_filename = QtWidgets.QLabel()
        self.lbl_encoding = QtWidgets.QLabel()
        self.lbl_cursor_pos = QtWidgets.QLabel()
        self.statusbar.addPermanentWidget(self.lbl_filename, 200)
        self.statusbar.addPermanentWidget(self.lbl_interpreter, 100)
        self.statusbar.addPermanentWidget(self.lbl_encoding, 20)
        self.statusbar.addPermanentWidget(self.lbl_cursor_pos, 20)

    def closeEvent(self, QCloseEvent):
        """
        Delegates the close event to the tabWidget to be sure we do not quit
        the application while there are some still some unsaved tabs.
        """
        self.tabWidget.closeEvent(QCloseEvent)
        # Save window state
        state = [self.saveState(),
                 self.size(),
                 self.pos(),
                 self.isMaximized()]
        Settings().mainWindowState = state

    def setup_editor(self, editor):
        """
        Setup the python editor, run the server and connect a few signals.

        :param editor: editor to setup.
        """
        editor.cursorPositionChanged.connect(self.on_cursor_pos_changed)
        try:
            m = editor.modes.get(modes.GoToAssignmentsMode)
        except KeyError:
            pass
        else:
            assert isinstance(m, modes.GoToAssignmentsMode)
            m.out_of_doc.connect(self.on_goto_out_of_doc)

    def open_file(self, path, line=None):
        """
        Creates a new GenericCodeEdit, opens the requested file and adds it
        to the tab widget.

        :param path: Path of the file to open

        :return The opened editor if open succeeded.
        """
        editor = None
        if path:
            editor = self.tabWidget.open_document(
                path, interpreter=utils.getInterpreter())
            if editor:
                self.setup_editor(editor)
            self.recent_files_manager.open_file(path)
            self.menuBar.openRecMenu.update_actions()
        if line is not None:
            TextHelper(self.tabWidget.current_widget()).goto_line(line)
        return editor

    @QtCore.Slot()
    def onInterpConfig(self):
        if InterpreterConfigDialog.run(self):
            for editor in self.tabWidget.widgets(include_clones=True):
                editor.backend.stop()
                editor.backend.start(editor.backend.server_script,
                                     interpreter=utils.getInterpreter(),
                                     args=editor.backend.args)

    @QtCore.Slot()
    def on_new(self):
        """
        Add a new empty code editor to the tab widget
        """
        self.setup_editor(self.tabWidget.create_new_document(
            extension='.py', interpreter=utils.getInterpreter()))
        self.menuBar.runAct.setDisabled(True)
        self.menuBar.runConfigAct.setDisabled(True)

    @QtCore.Slot()
    def on_open(self):
        """
        Shows an open file dialog and open the file if the dialog was
        accepted.

        """
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open')
        if filename:
            self.open_file(filename)
        self.menuBar.runAct.setEnabled(True)
        self.menuBar.runConfigAct.setEnabled(True)

    @QtCore.Slot()
    def on_save(self):
        self.tabWidget.save_current()
        self._enable_run()
        self._update_status_bar(self.tabWidget.current_widget())

    @QtCore.Slot()
    def on_save_as(self):
        """
        Save the current editor document as.
        """
        path = self.tabWidget.current_widget().file.path
        path = os.path.dirname(path) if path else ''
        filename, filter = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save', path)
        if filename:
            self.tabWidget.save_current(filename)
            self.recent_files_manager.open_file(filename)
            self.menuBar.openRecMenu.update_actions()
            self.menuBar.runAct.setEnabled(True)
            self.menuBar.runConfigAct.setEnabled(True)
            self._update_status_bar(self.tabWidget.current_widget())

    @QtCore.Slot()
    def on_save_all(self):
        self.tabWidget.save_all()
        self._update_status_bar(self.tabWidget.current_widget())

    @QtCore.Slot(str)
    def onFileDropped(self, path):
        p = utils.rectifyPath(path)
        self.open_file(p)

    def setup_mnu_edit(self, editor):
        """
        Setup the edit menu for the current editor. We show the current editor
        context menu and a menu to change the python interpreter.
    
        :param editor: new editor
        """
        self.menuBar.editMenu.addActions(editor.actions())

    @QtCore.Slot()
    def on_last_tab_closed(self):
        self.outlineTreeDock.outlineTree.set_editor(None)
        self.menuBar.editMenu.setEnabled(False)
        self.menuBar.saveAct.setEnabled(False)
        self.menuBar.saveAsAct.setEnabled(False)
        self.menuBar.saveAllAct.setEnabled(False)
        self.menuBar.runAct.setEnabled(False)
        self.menuBar.runConfigAct.setEnabled(False)

    @QtCore.Slot()
    def on_current_tab_changed(self):
        """
        Update action states when the current tab changed.
        """
        self.menuBar.editMenu.clear()
        # self.menuModes.clear()
        # self.menuPanels.clear()
        editor = self.tabWidget.current_widget()
        self.menuBar.editMenu.setEnabled(editor is not None)
        # self.menuModes.setEnabled(editor is not None)
        # self.menuPanels.setEnabled(editor is not None)
        self.menuBar.saveAct.setEnabled(editor is not None)
        self.menuBar.saveAsAct.setEnabled(editor is not None)
        self.menuBar.saveAllAct.setEnabled(editor is not None)
        self.menuBar.runAct.setEnabled(editor is not None)
        self.menuBar.runConfigAct.setEnabled(editor is not None)
        if editor is not None:
            self.setup_mnu_edit(editor)
            ToolBars.initEditBar(self.editBar, editor)
            # self.setup_mnu_modes(editor)
            # self.setup_mnu_panels(editor)
        self.outlineTreeDock.outlineTree.set_editor(editor)
        self._update_status_bar(editor)

    def _update_status_bar(self, editor):
        if editor:
            l, c = TextHelper(editor).cursor_position()
            self.lbl_cursor_pos.setText(
                '%d:%d' % (l + 1, c + 1))
            self.lbl_encoding.setText(editor.file.encoding)
            self.lbl_filename.setText(editor.file.path)
            self.lbl_interpreter.setText(sys.executable)
        else:
            self.lbl_encoding.clear()
            self.lbl_filename.clear()
            self.lbl_cursor_pos.clear()

    def _enable_run(self):
        self.menuBar.runAct.setEnabled(
            self.tabWidget.current_widget().file.path != '')
        self.menuBar.runConfigAct.setEnabled(
            self.tabWidget.current_widget().file.path != '')

    def on_run(self):
        """
        Run the current current script
        """
        filename = self.tabWidget.current_widget().file.path
        wd = os.path.dirname(filename)
        args = Settings().get_run_config_for_file(filename)
        self.outputDock.iconsole.start_process(
            utils.getInterpreter(),
            args=[filename] + args, cwd=wd)
        self.outputDock.show()
        self.menuBar.runAct.setEnabled(False)
        self.menuBar.runConfigAct.setEnabled(False)

    def on_goto_out_of_doc(self, assignment):
        """
        Open the a new tab when goto goes out of the current document.

        :param assignment: Destination
        """
        editor = self.open_file(assignment.module_path)
        if editor:
            TextHelper(editor).goto_line(assignment.line, assignment.column)

    def on_process_finished(self):
        self.menuBar.runAct.setEnabled(True)
        self.menuBar.runConfigAct.setEnabled(True)

    def on_configure_run(self):
        path = self.tabWidget.current_widget().file.path
        args = Settings().get_run_config_for_file(path)
        text, status = QtWidgets.QInputDialog.getText(
            self, 'Run configuration', 'Script arguments:',
            QtWidgets.QLineEdit.Normal, ' '.join(args))
        if status:
            args = text.split(' ')
            Settings().set_run_config_for_file(path, args)

    @QtCore.Slot()
    def on_cursor_pos_changed(self):
        editor = self.tabWidget.current_widget()
        if editor:
            l, c = TextHelper(editor).cursor_position()
            self.lbl_cursor_pos.setText(
                '%d:%d' % (l + 1, c + 1))

    @QtCore.Slot(WritableObject)
    def pylintFinished(self, out):
        self.pylintDock.outputTE.clear()
        for line in out.read():
            self.pylintDock.outputTE.appendPlainText(line)
        self.pylintDock.show()
