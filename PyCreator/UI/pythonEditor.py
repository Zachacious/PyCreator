#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
PythonEditor

- ~To Do~
Type Description

"""

import sys
from pyqode.core.api import ColorScheme
# from pyqode.qt import QtWidgets, QtCore
from pyqode.core import api, modes, panels
# from pyqode.core.widgets import OutlineTreeWidget
from pyqode.python import modes as pymodes, \
    panels as pypanels, widgets as pwidgets  # , managers
from pyqode.python.folding import PythonFoldDetector
from pyqode.python.backend.workers import defined_names
from pyqode.python.backend import server


class PythonEditor(pwidgets.PyCodeEditBase):
    """Python pQode code editor widget.

    Extends PyCodeEditBase with a set of hardcoded modes and panels specifics
    to a python code editor widget.
    """
    DARK_STYLE = 0
    LIGHT_STYLE = 1

    mimetypes = ['text/x-python']

    def __init__(self, parent=None, server_script=server.__file__,
                 interpreter=sys.executable, args=None,
                 create_default_actions=True, color_scheme='qt',
                 reuse_backend=False):
        super(PythonEditor, self).__init__(
                      parent=parent,
                      create_default_actions=create_default_actions)
        self.backend.start(server_script)
        # self.backend.start(server_script, interpreter, args,
        #                    reuse=reuse_backend)
        self.setLineWrapMode(self.NoWrap)
        self.setWindowTitle("Python")

        # install those modes first as they are required by other modes/panels
        self.modes.append(modes.OutlineMode(defined_names))

        # panels
        self.panels.append(panels.FoldingPanel())
        self.panels.append(panels.LineNumberPanel())
        self.panels.append(panels.CheckerPanel())
        self.panels.append(panels.GlobalCheckerPanel(),
                           panels.GlobalCheckerPanel.Position.RIGHT)
        self.panels.append(panels.SearchAndReplacePanel(),
                           panels.SearchAndReplacePanel.Position.BOTTOM)
        self.panels.append(panels.EncodingPanel(), api.Panel.Position.TOP)
        self.add_separator()
        self.panels.append(pypanels.QuickDocPanel(), api.Panel.Position.BOTTOM)

        # modes
        # generic
        self.modes.append(modes.CaretLineHighlighterMode())
        self.modes.append(modes.FileWatcherMode())
        self.modes.append(modes.RightMarginMode())
        self.modes.append(modes.ZoomMode())
        self.modes.append(modes.SymbolMatcherMode())
        self.modes.append(modes.CodeCompletionMode())
        self.modes.append(modes.OccurrencesHighlighterMode())
        self.modes.append(modes.SmartBackSpaceMode())
        self.modes.append(modes.ExtendedSelectionMode())
        self.modes.append(modes.CaseConverterMode())
        # python specifics
        self.modes.append(pymodes.PyAutoIndentMode())
        self.modes.append(pymodes.PyAutoCompleteMode())
        self.modes.append(pymodes.FrostedCheckerMode())
        self.modes.append(pymodes.PEP8CheckerMode())
        self.modes.append(pymodes.CalltipsMode())
        self.modes.append(pymodes.PyIndenterMode())
        self.modes.append(pymodes.GoToAssignmentsMode())
        self.modes.append(pymodes.CommentsMode())
        self.modes.append(pymodes.PythonSH(
            self.document(), color_scheme=ColorScheme(color_scheme)))
        self.syntax_highlighter.fold_detector = PythonFoldDetector()

    def clone(self):
        clone = self.__class__(
            parent=self.parent(), server_script=self.backend.server_script,
            interpreter=self.backend.interpreter, args=self.backend.args,
            color_scheme=self.syntax_highlighter.color_scheme.name)
        return clone

    def __repr__(self):
        return 'PythonEditor(path=%r)' % self.file.path
