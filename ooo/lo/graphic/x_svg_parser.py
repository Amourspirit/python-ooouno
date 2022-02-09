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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.graphic
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_primitive2_d import XPrimitive2D as XPrimitive2D_d5730c6d

class XSvgParser(XInterface_8f010a43):
    """
    XSvgParser interface.
    
    This interface allows to parse a SVG stream in form of a sequence of bytes to be parsed into a sequence of XPrimitive2Ds
    
    **since**
    
        LibreOffice 6.3

    See Also:
        `API XSvgParser <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XSvgParser.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.graphic'
    __ooo_full_ns__: str = 'com.sun.star.graphic.XSvgParser'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.graphic.XSvgParser'

    @abstractmethod
    def getDecomposition(self, xSvgStream: object, aAbsolutePath: str) -> 'typing.Tuple[XPrimitive2D_d5730c6d, ...]':
        """
        Retrieve decomposed list of simpler primitives.
        """
    @abstractmethod
    def getDrawCommands(self, xSvgStream: object, aAbsolutePath: str) -> object:
        """
        Get the \"draw command\" graph that is created from the SVG content.
        
        **since**
        
            LibreOffice 6.3
        """


__all__ = ['XSvgParser']

