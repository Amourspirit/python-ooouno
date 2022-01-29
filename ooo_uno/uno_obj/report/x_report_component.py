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
from ..drawing.x_shape import XShape as XShape_8fd00a3d
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..util.x_cloneable import XCloneable as XCloneable_99d00aa3
if typing.TYPE_CHECKING:
    from .x_section import XSection as XSection_9b630ad1

class XReportComponent(XPropertySet_bc180bfa, XChild_a6390b07, XShape_8fd00a3d, XComponent_98dc0ab5, XCloneable_99d00aa3):
    """
    describes a component which may be part of a report.

    See Also:
        `API XReportComponent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XReportComponent.html>`_
    """

    @abstractproperty
    def AutoGrow(self) -> bool:
        """
        Specifies that the control containing data shall automatically grow to the optimal height to show the data without wasting space.
        """
    @abstractproperty
    def ControlBorder(self) -> int:
        """
        specifies the border style of the control.
        """
    @abstractproperty
    def ControlBorderColor(self) -> int:
        """
        specifies the color of the border, if present
        
        Not every border style (see Border) may support coloring. For instance, usually a border with 3D effect will ignore the BorderColor setting.
        """
    @abstractproperty
    def Height(self) -> int:
        """
        specifies the height of the control.
        """
    @abstractproperty
    def Name(self) -> str:
        """
        the name of the component.
        """
    @abstractproperty
    def PositionX(self) -> int:
        """
        specifies the horizontal position of the control.
        """
    @abstractproperty
    def PositionY(self) -> int:
        """
        specifies the vertical position of the control.
        """
    @abstractproperty
    def PrintRepeatedValues(self) -> bool:
        """
        Specifies that recurring values are printed.
        
        If set to TRUE then the value will be printed every time. If set to FALSE then the value will only be printed once. The default value is TRUE.
        """
    @abstractproperty
    def Section(self) -> 'XSection_9b630ad1':
        """
        Specifies the section where the control belongs to.
        
        This is a shortcut to get control hierarchy up. This value is NULL when the control was not inserted in any section.
        """
    @abstractproperty
    def Width(self) -> int:
        """
        specifies the width of the control.
        """
    @abstractproperty
    def DetailFields(self) -> 'typing.List[str]':
        """
        is used for subreports and contains the names of the columns of the subreport which are related to the master fields of the parent report.
        
        Entries in this sequence can either denote column names in the sub report, or parameter names.
        For instance, you could base the report on the SQL statement SELECT * FROM invoices WHERE cust_ref = :cid, and add cid to the DetailFields property. In this case, the parameter will be filled from the corresponding master field.
        Alternatively, you could simply base your report on the table invoices, and add the column name cust_ref to the DetailFields. In this case, and implicit filter clause WHERE cust_ref = :<new_param_name> will be created, and the artificial parameter will be filled from the corresponding master field.
        If a string in this property denotes both a column name and a parameter name, it is undefined which way it is interpreted, but implementations of the service are required to either decide for the parameter or the column, and proceed as usual.
        
        The columns specified herein typically represent a part of the primary key fields or their aliases of the detail report.
        
        If the report is no sub report (e.g. its parent is not a report itself), this property is not evaluated.
        """
    @abstractproperty
    def MasterFields(self) -> 'typing.List[str]':
        """
        is used for subreports and contains the names of columns of the parent report.
        
        These columns are typically the foreign key fields of the parent report. The values of these columns are used to identify the data for the subreport. Each time the parent report changes its current row, the subreport requeries it's data based on the values of the master fields.
        
        If the report is no sub report (e.g. its parent is not a report itself), this property is not evaluated.
        """

__all__ = ['XReportComponent']

