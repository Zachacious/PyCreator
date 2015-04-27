#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Utility to convert .ui files into python modules
"""

from PyQt5 import uic

uic.compileUiDir('./PyCreator',True)
