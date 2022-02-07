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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2


class DataPilotFieldAutoShowInfo(object):
    """
    Struct Class

    contains the auto show information of a DataPilotField.
    
    If enabled, only a number of items with the highest or lowest result values are shown. The other items are hidden automatically.

    See Also:
        `API DataPilotFieldAutoShowInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldAutoShowInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldAutoShowInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DataPilotFieldAutoShowInfo'
    """Literal Constant ``com.sun.star.sheet.DataPilotFieldAutoShowInfo``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DataPilotFieldAutoShowInfo`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DataPilotFieldAutoShowInfo``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            IsEnabled (bool, optional): IsEnabled value
            ShowItemsMode (int, optional): ShowItemsMode value
            ItemCount (int, optional): ItemCount value
            DataField (str, optional): DataField value
        """
        self._is_enabled = None
        self._show_items_mode = None
        self._item_count = None
        self._data_field = None

        key_order = ('IsEnabled', 'ShowItemsMode', 'ItemCount', 'DataField')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DataPilotFieldAutoShowInfo):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DataPilotFieldAutoShowInfo.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def IsEnabled(self) -> bool:
        """
        specifies whether the AutoShow feature is enabled or not.
        """
        return self._is_enabled
    
    @IsEnabled.setter
    def IsEnabled(self, value: bool) -> None:
        self._is_enabled = value

    @property
    def ShowItemsMode(self) -> int:
        """
        specifies the mode which items have to be shown.
        """
        return self._show_items_mode
    
    @ShowItemsMode.setter
    def ShowItemsMode(self, value: int) -> None:
        self._show_items_mode = value

    @property
    def ItemCount(self) -> int:
        """
        specifies the number of the items to show.
        """
        return self._item_count
    
    @ItemCount.setter
    def ItemCount(self, value: int) -> None:
        self._item_count = value

    @property
    def DataField(self) -> str:
        """
        specifies the field where the values to show and select are taken from.
        """
        return self._data_field
    
    @DataField.setter
    def DataField(self, value: str) -> None:
        self._data_field = value


__all__ = ['DataPilotFieldAutoShowInfo']
