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


class ColorScaleEntryType(object):
    """
    Const Class


    See Also:
        `API ColorScaleEntryType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1ColorScaleEntryType.html>`_
    """
    COLORSCALE_MIN = 0
    COLORSCALE_MAX = 1
    COLORSCALE_PERCENTILE = 2
    COLORSCALE_VALUE = 3
    COLORSCALE_PERCENT = 4
    COLORSCALE_FORMULA = 5


class ColorScaleEntryTypeEnum(IntEnum):
    """
    Enum of Const Class ColorScaleEntryType

    """
    COLORSCALE_MIN = ColorScaleEntryType.COLORSCALE_MIN
    COLORSCALE_MAX = ColorScaleEntryType.COLORSCALE_MAX
    COLORSCALE_PERCENTILE = ColorScaleEntryType.COLORSCALE_PERCENTILE
    COLORSCALE_VALUE = ColorScaleEntryType.COLORSCALE_VALUE
    COLORSCALE_PERCENT = ColorScaleEntryType.COLORSCALE_PERCENT
    COLORSCALE_FORMULA = ColorScaleEntryType.COLORSCALE_FORMULA

__all__ = ['ColorScaleEntryType', 'ColorScaleEntryTypeEnum']
