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
import typing
if typing.TYPE_CHECKING:
    from .sub_increment import SubIncrement as SubIncrement_c5630c1b
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class IncrementData(object):
        """
        Struct Class

        An IncrementData describes how tickmarks are positioned on the scale of an axis.

        See Also:
            `API IncrementData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1IncrementData.html>`_


        Note:
            | At runtime IncrementData will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | IncrementData is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, BaseValue: typing.Optional[object] = None, Distance: typing.Optional[object] = None, PostEquidistant: typing.Optional[object] = None, SubIncrements: 'typing.Optional[typing.List[SubIncrement_c5630c1b]]' = None):
            self._base_value = BaseValue
            self._distance = Distance
            self._post_equidistant = PostEquidistant
            self._sub_increments = SubIncrements

        @property
        def BaseValue(self) -> object:
            """
            if the any contains a double value this is used as a fixed BaseValue.
            
            Otherwise, if the any is empty or contains an incompatible type, the BaseValue is meant to be calculated automatically by the view component representing the model containing this increment.
            """
            return self._base_value
        
        @BaseValue.setter
        def BaseValue(self, value: object) -> None:
            self._base_value = value

        @property
        def Distance(self) -> object:
            """
            if the any contains a double value this is used as a fixed Distance value.
            
            Otherwise, if the any is empty or contains an incompatible type, the Distance is meant to be calculated automatically by the view component representing the model containing this increment.
            """
            return self._distance
        
        @Distance.setter
        def Distance(self, value: object) -> None:
            self._distance = value

        @property
        def PostEquidistant(self) -> object:
            """
            PostEquidistant rules whether the member Distance describes a distance before or after the scaling is applied.
            
            If PostEquidistant equals TRUE Distance is given in values after XScaling is applied, thus resulting main tickmarks will always look equidistant on the screen. If PostEquidistant equals FALSE Distance is given in values before XScaling is applied.
            """
            return self._post_equidistant
        
        @PostEquidistant.setter
        def PostEquidistant(self, value: object) -> None:
            self._post_equidistant = value

        @property
        def SubIncrements(self) -> 'typing.List[SubIncrement_c5630c1b]':
            """
            SubIncrements describes the positioning of further sub tickmarks on the scale of an axis.
            
            The first SubIncrement in this sequence determines how the distance between two neighboring main tickmarks is divided for positioning of further sub tickmarks. Every following SubIncrement determines the positions of subsequent tickmarks in relation to their parent tickmarks given by the preceding SubIncrement.
            """
            return self._sub_increments
        
        @SubIncrements.setter
        def SubIncrements(self, value: 'typing.List[SubIncrement_c5630c1b]') -> None:
            self._sub_increments = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global IncrementData
        order = ('BaseValue', 'Distance', 'PostEquidistant', 'SubIncrements')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.chart2.IncrementData')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        IncrementData = _struct_init

    _dynamic_struct()

__all__ = ['IncrementData']
