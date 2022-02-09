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
# Namespace: com.sun.star.mozilla
# Libre Office Version: 7.2


class MenuSingleChange(object):
    """
    Struct Class

    Explains a change for a menu item.

    See Also:
        `API MenuSingleChange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1mozilla_1_1MenuSingleChange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.mozilla'
    __ooo_full_ns__: str = 'com.sun.star.mozilla.MenuSingleChange'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.mozilla.MenuSingleChange'
    """Literal Constant ``com.sun.star.mozilla.MenuSingleChange``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``MenuSingleChange`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``MenuSingleChange``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ID (int, optional): ID value
            ChangeID (int, optional): ChangeID value
            Change (object, optional): Change value
        """
        self._id = None
        self._change_id = None
        self._change = None

        key_order = ('ID', 'ChangeID', 'Change')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], MenuSingleChange):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("MenuSingleChange.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def ID(self) -> int:
        """
        unique ID of this menu item
        """
        return self._id
    
    @ID.setter
    def ID(self, value: int) -> None:
        self._id = value

    @property
    def ChangeID(self) -> int:
        """
        ID identifying the type of change in the any type change.
        """
        return self._change_id
    
    @ChangeID.setter
    def ChangeID(self, value: int) -> None:
        self._change_id = value

    @property
    def Change(self) -> object:
        """
        value of change
        """
        return self._change
    
    @Change.setter
    def Change(self, value: object) -> None:
        self._change = value


__all__ = ['MenuSingleChange']
