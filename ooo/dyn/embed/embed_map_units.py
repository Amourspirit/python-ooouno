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

    class EmbedMapUnits(metaclass=UnoConstMeta, type_name="com.sun.star.embed.EmbedMapUnits", name_space="com.sun.star.embed"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.embed.EmbedMapUnits``"""
        pass

    class EmbedMapUnitsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.embed.EmbedMapUnits", name_space="com.sun.star.embed"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.embed.EmbedMapUnits`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.embed import EmbedMapUnits as EmbedMapUnits
    else:
        # keep document generators happy
        from ...lo.embed.embed_map_units import EmbedMapUnits as EmbedMapUnits

    class EmbedMapUnitsEnum(IntEnum):
        """
        Enum of Const Class EmbedMapUnits

        contains list of possible map modes supported by embedded object.
        """
        ONE_100TH_MM = EmbedMapUnits.ONE_100TH_MM
        """
        In this type of map mode one logical point is equal to one-hundredth of millimeter.
        """
        ONE_10TH_MM = EmbedMapUnits.ONE_10TH_MM
        """
        In this type of map mode one logical point is equal to one-tenth of millimeter.
        """
        ONE_MM = EmbedMapUnits.ONE_MM
        """
        In this type of map mode one logical point is equal to one millimeter.
        """
        ONE_CM = EmbedMapUnits.ONE_CM
        """
        In this type of map mode one logical point is equal to one centimeter.
        """
        ONE_1000TH_INCH = EmbedMapUnits.ONE_1000TH_INCH
        """
        In this type of map mode one logical point is equal to one-thousandth of inch.
        """
        ONE_100TH_INCH = EmbedMapUnits.ONE_100TH_INCH
        """
        In this type of map mode one logical point is equal to one-hundredth of inch.
        """
        ONE_10TH_INCH = EmbedMapUnits.ONE_10TH_INCH
        """
        In this type of map mode one logical point is equal to one-tenth of inch.
        """
        ONE_INCH = EmbedMapUnits.ONE_INCH
        """
        In this type of map mode one logical point is equal to one inch.
        """
        POINT = EmbedMapUnits.POINT
        """
        In this type of map mode one logical point is equal to one typographical point.
        """
        TWIP = EmbedMapUnits.TWIP
        """
        In this type of map mode one logical point is equal to one twentieth of typographical point.
        """
        PIXEL = EmbedMapUnits.PIXEL
        """
        In this type of map mode one logical point is equal to one pixel.
        """

__all__ = ['EmbedMapUnits', 'EmbedMapUnitsEnum']
