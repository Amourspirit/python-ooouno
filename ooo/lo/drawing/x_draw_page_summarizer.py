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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_draw_page import XDrawPage as XDrawPage_b07a0b57
    from .x_draw_pages import XDrawPages as XDrawPages_bc440bca

class XDrawPageSummarizer(XInterface_8f010a43):
    """
    is implemented by documents that can create summaries of their DrawPages.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XDrawPageSummarizer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XDrawPageSummarizer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XDrawPageSummarizer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XDrawPageSummarizer'

    @abstractmethod
    def summarize(self, xPages: 'XDrawPages_bc440bca') -> 'XDrawPage_b07a0b57':
        """
        creates a new DrawPage with a summary of all DrawPages in the given collection.
        """

__all__ = ['XDrawPageSummarizer']
