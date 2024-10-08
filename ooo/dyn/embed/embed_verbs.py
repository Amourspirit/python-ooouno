# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
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

    class EmbedVerbs(metaclass=UnoConstMeta, type_name="com.sun.star.embed.EmbedVerbs", name_space="com.sun.star.embed"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.embed.EmbedVerbs``"""
        pass

    class EmbedVerbsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.embed.EmbedVerbs", name_space="com.sun.star.embed"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.embed.EmbedVerbs`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.embed import EmbedVerbs as EmbedVerbs
    else:
        # keep document generators happy
        from ...lo.embed.embed_verbs import EmbedVerbs as EmbedVerbs

    class EmbedVerbsEnum(IntEnum):
        """
        Enum of Const Class EmbedVerbs

        This constants set contains possible verbs for a contained object.
        """
        MS_OLEVERB_PRIMARY = EmbedVerbs.MS_OLEVERB_PRIMARY
        """
        lets the object do default activation, as by double-click.
        """
        MS_OLEVERB_SHOW = EmbedVerbs.MS_OLEVERB_SHOW
        """
        lets the object open itself for editing or viewing.
        """
        MS_OLEVERB_OPEN = EmbedVerbs.MS_OLEVERB_OPEN
        """
        lets the object activate itself outplace.
        """
        MS_OLEVERB_HIDE = EmbedVerbs.MS_OLEVERB_HIDE
        """
        lets the inplace object remove its UI from container.
        """
        MS_OLEVERB_UIACTIVATE = EmbedVerbs.MS_OLEVERB_UIACTIVATE
        """
        lets the object proceed with UI activation.
        """
        MS_OLEVERB_IPACTIVATE = EmbedVerbs.MS_OLEVERB_IPACTIVATE
        """
        lets the object activate itself inplace.
        """
        MS_OLEVERB_DISCARDUNDOSTATE = EmbedVerbs.MS_OLEVERB_DISCARDUNDOSTATE
        """
        lets the object forget any undo state.
        """

__all__ = ['EmbedVerbs', 'EmbedVerbsEnum']
