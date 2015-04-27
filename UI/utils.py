# -*- coding: utf-8 -*-
import os
from settings import Settings


def getInterpreter():
    iconfig = Settings().interpreterConfig
    if iconfig[Settings.IConfigOption] == Settings.IConfigOptAuto:
        dirs = os.environ['PYTHONPATH'].split(os.pathsep)
        pyfile = "python.exe"
        for p in dirs:
            path = os.path.join(p, pyfile)
            if os.path.exists(path):
                if os.path.isfile(path):
                    return path
    else:
        return iconfig[Settings.IConfigPath]


def getParentDir(path):
    directories = path.split(os.sep)
    return os.path.join(path, os.sep.join(directories[0:]))


def rectifyPath(path):
    # Hopefully this is portable
    path = os.path.normpath(path)
    drive, xpath = os.path.splitdrive(path)
    if path == drive+os.sep:
        path = os.path.normcase(path)
    return path
