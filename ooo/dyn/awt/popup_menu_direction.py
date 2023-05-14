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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class PopupMenuDirection(metaclass=UnoConstMeta, type_name="com.sun.star.awt.PopupMenuDirection", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.PopupMenuDirection``"""
        pass

    class PopupMenuDirectionEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.PopupMenuDirection", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.PopupMenuDirection`` as Enum values"""
        pass

else:
    from ...lo.awt.popup_menu_direction import PopupMenuDirection as PopupMenuDirection

    class PopupMenuDirectionEnum(IntFlag):
        """
        Enum of Const Class PopupMenuDirection

        These values are used to specify the direction in which a pop-up menu will grow.
        
        They may be expanded in future versions.
        """
        EXECUTE_DEFAULT = PopupMenuDirection.EXECUTE_DEFAULT
        """
        opens on execute in a default direction.
        """
        EXECUTE_DOWN = PopupMenuDirection.EXECUTE_DOWN
        """
        opens on execute downwards.
        """
        EXECUTE_UP = PopupMenuDirection.EXECUTE_UP
        """
        opens on execute upwards.
        """
        EXECUTE_LEFT = PopupMenuDirection.EXECUTE_LEFT
        """
        opens on execute to the left.
        """
        EXECUTE_RIGHT = PopupMenuDirection.EXECUTE_RIGHT
        """
        opens on execute to the right.
        """

__all__ = ['PopupMenuDirection', 'PopupMenuDirectionEnum']
