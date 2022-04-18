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
# Libre Office Version: 7.3
# Namespace: com.sun.star.animations
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.animations import EventTrigger as EventTrigger
    if hasattr(EventTrigger, '_constants') and isinstance(EventTrigger._constants, dict):
        EventTrigger._constants['__ooo_ns__'] = 'com.sun.star.animations'
        EventTrigger._constants['__ooo_full_ns__'] = 'com.sun.star.animations.EventTrigger'
        EventTrigger._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global EventTriggerEnum
        ls = [f for f in dir(EventTrigger) if not callable(getattr(EventTrigger, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(EventTrigger, name)
        EventTriggerEnum = IntEnum('EventTriggerEnum', _dict)
    build_enum()
else:
    from ...lo.animations.event_trigger import EventTrigger as EventTrigger

    class EventTriggerEnum(IntEnum):
        """
        Enum of Const Class EventTrigger

        """
        NONE = EventTrigger.NONE
        """
        Nothing triggers this event.
        """
        ON_BEGIN = EventTrigger.ON_BEGIN
        ON_END = EventTrigger.ON_END
        BEGIN_EVENT = EventTrigger.BEGIN_EVENT
        """
        This event is raised when the element local timeline begins to play.
        
        It will be raised each time the element begins the active duration (i.e. when it restarts, but not when it repeats).
        """
        END_EVENT = EventTrigger.END_EVENT
        """
        This event is raised at the active end of the element.
        
        Note that this event is not raised at the simple end of each repeat.
        """
        ON_CLICK = EventTrigger.ON_CLICK
        ON_DBL_CLICK = EventTrigger.ON_DBL_CLICK
        ON_MOUSE_ENTER = EventTrigger.ON_MOUSE_ENTER
        ON_MOUSE_LEAVE = EventTrigger.ON_MOUSE_LEAVE
        ON_NEXT = EventTrigger.ON_NEXT
        """
        This event is raised when the user wants the presentation to go one step forward.
        """
        ON_PREV = EventTrigger.ON_PREV
        """
        This event is raised when the user wants the presentation to go one step backward.
        """
        ON_STOP_AUDIO = EventTrigger.ON_STOP_AUDIO
        REPEAT = EventTrigger.REPEAT
        """
        This event is raised when the element local timeline repeats.
        
        It will be raised each time the element repeats, after the first iteration.
        """

__all__ = ['EventTrigger', 'EventTriggerEnum']
