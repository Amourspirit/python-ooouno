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
# Namespace: com.sun.star.animations
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..beans.named_value import NamedValue as NamedValue_a37a0af3


class TargetProperties(object):
    """
    Struct Class

    Properties of an animated target.
    
    This struct collects all global attributes that apply to an animation target. An animation target is anything that is referenced from a given XAnimationNode tree as a target object.

    See Also:
        `API TargetProperties <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1animations_1_1TargetProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.TargetProperties'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.animations.TargetProperties'
    """Literal Constant ``com.sun.star.animations.TargetProperties``"""

    def __init__(self, Properties: typing.Optional[typing.Tuple[NamedValue_a37a0af3, ...]] = UNO_NONE, Target: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Properties (typing.Tuple[NamedValue, ...], optional): Properties value.
            Target (object, optional): Target value.
        """
        super().__init__()

        if isinstance(Properties, TargetProperties):
            oth: TargetProperties = Properties
            self.Properties = oth.Properties
            self.Target = oth.Target
            return

        kargs = {
            "Properties": Properties,
            "Target": Target,
        }
        if kargs["Properties"] is UNO_NONE:
            kargs["Properties"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._properties = kwargs["Properties"]
        self._target = kwargs["Target"]


    @property
    def Properties(self) -> typing.Tuple[NamedValue_a37a0af3, ...]:
        """
        Global target properties.
        """
        return self._properties
    
    @Properties.setter
    def Properties(self, value: typing.Tuple[NamedValue_a37a0af3, ...]) -> None:
        self._properties = value

    @property
    def Target(self) -> object:
        """
        Target for which this struct specifies properties.
        """
        return self._target
    
    @Target.setter
    def Target(self, value: object) -> None:
        self._target = value


__all__ = ['TargetProperties']
