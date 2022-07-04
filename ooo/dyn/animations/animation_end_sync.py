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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.animations
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class AnimationEndSync(metaclass=UnoConstMeta, type_name="com.sun.star.animations.AnimationEndSync", name_space="com.sun.star.animations"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.animations.AnimationEndSync``"""
        pass

    class AnimationEndSyncEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.animations.AnimationEndSync", name_space="com.sun.star.animations"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.animations.AnimationEndSync`` as Enum values"""
        pass

else:
    from ...lo.animations.animation_end_sync import AnimationEndSync as AnimationEndSync

    class AnimationEndSyncEnum(IntEnum):
        """
        Enum of Const Class AnimationEndSync

        """
        FIRST = AnimationEndSync.FIRST
        """
        The par, excl, or media element's implicit duration ends with the earliest active end of all the child elements.
        
        This does not refer to the lexical first child, or to the first child to start, but rather refers to the first child to end its (first) active duration.
        """
        LAST = AnimationEndSync.LAST
        """
        The par, excl, or media element's implicit duration ends with the last active end of the child elements.
        
        This does not refer to the lexical last child, or to the last child to start, but rather refers to the last active end of all children that have a resolved, definite begin time. If the time container has no children with a resolved begin time, the time container ends immediately. If child elements have multiple begin times, or otherwise restart, the child elements must complete all instances of active durations for resolved begin times. This is the default value for par and excl elements.
        """
        ALL = AnimationEndSync.ALL
        """
        The par, excl, or media element's implicit duration ends when all of the child elements have ended their respective active durations.
        
        Elements with indefinite or unresolved begin times will keep the simple duration of the time container from ending. When all elements have completed the active duration one or more times, the parent time container can end.
        """
        MEDIA = AnimationEndSync.MEDIA
        """
        The time container element's implicit duration ends when the intrinsic media duration of the element ends.
        
        This must be defined by a host language. If the time container element does not define an intrinsic media duration, the host language must define the simple duration for the element. This is the default value for media time container elements.
        """

__all__ = ['AnimationEndSync', 'AnimationEndSyncEnum']
