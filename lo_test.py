"""
This module is not to be run on its own.
This module is to be compiled and run inside of Libre Office.

Certain test do no seem to lend themself to normal testing methods.
For instance trying to test the loading of a singleton crashes the thread
when testing with pytest. Propally on a pytest issue.

By writing test and compiling special case test into a single script and running
in Libre Office the test can be run.

command: python -m app test -w
By running command the file is created in tmp dir.
The recommended way to test this in Libre Office is to create a sys link in
Libre office Scripts python dir.
For snap it may be similar to the following:
~/snap/libreoffice/current/.config/libreoffice/4/user/Scripts/python/test

Once a link is created the test will show as a macros.
Run test as a macro in Libre Office.

Using the Libre Office Python console the result of test can be see.

Note:
    Libre Office will run stickytape extraction method on first macro call.
    Libre Office will extract all module into a tmp dir, load the modules into memory
    and then Libre Office will del the temp dir. This means when you get a module path
    it will no longer exist on disk.
"""
import unittest
from io import StringIO
from lotest import tst_singleton

def run_test():
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(unittest.makeSuite(tst_singleton.TestSingleton))
    print('Singleton tests run ', result.testsRun)
    print('Singleton Was Successfull', result.wasSuccessful())
    for fail in result.failures:
        print("Test Failed:", fail)
    for err in result.errors:
        print(err)
