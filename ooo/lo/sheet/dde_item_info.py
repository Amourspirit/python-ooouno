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
import typing


class DDEItemInfo(object):
    """
    Struct Class

    describes an item of a DDE connection.
    
    A DDE connection consists of the DDE service name, the DDE topic and a list of DDE items which may contain cached result sets.
    
    **since**
    
        OOo 3.1

    See Also:
        `API DDEItemInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DDEItemInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DDEItemInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DDEItemInfo'
    """Literal Constant ``com.sun.star.sheet.DDEItemInfo``"""

    Results: typing.TypeAlias = typing.Tuple[typing.Tuple[object, ...], ...]
    """
    The results of the item cached from the last update of the DDE link if available.
    
    This sequence may be empty.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DDEItemInfo`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DDEItemInfo``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Item (str, optional): Item value
        """
        self._item = None

        key_order = ('Item',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DDEItemInfo):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DDEItemInfo.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Item(self) -> str:
        """
        The name of the DDE item.
        """
        return self._item
    
    @Item.setter
    def Item(self, value: str) -> None:
        self._item = value


__all__ = ['DDEItemInfo']
