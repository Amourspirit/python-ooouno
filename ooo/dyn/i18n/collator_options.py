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
# Namespace: com.sun.star.i18n
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class CollatorOptions(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.CollatorOptions", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.CollatorOptions``"""
        pass

    class CollatorOptionsEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.CollatorOptions", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.CollatorOptions`` as Enum values"""
        pass

else:
    from ...lo.i18n.collator_options import CollatorOptions as CollatorOptions

    class CollatorOptionsEnum(IntFlag):
        """
        Enum of Const Class CollatorOptions

        Options to be used with XCollator methods.
        """
        CollatorOptions_IGNORE_CASE = CollatorOptions.CollatorOptions_IGNORE_CASE
        """
        Ignore case.
        """
        CollatorOptions_IGNORE_KANA = CollatorOptions.CollatorOptions_IGNORE_KANA
        """
        Ignore Kana.
        """
        CollatorOptions_IGNORE_WIDTH = CollatorOptions.CollatorOptions_IGNORE_WIDTH
        """
        Ignore width.
        """
        CollatorOptions_IGNORE_CASE_ACCENT = CollatorOptions.CollatorOptions_IGNORE_CASE_ACCENT
        """
        Ignore case and accent.
        """

__all__ = ['CollatorOptions', 'CollatorOptionsEnum']
