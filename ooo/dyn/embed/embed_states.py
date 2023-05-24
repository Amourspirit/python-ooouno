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
# Namespace: com.sun.star.embed
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class EmbedStates(metaclass=UnoConstMeta, type_name="com.sun.star.embed.EmbedStates", name_space="com.sun.star.embed"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.embed.EmbedStates``"""
        pass

    class EmbedStatesEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.embed.EmbedStates", name_space="com.sun.star.embed"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.embed.EmbedStates`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.embed import EmbedStates as EmbedStates
    else:
        # keep document generators happy
        from ...lo.embed.embed_states import EmbedStates as EmbedStates

    class EmbedStatesEnum(IntEnum):
        """
        Enum of Const Class EmbedStates

        This constant set contains possible states for EmbeddedObject.
        """
        LOADED = EmbedStates.LOADED
        """
        \"Loaded\" - the persistent representation of the object is loaded in memory.
        
        The object is created and assigned with a persistent entry, and a view representation ( metafile and etc. ) can be retrieved ( if there is any ).
        """
        RUNNING = EmbedStates.RUNNING
        """
        \"Running\" - the object is connected and loaded.
        
        The object has a connection to the container client and a component loaded from persistent entry. In case of internal document it also means existing of document model that implements com.sun.star.frame.XModel interface.
        """
        ACTIVE = EmbedStates.ACTIVE
        """
        \"Active\" - the object is activated in separate window ( outplace activation ).
        """
        INPLACE_ACTIVE = EmbedStates.INPLACE_ACTIVE
        """
        \"Inplace active\" - the object has own window in the container's window.
        
        The object is activated and has its own window in the container's window that allows object to process mouse events and control own rendering.
        """
        UI_ACTIVE = EmbedStates.UI_ACTIVE
        """
        \"UI active\" - the inplace active object that has user interface.
        
        The object is inplace active, allowed to have menus, toolbars, keyboard accelerators, and has the focus.
        """

__all__ = ['EmbedStates', 'EmbedStatesEnum']
