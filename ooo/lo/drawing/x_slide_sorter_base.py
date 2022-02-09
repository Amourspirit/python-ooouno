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
# Namespace: com.sun.star.drawing
import typing
from abc import abstractproperty
from .x_draw_view import XDrawView as XDrawView_b0b80b75
from .framework.x_view import XView as XView_ffed0de3
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
    from ..util.color import Color as Color_68e908c5

class XSlideSorterBase(XDrawView_b0b80b75, XView_ffed0de3):
    """
    This interface exists only because services do not directly support multiple inheritance and attributes.
    
    It provides the interfaces and attributes that every object that implements the SlideSorter service.

    See Also:
        `API XSlideSorterBase <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XSlideSorterBase.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XSlideSorterBase'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XSlideSorterBase'

    @abstractproperty
    def BackgroundColor(self) -> 'Color_68e908c5':
        """
        """
    @abstractproperty
    def DocumentSlides(self) -> 'XIndexAccess_f0910d6d':
        """
        The set of slides that are displayed by the implementing object.
        
        The default value is the set of all slides of the document for which a slide sorter is created.
        """
    @abstractproperty
    def HighlightColor(self) -> 'Color_68e908c5':
        """
        """
    @abstractproperty
    def IsCenterSelection(self) -> bool:
        """
        When this flag has the value TRUE then every time the current slide is changed the visual area is shifted so that the new current slide is display in the center of the slide sorter window.
        
        It is not always possible to move the current slide into the exact center of the window, for example when slides are located near the start or end of a document.
        
        The default value is FALSE.
        """
    @abstractproperty
    def IsHighlightCurrentSlide(self) -> bool:
        """
        Set this flag to TRUE in order to have the current slide highlighted.
        
        The default value is FALSE.
        """
    @abstractproperty
    def IsOrientationVertical(self) -> bool:
        """
        The orientation of a slide sorter can be either vertical (TRUE) or horizontal (FALSE).
        """
    @abstractproperty
    def IsShowFocus(self) -> bool:
        """
        Set this flag to TRUE to visualize to where the focus is by showing a dotted rectangle around the focused slide.
        
        The default value is TRUE.
        """
    @abstractproperty
    def IsShowSelection(self) -> bool:
        """
        Set this flag to TRUE in order to visualize the selection of slides (typically a bold frame around the selected slides).
        
        The default value is TRUE.
        """
    @abstractproperty
    def IsSmoothScrolling(self) -> bool:
        """
        This flag is a hint to make scrolling look smooth.
        """
    @abstractproperty
    def IsSuspendPreviewUpdatesDuringFullScreenPresentation(self) -> bool:
        """
        This flag controls whether updates of previews are created during full screen presentations (FALSE) or not (TRUE).
        
        The suspension of preview creations is an optimization for not slowing down a running presentation.
        
        The default value is TRUE.
        """
    @abstractproperty
    def IsUIReadOnly(self) -> bool:
        """
        This flag controls whether the model can be modified by using keyboard or mouse.
        
        The default value is TRUE.
        """
    @abstractproperty
    def SelectionColor(self) -> 'Color_68e908c5':
        """
        """
    @abstractproperty
    def TextColor(self) -> 'Color_68e908c5':
        """
        """


__all__ = ['XSlideSorterBase']

