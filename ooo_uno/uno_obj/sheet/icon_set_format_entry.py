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
# Namespace: com.sun.star.sheet
from enum import IntEnum


class IconSetFormatEntry(object):
    """
    Const Class


    See Also:
        `API IconSetFormatEntry <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1IconSetFormatEntry.html>`_
    """
    ICONSET_MIN = 0
    """
    Can not be set! Will always be the type of the first entry.
    """
    ICONSET_PERCENTILE = 1
    ICONSET_VALUE = 2
    ICONSET_PERCENT = 3
    ICONSET_FORMULA = 4


class IconSetFormatEntryEnum(IntEnum):
    """
    Enum of Const Class IconSetFormatEntry

    """
    ICONSET_MIN = IconSetFormatEntry.ICONSET_MIN
    """
    Can not be set! Will always be the type of the first entry.
    """
    ICONSET_PERCENTILE = IconSetFormatEntry.ICONSET_PERCENTILE
    ICONSET_VALUE = IconSetFormatEntry.ICONSET_VALUE
    ICONSET_PERCENT = IconSetFormatEntry.ICONSET_PERCENT
    ICONSET_FORMULA = IconSetFormatEntry.ICONSET_FORMULA

__all__ = ['IconSetFormatEntry', 'IconSetFormatEntryEnum']
