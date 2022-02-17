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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractproperty
from ..beans.property_set import PropertySet as PropertySet_b0e70ba2
from .x_formula_parser import XFormulaParser as XFormulaParser_d54d0cbc
if typing.TYPE_CHECKING:
    from .external_link_info import ExternalLinkInfo as ExternalLinkInfo_f09b0d7e
    from .formula_op_code_map_entry import FormulaOpCodeMapEntry as FormulaOpCodeMapEntry_37da0f61

class FormulaParser(PropertySet_b0e70ba2, XFormulaParser_d54d0cbc):
    """
    Service Class

    
    **since**
    
        OOo 3.1

    See Also:
        `API FormulaParser <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1FormulaParser.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FormulaParser'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ExternalLinks(self) -> 'typing.Tuple[ExternalLinkInfo_f09b0d7e, ...]':
        """
        contains a list of external links referenced in formulas.
        
        Use of this property depends on the FormulaConvention in use. It is relevant only for AddressConvention.XL_OOX to map indices to external documents. The sequence must be in the order of indices used. Note that indices are 1-based, the sequence must start with an empty element.
        
        **since**
        
            OOo 3.1
        """

    @abstractproperty
    def OpCodeMap(self) -> 'typing.Tuple[FormulaOpCodeMapEntry_37da0f61, ...]':
        """
        contains the complete mapping of names to op-codes.
        
        Names and symbols not defined here lead to a parser/print error.
        """



__all__ = ['FormulaParser']
