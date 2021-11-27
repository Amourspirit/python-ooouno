# coding: utf-8
from ...base.const import ConstIntBase


class FontUnderline(ConstIntBase):
    """
    These values are used to specify the kind of underlining.

    See Also:
        `API FontUnderline <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1FontUnderline.html>`_
    """
    NONE = 0
    """specifies no underlining."""

    SINGLE = 1
    """specifies underlining with a single line."""

    DOUBLE = 2
    """specifies underlining with a double line."""

    DOTTED = 3
    """specifies underlining with a dotted line."""

    DONTKNOW = 4
    """The kind of underlining is not known."""

    DASH = 5
    """specifies underlining with a dashed line."""

    LONG_DASH = 6
    """specifies underlining with long dashes."""

    DASH_DOT = 7
    """specifies underlining with a dash and dot sequence."""

    DASH_DOT_DOT = 8
    """specifies underlining with a dash, dot, dot sequence."""

    SMALL_WAVE = 9
    """specifies underlining with a small wave."""

    WAVE = 10
    """specifies underlining with a wave."""

    DOUBLE_WAVE = 11
    """specifies underlining with a double wave."""

    BOLD = 12
    """specifies underlining with a bold line."""

    BOLDDOTTED = 13
    """specifies underlining with bold dots."""

    BOLD_DASH = 14
    """specifies underlining with bold dashes."""

    BOLD_LONG_DASH = 15
    """specifies underlining with long bold dashes."""

    BOLD_DASH_DOT = 16
    """specifies underlining with a dash and dot sequence in bold."""

    BOLD_DASH_DOT_DOT = 17
    """specifies underlining with a dash, dot, dot sequence in bold."""

    BOLD_WAVE = 18
    """specifies underlining with a bold wave."""
