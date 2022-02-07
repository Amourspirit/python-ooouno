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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2


class Size(object):
    """
    Struct Class

    specifies the 2-dimensional size of an area using width and height.

    See Also:
        `API Size <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Size.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.Size'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.Size'
    """Literal Constant ``com.sun.star.awt.Size``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``Size`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``Size``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Width (int, optional): Width value
            Height (int, optional): Height value
        """
        self._width = None
        self._height = None

        key_order = ('Width', 'Height')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], Size):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("Size.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Width(self) -> int:
        """
        specifies the width.
        """
        return self._width
    
    @Width.setter
    def Width(self, value: int) -> None:
        self._width = value

    @property
    def Height(self) -> int:
        """
        specifies the height.
        """
        return self._height
    
    @Height.setter
    def Height(self, value: int) -> None:
        self._height = value


__all__ = ['Size']
