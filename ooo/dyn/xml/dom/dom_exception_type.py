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
# Namespace: com.sun.star.xml.dom
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import uno_enum_class_new
    from com.sun.star.xml.dom.DOMExceptionType import (DOMSTRING_SIZE_ERR, HIERARCHY_REQUEST_ERR, INDEX_SIZE_ERR, INUSE_ATTRIBUTE_ERR, INVALID_ACCESS_ERR, INVALID_CHARACTER_ERR, INVALID_MODIFICATION_ERR, INVALID_STATE_ERR, NAMESPACE_ERR, NOT_FOUND_ERR, NOT_SUPPORTED_ERR, NO_DATA_ALLOWED_ERR, NO_MODIFICATION_ALLOWED_ERR, SYNTAX_ERR, WRONG_DOCUMENT_ERR)

    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global DOMExceptionType
        _dict = {
            "__doc__": "Dynamically created class that represents com.sun.star.xml.dom.DOMExceptionType Enum. Class loosly mimics Enum",
            "__new__": uno_enum_class_new,
            "__ooo_ns__": "com.sun.star.xml.dom",
            "__ooo_full_ns__": "com.sun.star.xml.dom.DOMExceptionType",
            "__ooo_type_name__": "enum",
            "DOMSTRING_SIZE_ERR": DOMSTRING_SIZE_ERR,
            "HIERARCHY_REQUEST_ERR": HIERARCHY_REQUEST_ERR,
            "INDEX_SIZE_ERR": INDEX_SIZE_ERR,
            "INUSE_ATTRIBUTE_ERR": INUSE_ATTRIBUTE_ERR,
            "INVALID_ACCESS_ERR": INVALID_ACCESS_ERR,
            "INVALID_CHARACTER_ERR": INVALID_CHARACTER_ERR,
            "INVALID_MODIFICATION_ERR": INVALID_MODIFICATION_ERR,
            "INVALID_STATE_ERR": INVALID_STATE_ERR,
            "NAMESPACE_ERR": NAMESPACE_ERR,
            "NOT_FOUND_ERR": NOT_FOUND_ERR,
            "NOT_SUPPORTED_ERR": NOT_SUPPORTED_ERR,
            "NO_DATA_ALLOWED_ERR": NO_DATA_ALLOWED_ERR,
            "NO_MODIFICATION_ALLOWED_ERR": NO_MODIFICATION_ALLOWED_ERR,
            "SYNTAX_ERR": SYNTAX_ERR,
            "WRONG_DOCUMENT_ERR": WRONG_DOCUMENT_ERR,
        }

        DOMExceptionType = type('DOMExceptionType', (object,), _dict)
    _dynamic_enum()
else:
    from ....lo.xml.dom.dom_exception_type import DOMExceptionType as DOMExceptionType

__all__ = ['DOMExceptionType']

