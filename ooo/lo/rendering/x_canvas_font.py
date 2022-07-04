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
# Namespace: com.sun.star.rendering
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .font_metrics import FontMetrics as FontMetrics_e4540d34
    from .font_request import FontRequest as FontRequest_e4890d46
    from .string_context import StringContext as StringContext_d50e22
    from .x_text_layout import XTextLayout as XTextLayout_e44a0d41

class XCanvasFont(XInterface_8f010a43):
    """
    This interface provides access to a specific, XCanvas-dependent font incarnation.
    
    This font is not universally usable, but belongs to the XCanvas it was queried from.

    See Also:
        `API XCanvasFont <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XCanvasFont.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XCanvasFont'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XCanvasFont'

    @abstractmethod
    def createTextLayout(self, aText: 'StringContext_d50e22', nDirection: int, nRandomSeed: int) -> 'XTextLayout_e44a0d41':
        """
        Create a text layout interface.
        
        Create a text layout interface for the given string, using this font to generate the glyphs from.
        """
        ...
    @abstractmethod
    def getAvailableSizes(self) -> 'typing.Tuple[float, ...]':
        """
        Query the list of available font sizes.
        
        This method queries the list of available font sizes (in device units) for this font. For scalable fonts that are not restricted to discrete sizes, this list is empty, meaning that every size is possible. Fonts that do restrict the device size to certain discrete values, setting an overall transformation that scales the FontRequest.CellSize to something not contained in the list returned by this method can lead to visible disturbances.
        """
        ...
    @abstractmethod
    def getExtraFontProperties(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Query the list of additional font properties.
        """
        ...
    @abstractmethod
    def getFontMetrics(self) -> 'FontMetrics_e4540d34':
        """
        Query metric information about the font, that is generic to all its glyphs.
        
        Note that the metric values in the returned result are in the font coordinate system, i.e. relative to the corresponding size of this font. That is, when this font was created with a cell size of 20 units, the metrics returned are calculated relative to this size.
        """
        ...
    @abstractmethod
    def getFontRequest(self) -> 'FontRequest_e4890d46':
        """
        Query the FontRequest that was used to generate this object.
        """
        ...

__all__ = ['XCanvasFont']

