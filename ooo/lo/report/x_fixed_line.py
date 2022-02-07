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
# Namespace: com.sun.star.report
import typing
from abc import abstractproperty
from .x_report_control_model import XReportControlModel as XReportControlModel_2d800f4a
if typing.TYPE_CHECKING:
    from ..drawing.line_dash import LineDash as LineDash_a54e0afc
    from ..drawing.line_style import LineStyle as LineStyle_b1600b8d
    from ..util.color import Color as Color_68e908c5

class XFixedLine(XReportControlModel_2d800f4a):
    """

    See Also:
        `API XFixedLine <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XFixedLine.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XFixedLine'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XFixedLine'

    @abstractproperty
    def LineColor(self) -> 'Color_68e908c5':
        """
        This property contains the line color.
        """
    @abstractproperty
    def LineDash(self) -> 'LineDash_a54e0afc':
        """
        This property contains the dash of the line.
        """
    @abstractproperty
    def LineStyle(self) -> 'LineStyle_b1600b8d':
        """
        This property contains the type of the line.
        """
    @abstractproperty
    def LineTransparence(self) -> int:
        """
        This property contains the extent of transparency.
        """
    @abstractproperty
    def LineWidth(self) -> int:
        """
        This property contains the width of the line in 1/100th mm.
        """
    @abstractproperty
    def Orientation(self) -> int:
        """
        specifies the orientation of the control.
        """

__all__ = ['XFixedLine']

