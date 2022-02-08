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
# Namespace: com.sun.star.view
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import uno_enum_class_new
    from com.sun.star.view.PaperFormat import (A3, A4, A5, B4, B5, LEGAL, LETTER, TABLOID, USER)

    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global PaperFormat
        _dict = {
            "A3": A3,
            "A4": A4,
            "A5": A5,
            "B4": B4,
            "B5": B5,
            "LEGAL": LEGAL,
            "LETTER": LETTER,
            "TABLOID": TABLOID,
            "USER": USER,
        }

        PaperFormat = type('PaperFormat', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(PaperFormat, k, v)
        setattr(PaperFormat, '__ooo_ns__', 'com.sun.star.view')
        setattr(PaperFormat, '__ooo_full_ns__', 'com.sun.star.view.PaperFormat')
        setattr(PaperFormat, '__ooo_type_name__', 'enum')
    _dynamic_enum()
else:
    from ...lo.view.paper_format import PaperFormat as PaperFormat

__all__ = ['PaperFormat']

