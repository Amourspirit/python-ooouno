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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from ..table.shadow_format import ShadowFormat as ShadowFormat_bb840bdf
    from ..table.table_border import TableBorder as TableBorder_aedf0b56
    from ..table.table_border2 import TableBorder2 as TableBorder2_ba670b88
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.awt.FontSlant import FontSlantProto  # type: ignore
    from com.sun.star.table.CellHoriJustify import CellHoriJustifyProto  # type: ignore
    from com.sun.star.table.CellOrientation import CellOrientationProto  # type: ignore

class TableAutoFormatField(XPropertySet_bc180bfa):
    """
    Service Class

    represents a field in an AutoFormat.
    
    A field contains all cell properties for a specific position in an AutoFormat.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TableAutoFormatField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1TableAutoFormatField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.TableAutoFormatField'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def CellBackColor(self) -> Color_68e908c5:
        """
        contains the cell background color.
        """
        ...

    @property
    @abstractmethod
    def CharColor(self) -> Color_68e908c5:
        """
        contains the value of the text color.
        """
        ...

    @property
    @abstractmethod
    def CharContoured(self) -> bool:
        """
        is TRUE if the characters are contoured.
        """
        ...

    @property
    @abstractmethod
    def CharCrossedOut(self) -> bool:
        """
        is TRUE if the characters are crossed out.
        """
        ...

    @property
    @abstractmethod
    def CharFontCharSet(self) -> str:
        """
        contains the value of the character set of the western font.
        """
        ...

    @property
    @abstractmethod
    def CharFontCharSetAsian(self) -> str:
        """
        contains the value of the character set of the Asian font.
        """
        ...

    @property
    @abstractmethod
    def CharFontCharSetComplex(self) -> str:
        """
        contains the value of the character set of the complex font.
        """
        ...

    @property
    @abstractmethod
    def CharFontFamily(self) -> str:
        """
        contains the value of the western font family.
        """
        ...

    @property
    @abstractmethod
    def CharFontFamilyAsian(self) -> str:
        """
        contains the value of the Asian font family.
        """
        ...

    @property
    @abstractmethod
    def CharFontFamilyComplex(self) -> str:
        """
        contains the value of the complex font family.
        """
        ...

    @property
    @abstractmethod
    def CharFontName(self) -> str:
        """
        specifies the name of the western font.
        """
        ...

    @property
    @abstractmethod
    def CharFontNameAsian(self) -> str:
        """
        specifies the name of the Asian font.
        """
        ...

    @property
    @abstractmethod
    def CharFontNameComplex(self) -> str:
        """
        specifies the name of the complex font.
        """
        ...

    @property
    @abstractmethod
    def CharFontPitch(self) -> str:
        """
        contains the value of the pitch of the western font.
        """
        ...

    @property
    @abstractmethod
    def CharFontPitchAsian(self) -> str:
        """
        contains the value of the pitch of the Asian font.
        """
        ...

    @property
    @abstractmethod
    def CharFontPitchComplex(self) -> str:
        """
        contains the value of the pitch of the complex font.
        """
        ...

    @property
    @abstractmethod
    def CharFontStyleName(self) -> str:
        """
        specifies the name of the western font style.
        """
        ...

    @property
    @abstractmethod
    def CharFontStyleNameAsian(self) -> str:
        """
        specifies the name of the Asian font style.
        """
        ...

    @property
    @abstractmethod
    def CharFontStyleNameComplex(self) -> str:
        """
        specifies the name of the complex font style.
        """
        ...

    @property
    @abstractmethod
    def CharHeight(self) -> float:
        """
        contains the height of characters of the western font in point.
        """
        ...

    @property
    @abstractmethod
    def CharHeightAsian(self) -> float:
        """
        contains the height of characters of the Asian font in point.
        """
        ...

    @property
    @abstractmethod
    def CharHeightComplex(self) -> float:
        """
        contains the height of characters of the complex font in point.
        """
        ...

    @property
    @abstractmethod
    def CharPosture(self) -> FontSlantProto:
        """
        contains the value of the posture of characters of the western font.
        """
        ...

    @property
    @abstractmethod
    def CharPostureAsian(self) -> FontSlantProto:
        """
        contains the value of the posture of characters of the Asian font.
        """
        ...

    @property
    @abstractmethod
    def CharPostureComplex(self) -> FontSlantProto:
        """
        contains the value of the posture of characters of the complex font.
        """
        ...

    @property
    @abstractmethod
    def CharShadowed(self) -> bool:
        """
        is TRUE if the characters are shadowed.
        """
        ...

    @property
    @abstractmethod
    def CharUnderline(self) -> int:
        """
        contains the value for the character underline.
        """
        ...

    @property
    @abstractmethod
    def CharWeight(self) -> float:
        """
        contains the value for the weight of characters of the western font.
        """
        ...

    @property
    @abstractmethod
    def CharWeightAsian(self) -> float:
        """
        contains the value for the weight of characters of the Asian font.
        """
        ...

    @property
    @abstractmethod
    def CharWeightComplex(self) -> float:
        """
        contains the value for the weight of characters of the complex font.
        """
        ...

    @property
    @abstractmethod
    def HoriJustify(self) -> CellHoriJustifyProto:
        """
        specifies the horizontal alignment of the cell contents.
        """
        ...

    @property
    @abstractmethod
    def IsCellBackgroundTransparent(self) -> bool:
        """
        is TRUE if the cell background is transparent.
        
        In this case the TableAutoFormatField.CellBackColor value is not used.
        """
        ...

    @property
    @abstractmethod
    def IsTextWrapped(self) -> bool:
        """
        is TRUE if text breaks automatically at cell borders.
        """
        ...

    @property
    @abstractmethod
    def Orientation(self) -> CellOrientationProto:
        """
        contains the orientation of the cell contents (i.e.
        
        top-to-bottom or stacked).
        """
        ...

    @property
    @abstractmethod
    def ParaBottomMargin(self) -> int:
        """
        contains the margin between cell contents and bottom border (in 1/100 mm).
        """
        ...

    @property
    @abstractmethod
    def ParaLeftMargin(self) -> int:
        """
        contains the margin between cell contents and left border (in 1/100 mm).
        """
        ...

    @property
    @abstractmethod
    def ParaRightMargin(self) -> int:
        """
        contains the margin between cell contents and right border (in 1/100 mm).
        """
        ...

    @property
    @abstractmethod
    def ParaTopMargin(self) -> int:
        """
        contains the margin between cell contents and top border (in 1/100 mm).
        """
        ...

    @property
    @abstractmethod
    def RotateAngle(self) -> int:
        """
        contains the rotation angle of the cell contents.
        """
        ...

    @property
    @abstractmethod
    def RotateReference(self) -> int:
        """
        contains the reference edge of the cell rotation.
        
        changed from com.sun.star.table.CellVertJustify to long in LibO 3.5
        """
        ...

    @property
    @abstractmethod
    def ShadowFormat(self) -> ShadowFormat_bb840bdf:
        """
        contains a description of the shadow.
        """
        ...

    @property
    @abstractmethod
    def TableBorder(self) -> TableBorder_aedf0b56:
        """
        property containing a description of the cell border.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @property
    @abstractmethod
    def TableBorder2(self) -> TableBorder2_ba670b88:
        """
        property containing a description of the cell border.
        
        Preferred over com.sun.star.table.TableBorder TableBorder.
        
        **since**
        
            LibreOffice 3.6
        """
        ...

    @property
    @abstractmethod
    def VertJustify(self) -> int:
        """
        specifies the vertical alignment of the cell contents.
        
        changed from com.sun.star.table.CellVertJustify to long in LibO 3.5
        """
        ...


__all__ = ['TableAutoFormatField']