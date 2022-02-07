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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2


class LeftRightMargin(object):
    """
    Struct Class

    specifies a left and right margin.
    
    **since**
    
        OOo 2.0

    See Also:
        `API LeftRightMargin <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1LeftRightMargin.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.LeftRightMargin'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.LeftRightMargin'
    """Literal Constant ``com.sun.star.frame.status.LeftRightMargin``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``LeftRightMargin`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``LeftRightMargin``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Left (int, optional): Left value
            Right (int, optional): Right value
        """
        self._left = None
        self._right = None

        key_order = ('Left', 'Right')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], LeftRightMargin):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("LeftRightMargin.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Left(self) -> int:
        """
        specifies a left side margin in 1/100th mm.
        """
        return self._left
    
    @Left.setter
    def Left(self, value: int) -> None:
        self._left = value

    @property
    def Right(self) -> int:
        """
        specifies a right side margin in 1/100th mm.
        """
        return self._right
    
    @Right.setter
    def Right(self, value: int) -> None:
        self._right = value


__all__ = ['LeftRightMargin']
