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
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.2


class IntegerRectangle2D(object):
    """
    Struct Class

    This structure contains the necessary information for a two-dimensional rectangle.
    
    **since**
    
        OOo 2.0

    See Also:
        `API IntegerRectangle2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1IntegerRectangle2D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.geometry'
    __ooo_full_ns__: str = 'com.sun.star.geometry.IntegerRectangle2D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.geometry.IntegerRectangle2D'
    """Literal Constant ``com.sun.star.geometry.IntegerRectangle2D``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``IntegerRectangle2D`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``IntegerRectangle2D``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            X1 (int, optional): X1 value
            Y1 (int, optional): Y1 value
            X2 (int, optional): X2 value
            Y2 (int, optional): Y2 value
        """
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        key_order = ('X1', 'Y1', 'X2', 'Y2')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], IntegerRectangle2D):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("IntegerRectangle2D.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def X1(self) -> int:
        """
        X coordinate of upper left corner.
        """
        return self._x1
    
    @X1.setter
    def X1(self, value: int) -> None:
        self._x1 = value

    @property
    def Y1(self) -> int:
        """
        Y coordinate of upper left corner.
        """
        return self._y1
    
    @Y1.setter
    def Y1(self, value: int) -> None:
        self._y1 = value

    @property
    def X2(self) -> int:
        """
        X coordinate of lower right corner.
        
        Must be greater than X1 for non-empty rectangles.
        """
        return self._x2
    
    @X2.setter
    def X2(self, value: int) -> None:
        self._x2 = value

    @property
    def Y2(self) -> int:
        """
        Y coordinate of lower right corner.
        
        Must be greater than y1 for non-empty rectangles.
        """
        return self._y2
    
    @Y2.setter
    def Y2(self, value: int) -> None:
        self._y2 = value


__all__ = ['IntegerRectangle2D']
