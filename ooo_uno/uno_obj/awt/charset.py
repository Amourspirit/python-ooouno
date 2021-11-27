# coding: utf-8
from ...base.const import ConstIntBase


class CharSet(ConstIntBase):
    """
    These values are used to specify the characters which are available in a font and their codes.

    See Also:
        `API CharSet <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1CharSet.html>`_
    """
    DONTKNOW = 0
    """specifies an unknown character set"""
    ANSI = 1
    """specifies the ANSI character set."""
    MAC = 2
    """specifies the Apple Macintosh character set."""
    IBMPC_437 = 3
    """specifies the IBM PC character set number 437."""
    IBMPC_850 = 4
    """specifies the IBM PC character set number 850."""
    IBMPC_860 = 5
    """specifies the IBM PC character set number 860."""
    IBMPC_861 = 6
    """specifies the IBM PC character set number 861."""
    IBMPC_863 = 7
    """specifies the IBM PC character set number 863."""
    IBMPC_865 = 8
    """specifies the IBM PC character set number 865."""
    SYSTEM = 9
    """specifies the system character set."""
    SYMBOL = 10
    """specifies a set of symbols."""
