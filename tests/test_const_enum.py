# coding: utf-8
import pytest
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.realpath('.'))
    pytest.main([__file__])


def test_message_box_results():
    from ooo.dyn.awt.message_box_results import MessageBoxResults, MessageBoxResultsEnum
    assert MessageBoxResults.CANCEL == MessageBoxResultsEnum.CANCEL.value
    assert MessageBoxResults.CANCEL == MessageBoxResultsEnum.CANCEL
