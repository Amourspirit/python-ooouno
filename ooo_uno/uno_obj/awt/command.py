# coding: utf-8
from ...base.const import ConstIntBase


class Command(ConstIntBase):
    """
    these values specify the different command types available.

    See Also:
        `API Command <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1Command.html>`_
    """
    CONTEXTMENU = 1
    """specifies a requests for a context menu."""
    STARTDRAG = 2
    """specifies the beginning of a drag operation."""
    WHEEL = 3
    """specifies a mouse wheel operation."""
    STARTAUTOSCROLL = 4
    """specifies the beginning of an auto scroll operation."""
    AUTOSCROLL = 5
    """specifies an auto scroll operation."""
    VOICE = 6
    """specifies a request for a voice operation."""
    STARTEXTTEXTINPUT = 7
    """specifies the beginning of an extended text input operation."""
    EXTTEXTINPUT = 8
    """specifies an extended text input operation."""
    ENDEXTTEXTINPUT = 9
    """specifies the end of an extended text input operation."""
    INPUTCONTEXTCHANGE = 10
    """specifies that the input context has been changed."""
    CURSORPOS = 11
    """specifies the cursor position."""
    PASTESELECTION = 12
    """specifies a paste selection command."""
    MODKEYCHANGE = 13
    """specifies that the state of a key modifier has changed."""
    HANGUL_HANJA_CONVERSION = 14
    """specifies a Hangul hanja conversion command."""
    USER = 4096
    """specifies a user-defined command."""
