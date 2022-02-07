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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.table
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from .border_line import BorderLine as BorderLine_a3f80af6
    from .border_line2 import BorderLine2 as BorderLine2_af200b28
    from .cell_hori_justify import CellHoriJustify as CellHoriJustify_e0470d10
    from .cell_orientation import CellOrientation as CellOrientation_e0e40d1c
    from .shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from .table_border import TableBorder as TableBorder_aedf0b56
    from .table_border2 import TableBorder2 as TableBorder2_ba670b88
    from ..util.cell_protection import CellProtection as CellProtection_c9290c6d
    from ..util.color import Color as Color_68e908c5

class CellProperties(XPropertySet_bc180bfa):
    """
    Service Class

    contains the properties of a table cell.
    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API CellProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1table_1_1CellProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.CellProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def AsianVerticalMode(self) -> bool:
        """
        selects Asian character orientation in vertical orientation.
        
        If the CellProperties.Orientation property is CellOrientation.STACKED, in Asian mode only Asian characters are printed in horizontal orientation instead of all characters. For other values of CellProperties.Orientation, this value is not used.
        """
    @abstractproperty
    def BottomBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains a description of the bottom border line of each cell.
        """
    @abstractproperty
    def BottomBorder2(self) -> 'BorderLine2_af200b28':
        """
        contains a description of the bottom border line of each cell.
        
        Preferred over BorderLine BottomBorder.
        
        **since**
        
            LibreOffice 3.6
        """
    @abstractproperty
    def CellBackColor(self) -> 'Color_68e908c5':
        """
        contains the cell background color.
        """
    @abstractproperty
    def CellProtection(self) -> 'CellProtection_c9290c6d':
        """
        contains a description of the cell protection.
        
        Cell protection is active only if the sheet is protected.
        """
    @abstractproperty
    def CellStyle(self) -> str:
        """
        contains the name of the style of the cell.
        """
    @abstractproperty
    def DiagonalBLTR(self) -> 'BorderLine_a3f80af6':
        """
        contains a description of the bottom left to top right diagonal line of each cell.
        """
    @abstractproperty
    def DiagonalBLTR2(self) -> 'BorderLine2_af200b28':
        """
        contains a description of the bottom left to top right diagonal line of each cell.
        
        Preferred over BorderLine DiagonalBLTR.
        
        **since**
        
            LibreOffice 3.6
        """
    @abstractproperty
    def DiagonalTLBR(self) -> 'BorderLine_a3f80af6':
        """
        contains a description of the top left to bottom right diagonal line of each cell.
        """
    @abstractproperty
    def DiagonalTLBR2(self) -> 'BorderLine2_af200b28':
        """
        contains a description of the top left to bottom right diagonal line of each cell.
        
        Preferred over BorderLine DiagonalTLBR.
        
        **since**
        
            LibreOffice 3.6
        """
    @abstractproperty
    def HoriJustify(self) -> 'CellHoriJustify_e0470d10':
        """
        contains the horizontal alignment of the cell contents.
        """
    @abstractproperty
    def IsCellBackgroundTransparent(self) -> bool:
        """
        is TRUE, if the cell background is transparent.
        
        In this case the CellProperties.CellBackColor value is not used.
        """
    @abstractproperty
    def IsTextWrapped(self) -> bool:
        """
        is TRUE, if text in the cells will be wrapped automatically at the right border.
        """
    @abstractproperty
    def LeftBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains a description of the left border line of each cell.
        """
    @abstractproperty
    def LeftBorder2(self) -> 'BorderLine2_af200b28':
        """
        contains a description of the left border line of each cell.
        
        Preferred over BorderLine LeftBorder.
        
        **since**
        
            LibreOffice 3.6
        """
    @abstractproperty
    def NumberFormat(self) -> int:
        """
        contains the index of the number format that is used in the cells.
        
        The proper value can be determined by using the com.sun.star.util.NumberFormatter interface of the document.
        """
    @abstractproperty
    def Orientation(self) -> 'CellOrientation_e0e40d1c':
        """
        contains the orientation of the cell contents.
        
        If the CellProperties.RotateAngle property is non-zero, this value is not used.
        """
    @abstractproperty
    def ParaIndent(self) -> int:
        """
        defines the indentation of the cell contents (in 1/100 mm).
        """
    @abstractproperty
    def RightBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains a description of the right border line of each cell.
        """
    @abstractproperty
    def RightBorder2(self) -> 'BorderLine2_af200b28':
        """
        contains a description of the right border line of each cell.
        
        Preferred over BorderLine RightBorder.
        
        **since**
        
            LibreOffice 3.6
        """
    @abstractproperty
    def RotateAngle(self) -> int:
        """
        defines how much the content of cells is rotated (in 1/100 degrees).
        """
    @abstractproperty
    def RotateReference(self) -> int:
        """
        defines at which edge rotated cells are aligned.
        
        changed from com.sun.star.table.CellVertJustify to long in LibO 3.5
        """
    @abstractproperty
    def ShadowFormat(self) -> 'ShadowFormat_bb840bdf':
        """
        contains a description of the shadow.
        """
    @abstractproperty
    def ShrinkToFit(self) -> bool:
        """
        is TRUE, if the cell content will be shrunk to fit in the cell.
        """
    @abstractproperty
    def TableBorder(self) -> 'TableBorder_aedf0b56':
        """
        contains a description of the cell or cell range border.
        
        If used with a cell range, the top, left, right, and bottom lines are at the edges of the entire range, not at the edges of the individual cell.
        """
    @abstractproperty
    def TableBorder2(self) -> 'TableBorder2_ba670b88':
        """
        contains a description of the cell or cell range border.
        
        Preferred over TableBorder TableBorder.
        
        If used with a cell range, the top, left, right, and bottom lines are at the edges of the entire range, not at the edges of the individual cell.
        
        **since**
        
            LibreOffice 3.6
        """
    @abstractproperty
    def TopBorder(self) -> 'BorderLine_a3f80af6':
        """
        contains a description of the top border line of each cell.
        """
    @abstractproperty
    def TopBorder2(self) -> 'BorderLine2_af200b28':
        """
        contains a description of the top border line of each cell.
        
        Preferred over BorderLine TopBorder.
        
        **since**
        
            LibreOffice 3.6
        """
    @abstractproperty
    def UserDefinedAttributes(self) -> 'XNameContainer_cb90e47':
        """
        stores additional attributes.
        
        This property is used i.e. by the XML filters to load and restore unknown attributes.
        """
    @abstractproperty
    def VertJustify(self) -> int:
        """
        contains the vertical alignment of the cell contents.
        
        changed from com.sun.star.table.CellVertJustify to long in LibO 3.5
        """
    @abstractproperty
    def CellInteropGrabBag(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Grab bag of cell properties, used as a string-any map for interim interop purposes.
        
        This property is intentionally not handled by the ODF filter. Any member that should be handled there should be first moved out from this grab bag to a separate property.
        
        **since**
        
            LibreOffice 4.3
        """

__all__ = ['CellProperties']

