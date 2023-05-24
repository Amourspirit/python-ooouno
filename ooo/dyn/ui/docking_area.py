# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ui
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class DockingArea(metaclass=UnoEnumMeta, type_name="com.sun.star.ui.DockingArea", name_space="com.sun.star.ui"):
        """Dynamically created class that represents ``com.sun.star.ui.DockingArea`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.ui.DockingArea import DOCKINGAREA_BOTTOM as DOCKING_AREA_DOCKINGAREA_BOTTOM
        from com.sun.star.ui.DockingArea import DOCKINGAREA_DEFAULT as DOCKING_AREA_DOCKINGAREA_DEFAULT
        from com.sun.star.ui.DockingArea import DOCKINGAREA_LEFT as DOCKING_AREA_DOCKINGAREA_LEFT
        from com.sun.star.ui.DockingArea import DOCKINGAREA_RIGHT as DOCKING_AREA_DOCKINGAREA_RIGHT
        from com.sun.star.ui.DockingArea import DOCKINGAREA_TOP as DOCKING_AREA_DOCKINGAREA_TOP

        class DockingArea(uno.Enum):
            """
            Enum Class


            See Also:
                `API DockingArea <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui.html#abab7084b80a737f798ccebf692878cc1>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.ui.DockingArea', value)

            __ooo_ns__: str = 'com.sun.star.ui'
            __ooo_full_ns__: str = 'com.sun.star.ui.DockingArea'
            __ooo_type_name__: str = 'enum'

            DOCKINGAREA_BOTTOM = DOCKING_AREA_DOCKINGAREA_BOTTOM
            """
            the bottom docking area above the status bar.
            """
            DOCKINGAREA_DEFAULT = DOCKING_AREA_DOCKINGAREA_DEFAULT
            """
            a default docking area.

            It depends on the implementation how to treat this value.
            """
            DOCKINGAREA_LEFT = DOCKING_AREA_DOCKINGAREA_LEFT
            """
            the left side docking area.
            """
            DOCKINGAREA_RIGHT = DOCKING_AREA_DOCKINGAREA_RIGHT
            """
            the right side docking area.
            """
            DOCKINGAREA_TOP = DOCKING_AREA_DOCKINGAREA_TOP
            """
            the top docking area below the menu bar.
            """
    else:
        # keep document generators happy
        from ...lo.ui.docking_area import DockingArea as DockingArea


__all__ = ['DockingArea']
