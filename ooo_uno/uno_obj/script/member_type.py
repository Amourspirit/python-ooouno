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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script
# Libre Office Version: 7.2
import os
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.script.MemberType import (METHOD, PROPERTY, UNKNOWN)


class MemberType(Enum):
    """
    

    See Also:
        `API MemberType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1script.html#a63e3de542c5d38de617ab78c8c8f5a41>`_
    """
    METHOD = 'METHOD'
    """
    """
    PROPERTY = 'PROPERTY'
    """
    """
    UNKNOWN = 'UNKNOWN'
    """
    """

def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global MemberType
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "METHOD": METHOD,
            "PROPERTY": PROPERTY,
            "UNKNOWN": UNKNOWN,
        }
        MemberType = type('MemberType', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(MemberType, k, v)

if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['MemberType']

