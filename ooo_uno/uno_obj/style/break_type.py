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
# Namespace: com.sun.star.style
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.style.BreakType import (COLUMN_AFTER, COLUMN_BEFORE, COLUMN_BOTH, NONE, PAGE_AFTER, PAGE_BEFORE, PAGE_BOTH)

if TYPE_CHECKING or _DYNAMIC is False:


    class BreakType(Enum):
        """
        Enum Class

        

        See Also:
            `API BreakType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925>`_
        """
        COLUMN_AFTER = 'COLUMN_AFTER'
        """
        A column break is applied after the object to which it belongs.
        """
        COLUMN_BEFORE = 'COLUMN_BEFORE'
        """
        A column break is applied before the object to which it belongs.
        """
        COLUMN_BOTH = 'COLUMN_BOTH'
        """
        A column break is applied before and after the object to which it belongs.
        """
        NONE = 'NONE'
        """
        No column or page break is applied.
        
        This value specifies that a location is not yet assigned.
        """
        PAGE_AFTER = 'PAGE_AFTER'
        """
        A page break is applied after the object to which it belongs.
        """
        PAGE_BEFORE = 'PAGE_BEFORE'
        """
        A page break is applied before the object to which it belongs.
        """
        PAGE_BOTH = 'PAGE_BOTH'
        """
        A page break is applied before and after the object to which it belongs.
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global BreakType
        _dict = {
            "COLUMN_AFTER": COLUMN_AFTER,
            "COLUMN_BEFORE": COLUMN_BEFORE,
            "COLUMN_BOTH": COLUMN_BOTH,
            "NONE": NONE,
            "PAGE_AFTER": PAGE_AFTER,
            "PAGE_BEFORE": PAGE_BEFORE,
            "PAGE_BOTH": PAGE_BOTH,
        }

        BreakType = type('BreakType', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(BreakType, k, v)

    _dynamic_enum()

__all__ = ['BreakType']

