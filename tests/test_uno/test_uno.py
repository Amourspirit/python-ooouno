# coding: utf-8
# NOTE:
#   On slower machines this test may have to be run several times before connection can be made
#   to Libre Office. If you see com.sun.star.connection.NoConnectException error this is an indicator.

import pytest
from typing import TYPE_CHECKING
from pathlib import Path
if TYPE_CHECKING:
    from ooo.lo.frame.x_model import XModel

if __name__ == "__main__":
    pytest.main([__file__])


def test_sequence(get_document: 'XModel'):
    import uno
    from ooo.lo.text.x_text import XText
    from ooo.lo.text.generic_text_document import GenericTextDocument
    from ooo.lo.io.sequence_input_stream import SequenceInputStream
    from ooo.lo.text.text_table import TextTable
    from ooo.dyn.beans.property_value import PropertyValue
    from ooo.helper import uno_helper

    doc: GenericTextDocument = get_document
    table: TextTable = doc.createInstance("com.sun.star.text.TextTable")
    text: XText = doc.getText()
    table.setName('NewTable')
    # table.initialize(nRows=2, nColumns=2) # named args are not supported
    table.initialize(2, 2)
    text.insertTextContent(text.getEnd(), table, True)
    # text.insertTextContent(xRange=text.getEnd(), xContent=table, bAbsorb=True) # named args are not supported
    a = (("foo", "bar"), (1, 2))
    table.setDataArray(a)
    data = table.getDataArray()
    assert data == a
    
    arg1 = PropertyValue()
    arg1.Name = "InputStream"
    arg2 = PropertyValue()
    arg2.Name = "FilterName"
    arg2.Value = "writer_web_HTML"
    bs = b"<html><body><p>Text from <b>HTML</b>.</p></body></html>"
    # sequence: SequenceInputStream = uno_helper.create_uno_service("com.sun.star.io.SequenceInputStream")
    sequence: SequenceInputStream = uno_helper.create_uno_service(SequenceInputStream)
    sequence.initialize((uno.ByteSequence(bs),))
    # sequence.createStreamFromSequence((uno.ByteSequence(bs),))
    arg1.Value = sequence
    text = doc.getText()
    text.setString("")

    text.getEnd().insertDocumentFromURL("", (arg1, arg2))
    sequence.closeInput()

def test_simple_file_access(get_document, fixture_dir):
    from ooo.helper import uno_helper
    from ooo.csslo.ucb import SimpleFileAccess
    doc = Path(fixture_dir) / 'docs' / 'hello_world.odt'
    file_access: SimpleFileAccess = uno_helper.create_uno_service('com.sun.star.ucb.SimpleFileAccess')
    # s = file_access.getContentType('https://raw.githubusercontent.com/Amourspirit/python-ooouno/main/README.rst')
    s = file_access.getContentType('file://' + str(doc))
    assert len(s) > 0
    # assert s == 'application/http-content'
    assert s == 'application/vnd.sun.staroffice.fsys-file'
