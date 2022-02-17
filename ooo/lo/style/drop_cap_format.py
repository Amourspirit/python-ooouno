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
# Namespace: com.sun.star.style
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class DropCapFormat(object):
    """
    Struct Class

    This struct describes drop caps at a paragraph object.

    See Also:
        `API DropCapFormat <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1style_1_1DropCapFormat.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.DropCapFormat'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.style.DropCapFormat'
    """Literal Constant ``com.sun.star.style.DropCapFormat``"""

    def __init__(self, Lines: int = 0, Count: int = 0, Distance: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``Lines`` can be another ``DropCapFormat`` instance,
                in which case other named args are ignored.

        Arguments:
            Lines (int, optional): Lines value
            Count (int, optional): Count value
            Distance (int, optional): Distance value
        """
        if isinstance(Lines, DropCapFormat):
            oth: DropCapFormat = Lines
            self._lines = oth.Lines
            self._count = oth.Count
            self._distance = oth.Distance
            return
        else:
            self._lines = Lines
            self._count = Count
            self._distance = Distance



    @property
    def Lines(self) -> int:
        """
        This is the number of lines used for a drop cap.
        """
        return self._lines
    
    @Lines.setter
    def Lines(self, value: int) -> None:
        self._lines = value

    @property
    def Count(self) -> int:
        """
        This is the number of characters in the drop cap.
        """
        return self._count
    
    @Count.setter
    def Count(self, value: int) -> None:
        self._count = value

    @property
    def Distance(self) -> int:
        """
        This is the distance between the drop cap in the following text.
        """
        return self._distance
    
    @Distance.setter
    def Distance(self, value: int) -> None:
        self._distance = value


__all__ = ['DropCapFormat']
