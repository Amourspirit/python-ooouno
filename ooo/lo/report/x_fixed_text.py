# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.report
from abc import abstractproperty
from .x_report_control_model import XReportControlModel as XReportControlModel_2d800f4a

class XFixedText(XReportControlModel_2d800f4a):
    """

    See Also:
        `API XFixedText <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XFixedText.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XFixedText'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XFixedText'

    @abstractproperty
    def Label(self) -> str:
        """
        specifies the label of the control.
        """
        ...


__all__ = ['XFixedText']

