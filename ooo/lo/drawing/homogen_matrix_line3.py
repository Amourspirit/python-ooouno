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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2


class HomogenMatrixLine3(object):
    """
    Struct Class

    specifies a single line for a HomogenMatrix3.

    See Also:
        `API HomogenMatrixLine3 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1HomogenMatrixLine3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.HomogenMatrixLine3'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.HomogenMatrixLine3'
    """Literal Constant ``com.sun.star.drawing.HomogenMatrixLine3``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``HomogenMatrixLine3`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``HomogenMatrixLine3``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Column1 (float, optional): Column1 value
            Column2 (float, optional): Column2 value
            Column3 (float, optional): Column3 value
        """
        self._column1 = None
        self._column2 = None
        self._column3 = None

        key_order = ('Column1', 'Column2', 'Column3')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], HomogenMatrixLine3):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("HomogenMatrixLine3.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def Column1(self) -> float:
        """
        """
        return self._column1
    
    @Column1.setter
    def Column1(self, value: float) -> None:
        self._column1 = value

    @property
    def Column2(self) -> float:
        """
        """
        return self._column2
    
    @Column2.setter
    def Column2(self, value: float) -> None:
        self._column2 = value

    @property
    def Column3(self) -> float:
        """
        """
        return self._column3
    
    @Column3.setter
    def Column3(self, value: float) -> None:
        self._column3 = value


__all__ = ['HomogenMatrixLine3']
