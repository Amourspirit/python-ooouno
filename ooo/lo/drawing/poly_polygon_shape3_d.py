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
import typing
if typing.TYPE_CHECKING:
    from .double_sequence_sequence import DoubleSequenceSequence as DoubleSequenceSequence_6b8010c1


class PolyPolygonShape3D(object):
    """
    Struct Class

    specifies the coordinates of a 3-dimensional poly polygon.

    See Also:
        `API PolyPolygonShape3D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1PolyPolygonShape3D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.PolyPolygonShape3D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.PolyPolygonShape3D'
    """Literal Constant ``com.sun.star.drawing.PolyPolygonShape3D``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``PolyPolygonShape3D`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``PolyPolygonShape3D``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            SequenceX (DoubleSequenceSequence, optional): SequenceX value
            SequenceY (DoubleSequenceSequence, optional): SequenceY value
            SequenceZ (DoubleSequenceSequence, optional): SequenceZ value
        """
        self._sequence_x = None
        self._sequence_y = None
        self._sequence_z = None

        key_order = ('SequenceX', 'SequenceY', 'SequenceZ')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], PolyPolygonShape3D):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("PolyPolygonShape3D.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def SequenceX(self) -> 'DoubleSequenceSequence_6b8010c1':
        return self._sequence_x
    
    @SequenceX.setter
    def SequenceX(self, value: 'DoubleSequenceSequence_6b8010c1') -> None:
        self._sequence_x = value

    @property
    def SequenceY(self) -> 'DoubleSequenceSequence_6b8010c1':
        return self._sequence_y
    
    @SequenceY.setter
    def SequenceY(self, value: 'DoubleSequenceSequence_6b8010c1') -> None:
        self._sequence_y = value

    @property
    def SequenceZ(self) -> 'DoubleSequenceSequence_6b8010c1':
        return self._sequence_z
    
    @SequenceZ.setter
    def SequenceZ(self, value: 'DoubleSequenceSequence_6b8010c1') -> None:
        self._sequence_z = value


__all__ = ['PolyPolygonShape3D']
