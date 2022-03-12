# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.presentation
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..drawing.x_shape import XShape as XShape_8fd00a3d


class ParagraphTarget(object):
    """
    Struct Class

    an event has a source that causes an event to be fired and a trigger that defines under which condition an event should be raised and an offset if the event should be raised a defined amount of time after the event is triggered.

    See Also:
        `API ParagraphTarget <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1presentation_1_1ParagraphTarget.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.ParagraphTarget'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.presentation.ParagraphTarget'
    """Literal Constant ``com.sun.star.presentation.ParagraphTarget``"""

    def __init__(self, Shape: typing.Optional[XShape_8fd00a3d] = None, Paragraph: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Shape (XShape, optional): Shape value.
            Paragraph (int, optional): Paragraph value.
        """
        super().__init__()
        kargs = {
            "Shape": Shape,
            "Paragraph": Paragraph,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._shape = kwargs["Shape"]
        self._paragraph = kwargs["Paragraph"]


    @property
    def Shape(self) -> XShape_8fd00a3d:
        return self._shape
    
    @Shape.setter
    def Shape(self, value: XShape_8fd00a3d) -> None:
        self._shape = value

    @property
    def Paragraph(self) -> int:
        return self._paragraph
    
    @Paragraph.setter
    def Paragraph(self, value: int) -> None:
        self._paragraph = value


__all__ = ['ParagraphTarget']
