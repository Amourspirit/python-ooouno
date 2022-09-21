#!/usr/bin/env python
import pathlib
from setuptools import setup, find_packages
from ooo import __version__
PKG_NAME = 'ooouno'
VERSION = __version__
PKG_MAIN = 'ooo'

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE / "README.rst") as fh:
    README = fh.read()

PACKAGES = find_packages(exclude=['build', 'dist', 'env', 'app_cmd', 'docs', 'htmlcov', 'lotest', 'resources', 'tmp', 'tests', '*.tests', '*.tests.*'])

# This call to setup() does all the work
setup(
    name=PKG_NAME,
    version=VERSION,
    python_requires='>=3.7.0',
    description="Interfaces and classes for LibreOffice (uno)",
    long_description_content_type="text/x-rst",
    long_description=README,
    url="https://github.com/Amourspirit/python-ooouno",
    author=":Barry-Thomas-Paul: Moss",
    author_email='bigbytetech@gmail.com',
    license="Apache Software License",
    packages=PACKAGES,
    keywords=['ooouno', 'uno', 'libreoffice', 'openoffice', 'pyuno'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Office/Business",
        "Typing :: Typed",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[
        'types-unopy>=0.3.3'
    ],
    include_package_data=True,
)
