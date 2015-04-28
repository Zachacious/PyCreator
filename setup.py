#!/usr/bin/env python
"""
Setup script for PyCreator
"""
import PyCreator
from setuptools import setup, find_packages

cmdclass = {}

# get long description
with open('README.rst', 'r') as readme:
    long_desc = readme.read()

# install requirements
requirements = [
    'pyqode.python', 'pyzmq', 'virtualenv', 'pip>=1.5.6',
    'setuptools>=7.0'
]

# install desktop entry and pixmap on linux
data_files = []

# run setup
setup(
    name='PyCreator',
    version='0.1.0a1',
    packages=[p for p in find_packages() if 'test' not in p],
    keywords=['Python; PyCreator; IDE'],
    data_files=data_files,
    url='https://github.com/Zachacious/PyCreator',
    license='MIT',
    author='Zach Moore',
    author_email='Back4Moore@Gmail.com',
    description='A Simple Python ide developed for learning purposes',
    long_description=long_desc,
    install_requires=requirements,
    entry_points={'gui_scripts': ['PyCreator = PyCreator.main:main']},
    cmdclass=cmdclass
)