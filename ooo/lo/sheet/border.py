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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from enum import Enum


class Border(Enum):
    """
    Enum Class


    See Also:
        `API Border <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#aea307cd05a4c363d9cac3828a62f4127>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.Border'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.sheet.Border'

    BOTTOM = 'BOTTOM'
    """
    selects the bottom border.
    """
    LEFT = 'LEFT'
    """
    selects the left border.
    
    the cells to the right of the deleted cells are moved left.
    """
    RIGHT = 'RIGHT'
    """
    selects the right border.
    
    the cells to the right of the inserted cells are moved right.
    """
    TOP = 'TOP'
    """
    selects the top border.
    """

__all__ = ['Border']

