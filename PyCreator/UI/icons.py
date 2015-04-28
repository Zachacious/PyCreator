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
    # _basePath = os.getcwd() + "/UI/icons/"
    # _basePath = os.path.abspath(_basePath)
    # _bp = rectifyPath(_basePath)

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

        bp = ""

        if os.path.isdir(rectifyPath(os.getcwd() + "/PyCreator")):
            bp = rectifyPath(os.getcwd() + "/PyCreator/UI/Icons")
        else:
            bp = rectifyPath(os.getcwd() + "/UI/Icons")

        cls.new.addPixmap(QPixmap(bp + os.sep + "new.png"), QIcon.Normal,
                          QIcon.Off)

        cls.openFile.addPixmap(QPixmap(bp + os.sep + "open.png"),
                               QIcon.Normal, QIcon.Off)

        cls.save.addPixmap(QPixmap(bp + os.sep + "save.png"),
                           QIcon.Normal, QIcon.Off)

        cls.saveAs.addPixmap(QPixmap(bp + os.sep + "saveas.png"),
                             QIcon.Normal, QIcon.Off)

        cls.saveAll.addPixmap(QPixmap(bp + os.sep + "saveall.png"),
                              QIcon.Normal, QIcon.Off)

        cls.cut.addPixmap(QPixmap(bp + os.sep + "cut.png"),
                          QIcon.Normal, QIcon.Off)

        cls.copy.addPixmap(QPixmap(bp + os.sep + "copy.png"),
                           QIcon.Normal, QIcon.Off)

        cls.paste.addPixmap(QPixmap(bp + os.sep + "paste.png"),
                            QIcon.Normal, QIcon.Off)

        cls.undo.addPixmap(QPixmap(bp + os.sep + "undo.png"),
                           QIcon.Normal, QIcon.Off)

        cls.redo.addPixmap(QPixmap(bp + os.sep + "redo.png"),
                           QIcon.Normal, QIcon.Off)

        cls.indent.addPixmap(QPixmap(bp + os.sep + "indent.png"),
                             QIcon.Normal, QIcon.Off)

        cls.unindent.addPixmap(QPixmap(bp + os.sep + "unindent.png"),
                               QIcon.Normal, QIcon.Off)

        cls.search.addPixmap(QPixmap(bp + os.sep + "search.png"),
                             QIcon.Normal, QIcon.Off)

        cls.replace.addPixmap(QPixmap(bp + os.sep + "replace.png"),
                              QIcon.Normal, QIcon.Off)

        cls.doc.addPixmap(QPixmap(bp + os.sep + "doc.png"),
                          QIcon.Normal, QIcon.Off)

        cls.run.addPixmap(QPixmap(bp + os.sep + "run.png"),
                          QIcon.Normal, QIcon.Off)

        cls.runConfig.addPixmap(QPixmap(bp + os.sep + "runConfig.png"),
                                QIcon.Normal, QIcon.Off)

        cls.comment.addPixmap(QPixmap(bp + os.sep + "comment.png"),
                              QIcon.Normal, QIcon.Off)

        cls.gotoAssign.addPixmap(QPixmap(bp + os.sep + "gotoassign.png"),
                                 QIcon.Normal, QIcon.Off)

        cls.dupLine.addPixmap(QPixmap(bp + os.sep + "dupline.png"),
                              QIcon.Normal, QIcon.Off)

        cls.folder.addPixmap(QPixmap(bp + os.sep + "folder.png"),
                             QIcon.Normal, QIcon.Off)
