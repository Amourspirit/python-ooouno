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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet


class DataPilotFieldLayoutMode(object):
    """
    Const Class

    describes the layout mode of the data field
    
    **since**
    
        LibreOffice 7.6

    See Also:
        `API DataPilotFieldLayoutMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldLayoutMode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldLayoutMode'
    __ooo_type_name__: str = 'const'

    TABULAR_LAYOUT = 0
    """
    Tabular layout mode is the layout, where each item's name is on the same row as the first item from the following field.
    
    Subtotals are always shown below an item's data in this mode.
    """
    OUTLINE_SUBTOTALS_TOP = 1
    """
    In outline layout mode, the items from the following field start in the row below an item's name, like in traditional database reports.
    
    Subtotals are shown at the top (on the same row as the item's name). When the subtotals take up more than one row (manually selected, or because there are several data fields), they are always shown below the item's data, regardless of the setting.
    """
    OUTLINE_SUBTOTALS_BOTTOM = 2
    """
    In outline layout mode, the items from the following field start in the row below an item's name, like in traditional database reports.
    
    Subtotals are shown at the bottom (below the item's data, as in tabular layout mode). When the subtotals take up more than one row (manually selected, or because there are several data fields), they are always shown below the item's data, regardless of the setting.
    """
    COMPACT_LAYOUT = 3
    """
    In compact layout mode, the items from the following field start in the row below an item's name with an indentation but in the same column as this field's items are.
    
    Subtotals are shown at the top (on the same row as the item's name). When the subtotals take up more than one row (manually selected, or because there are several data fields), they are always shown below the item's data, regardless of the setting.
    
    **since**
    
        LibreOffice 7.6
    """

__all__ = ['DataPilotFieldLayoutMode']
