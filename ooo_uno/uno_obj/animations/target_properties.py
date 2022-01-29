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
import os
import typing
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class TargetProperties(object):
    """
    Struct Class

    Properties of an animated target.
    
    This struct collects all global attributes that apply to an animation target. An animation target is anything that is referenced from a given XAnimationNode tree as a target object.

    See Also:
        `API TargetProperties <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1animations_1_1TargetProperties.html>`_


    Note:
        | At runtime TargetProperties will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | TargetProperties is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, Properties: 'typing.Optional[typing.List[NamedValue_a37a0af3]]' = None, Target: typing.Optional[object] = None):
        self._properties = Properties
        self._target = Target

    @property
    def Properties(self) -> 'typing.List[NamedValue_a37a0af3]':
        """
        Global target properties.
        """
        return self._properties
    
    @Properties.setter
    def Properties(self, value: 'typing.List[NamedValue_a37a0af3]') -> None:
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

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global TargetProperties
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Properties', 'Target')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.animations.TargetProperties')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        TargetProperties = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['TargetProperties']
