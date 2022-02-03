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


class DataPilotFieldReferenceItemType(object):
    """
    Const Class

    is used to select the reference item

    See Also:
        `API DataPilotFieldReferenceItemType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldReferenceItemType.html>`_
    """
    NAMED = 0
    """
    the reference item is given by a name.
    """
    PREVIOUS = 1
    """
    the reference item is the previous one.
    """
    NEXT = 2
    """
    the reference item is the next one.
    """


class DataPilotFieldReferenceItemTypeEnum(IntEnum):
    """
    Enum of Const Class DataPilotFieldReferenceItemType

    is used to select the reference item
    """
    NAMED = DataPilotFieldReferenceItemType.NAMED
    """
    the reference item is given by a name.
    """
    PREVIOUS = DataPilotFieldReferenceItemType.PREVIOUS
    """
    the reference item is the previous one.
    """
    NEXT = DataPilotFieldReferenceItemType.NEXT
    """
    the reference item is the next one.
    """

__all__ = ['DataPilotFieldReferenceItemType', 'DataPilotFieldReferenceItemTypeEnum']
