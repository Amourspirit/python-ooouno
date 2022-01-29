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
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_report_control_format import XReportControlFormat as XReportControlFormat_3d4e0fc2

class XFormatCondition(XPropertySet_bc180bfa, XReportControlFormat_3d4e0fc2):
    """
    specifies a format condition for a control.

    See Also:
        `API XFormatCondition <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XFormatCondition.html>`_
    """

    @abstractproperty
    def Enabled(self) -> bool:
        """
        specifies if the condition is enabled or not.
        """
    @abstractproperty
    def Formula(self) -> str:
        """
        defines the formula of the format condition.
        
        If the formula evaluates to TRUE then the format will be applied.
        """

__all__ = ['XFormatCondition']

