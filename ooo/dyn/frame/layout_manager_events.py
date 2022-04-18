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
# Namespace: com.sun.star.frame
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.frame import LayoutManagerEvents as LayoutManagerEvents
    if hasattr(LayoutManagerEvents, '_constants') and isinstance(LayoutManagerEvents._constants, dict):
        LayoutManagerEvents._constants['__ooo_ns__'] = 'com.sun.star.frame'
        LayoutManagerEvents._constants['__ooo_full_ns__'] = 'com.sun.star.frame.LayoutManagerEvents'
        LayoutManagerEvents._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global LayoutManagerEventsEnum
        ls = [f for f in dir(LayoutManagerEvents) if not callable(getattr(LayoutManagerEvents, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(LayoutManagerEvents, name)
        LayoutManagerEventsEnum = IntEnum('LayoutManagerEventsEnum', _dict)
    build_enum()
else:
    from ...lo.frame.layout_manager_events import LayoutManagerEvents as LayoutManagerEvents

    class LayoutManagerEventsEnum(IntEnum):
        """
        Enum of Const Class LayoutManagerEvents

        provides information about layout manager events
        
        Events are provided only for notification purposes only.
        
        **since**
        
            OOo 2.0
        """
        LOCK = LayoutManagerEvents.LOCK
        """
        specifies that the layout manager processed a lock call, which prevents it from doing layouts.
        
        This event sends the current lock count as additional information.
        """
        UNLOCK = LayoutManagerEvents.UNLOCK
        """
        specifies that the layout manager processed an unlock call, which admit layouts when the lock count is zero.
        
        This event sends the current lock count as additional information.
        """
        LAYOUT = LayoutManagerEvents.LAYOUT
        """
        specifies that the layout manager refreshed the layout of the frame.
        
        This event sends no additional information.
        """
        VISIBLE = LayoutManagerEvents.VISIBLE
        """
        specifies that the layout manager container frame window becomes visible.
        
        This event sends no additional information.
        """
        INVISIBLE = LayoutManagerEvents.INVISIBLE
        """
        specifies that the layout manager container frame window becomes invisible.
        
        This event sends no additional information.
        """
        MERGEDMENUBAR = LayoutManagerEvents.MERGEDMENUBAR
        """
        A merged menu bar has been set at the layout manager.
        
        This event sends no additional information.
        """
        UIELEMENT_VISIBLE = LayoutManagerEvents.UIELEMENT_VISIBLE
        """
        specifies that a certain user interface element has been made visible
        
        This event sends the resource url of the newly visible user interface element.
        """
        UIELEMENT_INVISIBLE = LayoutManagerEvents.UIELEMENT_INVISIBLE
        """
        specifies that a certain user interface element has been made invisible
        
        This event sends the resource url of the invisible user interface element.
        """

__all__ = ['LayoutManagerEvents', 'LayoutManagerEventsEnum']
