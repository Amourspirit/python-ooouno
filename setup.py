#!/usr/bin/env python
import pathlib
import os
from setuptools import setup
from ooo import __version__
PKG_NAME = 'ooouno'
VERSION = __version__
PKG_MAIN = 'ooo_uno'
SUB_PKG = ['base', 'args', 'ctl', 'env', 'interface',
               'uno_obj', 'uno_obj.awt', 'uno_obj.beans', 'uno_obj.container',
               'uno_obj.frame', 'uno_obj.lang', 'uno_obj.script', 'uno_obj.script.provider',
               'uno_obj.style', 'uno_obj.text', 'uno_obj.uno',
               'com.sun.star.', 'com.sun.star.awt', 'com.sun.star.beans', 'com.sun.star.container',
               'com.sun.star.frame', 'com.sun.star.lang', 'com.sun.star.script', 'com.sun.star.script.provider',
               'com.sun.star.style', 'com.sun.star.text', 'com.sun.star.uno']
# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE / "README.rst") as fh:
    README = fh.read()


def getListOfFiles(dir_name):
    '''
    For the given path, get the List of all files in the directory tree 
    '''
    # create a list of file and sub directories
    # names in the given directory
    list_of_files = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + getListOfFiles(full_path)
        else:
            all_files.append(full_path)

    return all_files


def get_src_modules(root_path: pathlib.Path):
    dir_name = root_path / 'ooo_uno'
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dir_name)
    _slice = len(str(dir_name)) + 1
    py_lst = [f[_slice:-3]
              for f in list(filter(lambda p: p.endswith('.py'), listOfFiles))]
    return py_lst

def get_packages():
    result = []
    for pkg in SUB_PKG:
        result.append(PKG_MAIN + '.' + pkg)
    return result
        
MODULES = get_src_modules(HERE)
PACKAGES =  get_packages()

# This call to setup() does all the work
setup(
    name=PKG_NAME,
    version=VERSION,
    python_requires='>=3.6.0',
    description="Interfaces and classes for Libre Office (uno)",
    long_description_content_type="text/x-rst",
    long_description=README,
    url="https://github.com/Amourspirit/python-ooouno",
    author=":Barry-Thomas-Paul: Moss",
    author_email='bigbytetech@gmail.com',
    license="MIT",
    packages=PACKAGES,
    py_modules=MODULES,
    keywords=['uno', 'libreoffice', 'openoffice', 'pyuno'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    include_package_data=True,
)
