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
# Namespace: com.sun.star.rendering
from enum import IntEnum


class PanoseFamilyTypes(object):
    """
    Const Class


    See Also:
        `API PanoseFamilyTypes <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1PanoseFamilyTypes.html>`_
    """
    ANYTHING = 0
    NO_FIT = 1
    TEXT_DISPLAY = 2
    SCRIPT = 3
    DECORATIVE = 4
    PICTORIAL = 5


class PanoseFamilyTypesEnum(IntEnum):
    """
    Enum of Const Class PanoseFamilyTypes

    """
    ANYTHING = PanoseFamilyTypes.ANYTHING
    NO_FIT = PanoseFamilyTypes.NO_FIT
    TEXT_DISPLAY = PanoseFamilyTypes.TEXT_DISPLAY
    SCRIPT = PanoseFamilyTypes.SCRIPT
    DECORATIVE = PanoseFamilyTypes.DECORATIVE
    PICTORIAL = PanoseFamilyTypes.PICTORIAL

__all__ = ['PanoseFamilyTypes', 'PanoseFamilyTypesEnum']
