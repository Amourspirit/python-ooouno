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
# Namespace: com.sun.star.text
# Libre Office Version: 7.2


class HoriOrientationFormat(object):
    """
    Struct Class

    describes the horizontal orientation of an object.
    
    If HorizontalOrientation == HORI_NONE, then the value \"XPos\" describes the distance from the left border of the context. Otherwise \"XPos\" is ignored.
    
    The following flags are used to adapt the position of the object to odd and even pages. If \"PositionToggle\" is set, then the horizontal position is mirrored.

    See Also:
        `API HoriOrientationFormat <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1HoriOrientationFormat.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.HoriOrientationFormat'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.text.HoriOrientationFormat'
    """Literal Constant ``com.sun.star.text.HoriOrientationFormat``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``HoriOrientationFormat`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``HoriOrientationFormat``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            XPos (int, optional): XPos value
            HorizontalOrientation (int, optional): HorizontalOrientation value
            HorizontalRelation (int, optional): HorizontalRelation value
            PositionToggle (bool, optional): PositionToggle value
        """
        self._x_pos = None
        self._horizontal_orientation = None
        self._horizontal_relation = None
        self._position_toggle = None

        key_order = ('XPos', 'HorizontalOrientation', 'HorizontalRelation', 'PositionToggle')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], HoriOrientationFormat):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("HoriOrientationFormat.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def XPos(self) -> int:
        """
        contains the distance from the left border.
        
        Only valid if the property HorizontalOrientation contains the value HORI_NONE.
        """
        return self._x_pos
    
    @XPos.setter
    def XPos(self, value: int) -> None:
        self._x_pos = value

    @property
    def HorizontalOrientation(self) -> int:
        """
        determines the horizontal alignment of an object.
        
        The values refer to com.sun.star.HoriOrientation.
        """
        return self._horizontal_orientation
    
    @HorizontalOrientation.setter
    def HorizontalOrientation(self, value: int) -> None:
        self._horizontal_orientation = value

    @property
    def HorizontalRelation(self) -> int:
        """
        determines the reference position of the horizontal alignment.
        """
        return self._horizontal_relation
    
    @HorizontalRelation.setter
    def HorizontalRelation(self, value: int) -> None:
        self._horizontal_relation = value

    @property
    def PositionToggle(self) -> bool:
        """
        determines if the orientation toggles between left and right pages.
        """
        return self._position_toggle
    
    @PositionToggle.setter
    def PositionToggle(self, value: bool) -> None:
        self._position_toggle = value


__all__ = ['HoriOrientationFormat']
