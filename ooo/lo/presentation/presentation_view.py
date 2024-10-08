# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.presentation
from __future__ import annotations
import typing
from abc import abstractmethod
from ..awt.x_window import XWindow as XWindow_713b0924
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..drawing.x_draw_view import XDrawView as XDrawView_b0b80b75
from ..frame.controller import Controller as Controller_a5330b37
if typing.TYPE_CHECKING:
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..drawing.x_draw_page import XDrawPage as XDrawPage_b07a0b57

class PresentationView(Controller_a5330b37, XWindow_713b0924, XPropertySet_bc180bfa, XDrawView_b0b80b75):
    """
    Service Class

    This component integrates a view to a slide show of a presentation document into the desktop.

    See Also:
        `API PresentationView <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1presentation_1_1PresentationView.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.PresentationView'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def CurrentPage(self) -> XDrawPage_b07a0b57:
        """
        This is the drawing page that is currently visible.
        """
        ...

    @property
    @abstractmethod
    def VisibleArea(self) -> Rectangle_84b109e9:
        """
        This is the area that is currently visible.
        """
        ...


__all__ = ['PresentationView']

