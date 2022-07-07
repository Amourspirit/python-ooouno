# coding: utf-8
import pytest

if __name__ == "__main__":
    pytest.main([__file__])


def test_message_box_results():
    from ooo.dyn.awt.message_box_results import MessageBoxResults, MessageBoxResultsEnum

    assert MessageBoxResults.CANCEL == MessageBoxResultsEnum.CANCEL.value
    assert MessageBoxResults.CANCEL == MessageBoxResultsEnum.CANCEL


def test_numbering_type():
    # in NumberingType not all attribs are availibale in older versions
    # the following attribs are only avaliable in ver 7x
    # ARABIC_ZERO3, ARABIC_ZERO4, ARABIC_ZERO5, SZEKELY_ROVAS
    # these attribs will be missing from dynamic enum and const in version older than 7.0
    from ooo.cssdyn.style import NumberingType as NumberingType
    from ooo.cssdyn.style import NumberingTypeEnum as NumberingTypeEnum

    assert NumberingType.__ooo_ns__ == "com.sun.star.style"
    assert NumberingType.__ooo_full_ns__ == "com.sun.star.style.NumberingType"
    assert NumberingType.__ooo_type_name__ == "const"
    assert isinstance(NumberingType.BITMAP, int)
    assert NumberingTypeEnum.BITMAP == NumberingType.BITMAP
    assert NumberingTypeEnum.BITMAP.value == NumberingType.BITMAP


def test_focus_change_reason():
    # FocusChangeReason is Flags Enum
    from ooo.cssdyn.awt import FocusChangeReason
    from ooo.cssdyn.awt import FocusChangeReasonEnum

    assert FocusChangeReason.__ooo_ns__ == "com.sun.star.awt"
    assert FocusChangeReason.__ooo_full_ns__ == "com.sun.star.awt.FocusChangeReason"
    assert FocusChangeReason.__ooo_type_name__ == "const"
    e = FocusChangeReasonEnum.AROUND | FocusChangeReasonEnum.CURSOR
    assert FocusChangeReasonEnum.AROUND & e == FocusChangeReasonEnum.AROUND
    assert FocusChangeReasonEnum.CURSOR & e == FocusChangeReasonEnum.CURSOR


def test_cell_flags() -> None:
    from ooo.dyn.sheet.cell_flags import CellFlagsEnum

    flags = CellFlagsEnum.VALUE | CellFlagsEnum.STRING
    new_flags = CellFlagsEnum(flags)
    assert new_flags == flags
