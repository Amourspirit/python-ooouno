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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
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

    def __init__(self, SequenceX: typing.Optional[DoubleSequenceSequence_6b8010c1] = DoubleSequenceSequence_6b8010c1(()), SequenceY: typing.Optional[DoubleSequenceSequence_6b8010c1] = DoubleSequenceSequence_6b8010c1(()), SequenceZ: typing.Optional[DoubleSequenceSequence_6b8010c1] = DoubleSequenceSequence_6b8010c1(())) -> None:
        """
        Constructor

        Arguments:
            SequenceX (DoubleSequenceSequence, optional): SequenceX value.
            SequenceY (DoubleSequenceSequence, optional): SequenceY value.
            SequenceZ (DoubleSequenceSequence, optional): SequenceZ value.
        """
        super().__init__()

        if isinstance(SequenceX, PolyPolygonShape3D):
            oth: PolyPolygonShape3D = SequenceX
            self.SequenceX = oth.SequenceX
            self.SequenceY = oth.SequenceY
            self.SequenceZ = oth.SequenceZ
            return

        kargs = {
            "SequenceX": SequenceX,
            "SequenceY": SequenceY,
            "SequenceZ": SequenceZ,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._sequence_x = kwargs["SequenceX"]
        self._sequence_y = kwargs["SequenceY"]
        self._sequence_z = kwargs["SequenceZ"]


    @property
    def SequenceX(self) -> DoubleSequenceSequence_6b8010c1:
        return self._sequence_x

    @SequenceX.setter
    def SequenceX(self, value: DoubleSequenceSequence_6b8010c1) -> None:
        self._sequence_x = value

    @property
    def SequenceY(self) -> DoubleSequenceSequence_6b8010c1:
        return self._sequence_y

    @SequenceY.setter
    def SequenceY(self, value: DoubleSequenceSequence_6b8010c1) -> None:
        self._sequence_y = value

    @property
    def SequenceZ(self) -> DoubleSequenceSequence_6b8010c1:
        return self._sequence_z

    @SequenceZ.setter
    def SequenceZ(self, value: DoubleSequenceSequence_6b8010c1) -> None:
        self._sequence_z = value


__all__ = ['PolyPolygonShape3D']
