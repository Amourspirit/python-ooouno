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
# Libre Office Version: 7.4
# Namespace: com.sun.star.embed
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class Aspects(metaclass=UnoConstMeta, type_name="com.sun.star.embed.Aspects", name_space="com.sun.star.embed"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.embed.Aspects``"""
        pass

    class AspectsEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.embed.Aspects", name_space="com.sun.star.embed"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.embed.Aspects`` as Enum values"""
        pass

else:
    from ...lo.embed.aspects import Aspects as Aspects

    class AspectsEnum(IntFlag):
        """
        Enum of Const Class Aspects

        The constant set contains possible aspects for an embedded object.
        
        This constant set provides a set of values that can be used to specify the kind of object view. It can be used for example by container to request view representation of a certain kind from XEmbeddedObject.
        
        The first 32 bits are reserved for MS OLE aspects.
        """
        MSOLE_CONTENT = Aspects.MSOLE_CONTENT
        """
        specifies view of the object to be displayed as an embedded object inside a container.
        """
        MSOLE_THUMBNAIL = Aspects.MSOLE_THUMBNAIL
        """
        specifies view of the object to be displayed in a browsing tool.
        """
        MSOLE_ICON = Aspects.MSOLE_ICON
        """
        specifies view of the object when object is represented by Icon.
        """
        MSOLE_DOCPRINT = Aspects.MSOLE_DOCPRINT
        """
        specifies view of the object for print preview.
        """

__all__ = ['Aspects', 'AspectsEnum']
