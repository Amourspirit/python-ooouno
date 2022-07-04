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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from abc import abstractproperty, ABC

class LineNumberingProperties(ABC):
    """
    Service Class

    provides access to the settings of the line numbering.
    
    **since**
    
        OOo 2.0

    See Also:
        `API LineNumberingProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1LineNumberingProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.LineNumberingProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CharStyleName(self) -> str:
        """
        The name of the character style that is used for the line number.
        """
        ...

    @abstractproperty
    def CountEmptyLines(self) -> bool:
        """
        If TRUE, empty lines are counted.
        """
        ...

    @abstractproperty
    def CountLinesInFrames(self) -> bool:
        """
        If TRUE, lines in frames are included in counting.
        """
        ...

    @abstractproperty
    def Distance(self) -> int:
        """
        specifies the distance between the line number and the start or end of the text area.
        """
        ...

    @abstractproperty
    def Interval(self) -> int:
        """
        Line numbers are shown on every Intervalth line.
        """
        ...

    @abstractproperty
    def IsOn(self) -> bool:
        """
        If TRUE, line numbering is used.
        """
        ...

    @abstractproperty
    def NumberPosition(self) -> int:
        """
        specifies the position of the line number (constant LineNumberPositions left/right/inside/outside).
        """
        ...

    @abstractproperty
    def NumberingType(self) -> int:
        """
        specifies the type of the numbering.
        """
        ...

    @abstractproperty
    def RestartAtEachPage(self) -> bool:
        """
        specifies if the line numbering should start from the beginning at each page.
        
        If set to FALSE the line numbering will be continuous.
        
        **since**
        
            OOo 2.0
        """
        ...

    @abstractproperty
    def SeparatorInterval(self) -> int:
        """
        The line separator is shown every SeparatorIntervalth line.
        """
        ...

    @abstractproperty
    def SeparatorText(self) -> str:
        """
        specifies the string that is used for the line separator.
        """
        ...



__all__ = ['LineNumberingProperties']

