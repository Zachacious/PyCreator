#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Icons -- no rc file
"""

from pyqode.qt.QtGui import QIcon, QPixmap
from utils import rectifyPath
import os


# static class
class Icons(object):

    # get the abs path to icons from current project dir
    _basePath = "PyCreator/UI/icons/"
    _basePath = os.path.abspath(_basePath)
    _bp = rectifyPath(_basePath)

    new = QIcon()
    openFile = QIcon()
    save = QIcon()
    saveAs = QIcon()
    saveAll = QIcon()
    cut = QIcon()
    copy = QIcon()
    paste = QIcon()
    undo = QIcon()
    redo = QIcon()
    indent = QIcon()
    unindent = QIcon()
    search = QIcon()
    replace = QIcon()
    doc = QIcon()
    run = QIcon()
    runConfig = QIcon()
    comment = QIcon()
    gotoAssign = QIcon()
    dupLine = QIcon()
    folder = QIcon()

    isLoaded = False

    @classmethod
    def load(cls):
        if cls.isLoaded:
            return

        cls.new.addPixmap(QPixmap(cls._bp + os.sep + "new.png"), QIcon.Normal,
                          QIcon.Off)

        cls.openFile.addPixmap(QPixmap(cls._bp + os.sep + "open.png"),
                               QIcon.Normal, QIcon.Off)

        cls.save.addPixmap(QPixmap(cls._bp + os.sep + "save.png"),
                           QIcon.Normal, QIcon.Off)

        cls.saveAs.addPixmap(QPixmap(cls._bp + os.sep + "saveas.png"),
                             QIcon.Normal, QIcon.Off)

        cls.saveAll.addPixmap(QPixmap(cls._bp + os.sep + "saveall.png"),
                              QIcon.Normal, QIcon.Off)

        cls.cut.addPixmap(QPixmap(cls._bp + os.sep + "cut.png"),
                          QIcon.Normal, QIcon.Off)

        cls.copy.addPixmap(QPixmap(cls._bp + os.sep + "copy.png"),
                           QIcon.Normal, QIcon.Off)

        cls.paste.addPixmap(QPixmap(cls._bp + os.sep + "paste.png"),
                            QIcon.Normal, QIcon.Off)

        cls.undo.addPixmap(QPixmap(cls._bp + os.sep + "undo.png"),
                           QIcon.Normal, QIcon.Off)

        cls.redo.addPixmap(QPixmap(cls._bp + os.sep + "redo.png"),
                           QIcon.Normal, QIcon.Off)

        cls.indent.addPixmap(QPixmap(cls._bp + os.sep + "indent.png"),
                             QIcon.Normal, QIcon.Off)

        cls.unindent.addPixmap(QPixmap(cls._bp + os.sep + "unindent.png"),
                               QIcon.Normal, QIcon.Off)

        cls.search.addPixmap(QPixmap(cls._bp + os.sep + "search.png"),
                             QIcon.Normal, QIcon.Off)

        cls.replace.addPixmap(QPixmap(cls._bp + os.sep + "replace.png"),
                              QIcon.Normal, QIcon.Off)

        cls.doc.addPixmap(QPixmap(cls._bp + os.sep + "doc.png"),
                          QIcon.Normal, QIcon.Off)

        cls.run.addPixmap(QPixmap(cls._bp + os.sep + "run.png"),
                          QIcon.Normal, QIcon.Off)

        cls.runConfig.addPixmap(QPixmap(cls._bp + os.sep + "runConfig.png"),
                                QIcon.Normal, QIcon.Off)

        cls.comment.addPixmap(QPixmap(cls._bp + os.sep + "comment.png"),
                              QIcon.Normal, QIcon.Off)

        cls.gotoAssign.addPixmap(QPixmap(cls._bp + os.sep + "gotoassign.png"),
                                 QIcon.Normal, QIcon.Off)

        cls.dupLine.addPixmap(QPixmap(cls._bp + os.sep + "dupline.png"),
                              QIcon.Normal, QIcon.Off)

        cls.folder.addPixmap(QPixmap(cls._bp + os.sep + "folder.png"),
                             QIcon.Normal, QIcon.Off)
