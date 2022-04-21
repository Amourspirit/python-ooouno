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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..drawing.alignment import Alignment as Alignment_b1400b93


class RelativePosition(object):
    """
    Struct Class

    Determines a position of an object relative to a size defined by other means.
    
    Values from 0 to 1 cover the entire reference rectangle. Values may also be outside this range, especially negative.

    See Also:
        `API RelativePosition <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1RelativePosition.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.RelativePosition'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart2.RelativePosition'
    """Literal Constant ``com.sun.star.chart2.RelativePosition``"""

    def __init__(self, Primary: typing.Optional[float] = 0.0, Secondary: typing.Optional[float] = 0.0, Anchor: typing.Optional[Alignment_b1400b93] = Alignment_b1400b93.TOP_LEFT) -> None:
        """
        Constructor

        Arguments:
            Primary (float, optional): Primary value.
            Secondary (float, optional): Secondary value.
            Anchor (Alignment, optional): Anchor value.
        """
        super().__init__()

        if isinstance(Primary, RelativePosition):
            oth: RelativePosition = Primary
            self.Primary = oth.Primary
            self.Secondary = oth.Secondary
            self.Anchor = oth.Anchor
            return

        kargs = {
            "Primary": Primary,
            "Secondary": Secondary,
            "Anchor": Anchor,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._primary = kwargs["Primary"]
        self._secondary = kwargs["Secondary"]
        self._anchor = kwargs["Anchor"]


    @property
    def Primary(self) -> float:
        """
        The position in the primary direction.
        
        The direction is defined by the object using this point.
        
        For example for western languages the primary direction may be the horizontal distance measured from left to right.
        
        The values are relative to a reference size (for example the page size). Values between 0 and 1 span the complete bounding rectangle.
        """
        return self._primary
    
    @Primary.setter
    def Primary(self, value: float) -> None:
        self._primary = value

    @property
    def Secondary(self) -> float:
        """
        The position in the secondary direction.
        
        The direction is defined by the object using this point.
        
        For example for western languages the secondary direction may be the vertical distance measured from top to bottom.
        
        The values are relative to a reference size (for example the page size). Values between 0 and 1 span the complete bounding rectangle.
        """
        return self._secondary
    
    @Secondary.setter
    def Secondary(self, value: float) -> None:
        self._secondary = value

    @property
    def Anchor(self) -> Alignment_b1400b93:
        """
        This indicates how the object is placed at the relative position.
        
        The Anchor indicates which point of the placed object will be placed at the coordinates given within Primary and Secondary.
        
        For example if Anchor is TOP_LEFT the top left corner of an object will be placed at the given coordinates. If Anchor is RIGHT the right middle corner of the object will be placed at the given coordinates.
        """
        return self._anchor
    
    @Anchor.setter
    def Anchor(self, value: Alignment_b1400b93) -> None:
        self._anchor = value


__all__ = ['RelativePosition']
