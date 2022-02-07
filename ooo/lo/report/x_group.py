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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_child import XChild as XChild_a6390b07
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from .x_functions_supplier import XFunctionsSupplier as XFunctionsSupplier_1ee10f09
if typing.TYPE_CHECKING:
    from .x_groups import XGroups as XGroups_90d00a7c
    from .x_section import XSection as XSection_9b630ad1

class XGroup(XPropertySet_bc180bfa, XChild_a6390b07, XComponent_98dc0ab5, XFunctionsSupplier_1ee10f09):
    """
    identifies a XGroup.
    
    A group is always a child of the groups collection in the report.

    See Also:
        `API XGroup <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XGroup.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XGroup'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XGroup'

    @abstractproperty
    def Expression(self) -> str:
        """
        Defines either a column name or an expression.
        """
    @abstractproperty
    def Footer(self) -> 'XSection_9b630ad1':
        """
        returns the group footer.
        """
    @abstractproperty
    def FooterOn(self) -> bool:
        """
        Defines if a group has a footer.
        """
    @abstractproperty
    def GroupInterval(self) -> int:
        """
        Defines an interval value that rows are grouped by.
        """
    @abstractproperty
    def GroupOn(self) -> int:
        """
        Specifies how to group data.
        """
    @abstractproperty
    def Groups(self) -> 'XGroups_90d00a7c':
        """
        Specifies the parent of the group.
        """
    @abstractproperty
    def Header(self) -> 'XSection_9b630ad1':
        """
        returns the group header.
        """
    @abstractproperty
    def HeaderOn(self) -> bool:
        """
        Defines if a group has a header.
        """
    @abstractproperty
    def KeepTogether(self) -> int:
        """
        Specifies if a group header, detail, and footer section is printed on the same page.
        """
    @abstractproperty
    def ResetPageNumber(self) -> bool:
        """
        Specifies that the group header should always be printed on a new page and the reset of the page number to zero.
        """
    @abstractproperty
    def SortAscending(self) -> bool:
        """
        Defines if the group is sorted ascending or descending.
        
        The default is TRUE.
        """
    @abstractproperty
    def StartNewColumn(self) -> bool:
        """
        Specifies that the group header should always be printed on a new column.
        """

__all__ = ['XGroup']

