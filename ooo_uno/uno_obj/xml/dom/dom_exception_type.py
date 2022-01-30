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
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.xml.dom.DOMExceptionType import (DOMSTRING_SIZE_ERR, HIERARCHY_REQUEST_ERR, INDEX_SIZE_ERR, INUSE_ATTRIBUTE_ERR, INVALID_ACCESS_ERR, INVALID_CHARACTER_ERR, INVALID_MODIFICATION_ERR, INVALID_STATE_ERR, NAMESPACE_ERR, NOT_FOUND_ERR, NOT_SUPPORTED_ERR, NO_DATA_ALLOWED_ERR, NO_MODIFICATION_ALLOWED_ERR, SYNTAX_ERR, WRONG_DOCUMENT_ERR)

if TYPE_CHECKING or _DYNAMIC is False:


    class DOMExceptionType(Enum):
        """
        Enum Class

        ENUM DOMExceptionType

        See Also:
            `API DOMExceptionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1dom.html#a31e3fb46d584de1cfc4b4c7640a41239>`_
        """
        DOMSTRING_SIZE_ERR = 'DOMSTRING_SIZE_ERR'
        """
        """
        HIERARCHY_REQUEST_ERR = 'HIERARCHY_REQUEST_ERR'
        """
        """
        INDEX_SIZE_ERR = 'INDEX_SIZE_ERR'
        """
        """
        INUSE_ATTRIBUTE_ERR = 'INUSE_ATTRIBUTE_ERR'
        """
        """
        INVALID_ACCESS_ERR = 'INVALID_ACCESS_ERR'
        """
        """
        INVALID_CHARACTER_ERR = 'INVALID_CHARACTER_ERR'
        """
        """
        INVALID_MODIFICATION_ERR = 'INVALID_MODIFICATION_ERR'
        """
        """
        INVALID_STATE_ERR = 'INVALID_STATE_ERR'
        """
        """
        NAMESPACE_ERR = 'NAMESPACE_ERR'
        """
        """
        NOT_FOUND_ERR = 'NOT_FOUND_ERR'
        """
        """
        NOT_SUPPORTED_ERR = 'NOT_SUPPORTED_ERR'
        """
        """
        NO_DATA_ALLOWED_ERR = 'NO_DATA_ALLOWED_ERR'
        """
        """
        NO_MODIFICATION_ALLOWED_ERR = 'NO_MODIFICATION_ALLOWED_ERR'
        """
        """
        SYNTAX_ERR = 'SYNTAX_ERR'
        """
        """
        WRONG_DOCUMENT_ERR = 'WRONG_DOCUMENT_ERR'
        """
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global DOMExceptionType
        _dict = {
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

        DOMExceptionType = type('DOMExceptionType', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(DOMExceptionType, k, v)

    _dynamic_enum()

__all__ = ['DOMExceptionType']

