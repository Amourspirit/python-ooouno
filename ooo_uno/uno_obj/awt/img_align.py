# coding: utf-8
from ...base.const import ConstIntBase


class ImageAlign(ConstIntBase):
    """
    specifies the alignment of an image.

    See Also:
        `API ImageAlign <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1ImageAlign.html>`_
    """
    LEFT = 0
    """specifies to align left."""

    TOP = 1
    """specifies to align top."""

    RIGHT = 2
    """specifies to align right."""

    BOTTOM = 3
    """specifies to align bottom."""
