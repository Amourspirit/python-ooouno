# coding: utf-8
from email import message
import pytest
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))
    pytest.main([__file__])

from ooo_uno.uno_obj.awt.message_box_results import MessageBoxResults, MessageBoxResultsEnum

def test_message_box_results():
    assert MessageBoxResults.CANCEL == MessageBoxResultsEnum.CANCEL.value
    assert MessageBoxResults.CANCEL == MessageBoxResultsEnum.CANCEL
