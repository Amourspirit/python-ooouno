# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.xml.dom.DOMExceptionType import DOMSTRING_SIZE_ERR as D_O_M_EXCEPTION_TYPE_DOMSTRING_SIZE_ERR
    from com.sun.star.xml.dom.DOMExceptionType import HIERARCHY_REQUEST_ERR as D_O_M_EXCEPTION_TYPE_HIERARCHY_REQUEST_ERR
    from com.sun.star.xml.dom.DOMExceptionType import INDEX_SIZE_ERR as D_O_M_EXCEPTION_TYPE_INDEX_SIZE_ERR
    from com.sun.star.xml.dom.DOMExceptionType import INUSE_ATTRIBUTE_ERR as D_O_M_EXCEPTION_TYPE_INUSE_ATTRIBUTE_ERR
    from com.sun.star.xml.dom.DOMExceptionType import INVALID_ACCESS_ERR as D_O_M_EXCEPTION_TYPE_INVALID_ACCESS_ERR
    from com.sun.star.xml.dom.DOMExceptionType import INVALID_CHARACTER_ERR as D_O_M_EXCEPTION_TYPE_INVALID_CHARACTER_ERR
    from com.sun.star.xml.dom.DOMExceptionType import INVALID_MODIFICATION_ERR as D_O_M_EXCEPTION_TYPE_INVALID_MODIFICATION_ERR
    from com.sun.star.xml.dom.DOMExceptionType import INVALID_STATE_ERR as D_O_M_EXCEPTION_TYPE_INVALID_STATE_ERR
    from com.sun.star.xml.dom.DOMExceptionType import NAMESPACE_ERR as D_O_M_EXCEPTION_TYPE_NAMESPACE_ERR
    from com.sun.star.xml.dom.DOMExceptionType import NOT_FOUND_ERR as D_O_M_EXCEPTION_TYPE_NOT_FOUND_ERR
    from com.sun.star.xml.dom.DOMExceptionType import NOT_SUPPORTED_ERR as D_O_M_EXCEPTION_TYPE_NOT_SUPPORTED_ERR
    from com.sun.star.xml.dom.DOMExceptionType import NO_DATA_ALLOWED_ERR as D_O_M_EXCEPTION_TYPE_NO_DATA_ALLOWED_ERR
    from com.sun.star.xml.dom.DOMExceptionType import NO_MODIFICATION_ALLOWED_ERR as D_O_M_EXCEPTION_TYPE_NO_MODIFICATION_ALLOWED_ERR
    from com.sun.star.xml.dom.DOMExceptionType import SYNTAX_ERR as D_O_M_EXCEPTION_TYPE_SYNTAX_ERR
    from com.sun.star.xml.dom.DOMExceptionType import WRONG_DOCUMENT_ERR as D_O_M_EXCEPTION_TYPE_WRONG_DOCUMENT_ERR

    class DOMExceptionType(uno.Enum):
        """
        Enum Class

        ENUM DOMExceptionType

        See Also:
            `API DOMExceptionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1dom.html#a31e3fb46d584de1cfc4b4c7640a41239>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.xml.dom.DOMExceptionType', value)

        __ooo_ns__: str = 'com.sun.star.xml.dom'
        __ooo_full_ns__: str = 'com.sun.star.xml.dom.DOMExceptionType'
        __ooo_type_name__: str = 'enum'

        DOMSTRING_SIZE_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_DOMSTRING_SIZE_ERR)
        """
        """
        HIERARCHY_REQUEST_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_HIERARCHY_REQUEST_ERR)
        """
        """
        INDEX_SIZE_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_INDEX_SIZE_ERR)
        """
        """
        INUSE_ATTRIBUTE_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_INUSE_ATTRIBUTE_ERR)
        """
        """
        INVALID_ACCESS_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_INVALID_ACCESS_ERR)
        """
        """
        INVALID_CHARACTER_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_INVALID_CHARACTER_ERR)
        """
        """
        INVALID_MODIFICATION_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_INVALID_MODIFICATION_ERR)
        """
        """
        INVALID_STATE_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_INVALID_STATE_ERR)
        """
        """
        NAMESPACE_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_NAMESPACE_ERR)
        """
        """
        NOT_FOUND_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_NOT_FOUND_ERR)
        """
        """
        NOT_SUPPORTED_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_NOT_SUPPORTED_ERR)
        """
        """
        NO_DATA_ALLOWED_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_NO_DATA_ALLOWED_ERR)
        """
        """
        NO_MODIFICATION_ALLOWED_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_NO_MODIFICATION_ALLOWED_ERR)
        """
        """
        SYNTAX_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_SYNTAX_ERR)
        """
        """
        WRONG_DOCUMENT_ERR = cast("DOMExceptionType", D_O_M_EXCEPTION_TYPE_WRONG_DOCUMENT_ERR)
        """
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class DOMExceptionType(metaclass=UnoEnumMeta, type_name="com.sun.star.xml.dom.DOMExceptionType", name_space="com.sun.star.xml.dom"):
        """Dynamically created class that represents ``com.sun.star.xml.dom.DOMExceptionType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['DOMExceptionType']
