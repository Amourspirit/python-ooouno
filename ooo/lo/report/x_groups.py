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
from abc import abstractmethod, abstractproperty
from ..container.x_child import XChild as XChild_a6390b07
from ..container.x_container import XContainer as XContainer_d6fb0cc6
from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_group import XGroup as XGroup_86540a09
    from .x_report_definition import XReportDefinition as XReportDefinition_ec30e81

class XGroups(XChild_a6390b07, XContainer_d6fb0cc6, XIndexContainer_1c040ebe, XComponent_98dc0ab5):
    """
    This interface specifies the groups collections of the report definition.

    See Also:
        `API XGroups <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XGroups.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XGroups'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XGroups'

    @abstractmethod
    def createGroup(self) -> 'XGroup_86540a09':
        """
        factory method for XGroup.
        """
    @abstractproperty
    def ReportDefinition(self) -> 'XReportDefinition_ec30e81':
        """
        """


__all__ = ['XGroups']

