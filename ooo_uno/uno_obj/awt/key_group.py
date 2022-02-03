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
# Namespace: com.sun.star.awt
from enum import IntEnum


class KeyGroup(object):
    """
    Const Class

    These values are used to specify functional groups of keys.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API KeyGroup <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1KeyGroup.html>`_
    """
    NUM = 256
    """
    specifies a numeric key.
    """
    ALPHA = 512
    """
    specifies an alphabetic key.
    """
    FKEYS = 768
    """
    specifies a function key.
    """
    CURSOR = 1024
    """
    specifies a cursor key.
    """
    MISC = 1280
    """
    specifies other keys.
    """
    TYPE = 3840
    """
    specifies the group mask.
    """


class KeyGroupEnum(IntEnum):
    """
    Enum of Const Class KeyGroup

    These values are used to specify functional groups of keys.
    
    .. deprecated::
    
        Class is deprecated.
    """
    NUM = KeyGroup.NUM
    """
    specifies a numeric key.
    """
    ALPHA = KeyGroup.ALPHA
    """
    specifies an alphabetic key.
    """
    FKEYS = KeyGroup.FKEYS
    """
    specifies a function key.
    """
    CURSOR = KeyGroup.CURSOR
    """
    specifies a cursor key.
    """
    MISC = KeyGroup.MISC
    """
    specifies other keys.
    """
    TYPE = KeyGroup.TYPE
    """
    specifies the group mask.
    """

__all__ = ['KeyGroup', 'KeyGroupEnum']
