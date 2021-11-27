# coding: utf-8
from abc import ABC, abstractproperty


class IVerticalAlignmentEnum(ABC):
    """
    specify the horizontal alignment of an object within a container object.

    See Also:
        ` <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a9c2ed22cfbd21f13df24ea193b310aee>`_
    """
    @abstractproperty
    def TOP(self) -> int:
        """set the vertical alignment to the center between the top and bottom margins from the container object."""
    @abstractproperty
    def MIDDLE(self) -> int:
        """set the vertical alignment to the top margin from the container object."""
    @abstractproperty
    def BOTTOM(self) -> int:
        """set the vertical alignment to the bottom margin from the container object."""
