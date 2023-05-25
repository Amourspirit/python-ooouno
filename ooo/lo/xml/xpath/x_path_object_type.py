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
# Namespace: com.sun.star.xml.xpath
# Libre Office Version: 7.4
from __future__ import annotations
from enum import Enum


class XPathObjectType(Enum):
    """
    Enum Class

    ENUM XPathObjectType

    See Also:
        `API XPathObjectType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1xpath.html#a4e7de3ae7d09203486b85490e0a6f1a3>`_
    """
    __ooo_ns__: str = "com.sun.star.xml.xpath"
    __ooo_full_ns__: str = "com.sun.star.xml.xpath.XPathObjectType"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.xml.xpath.XPathObjectType"

    XPATH_BOOLEAN = "XPATH_BOOLEAN"
    """
    """
    XPATH_LOCATIONSET = "XPATH_LOCATIONSET"
    """
    """
    XPATH_NODESET = "XPATH_NODESET"
    """
    """
    XPATH_NUMBER = "XPATH_NUMBER"
    """
    """
    XPATH_POINT = "XPATH_POINT"
    """
    """
    XPATH_RANGE = "XPATH_RANGE"
    """
    """
    XPATH_STRING = "XPATH_STRING"
    """
    """
    XPATH_UNDEFINED = "XPATH_UNDEFINED"
    """
    """
    XPATH_USERS = "XPATH_USERS"
    """
    """
    XPATH_XSLT_TREE = "XPATH_XSLT_TREE"
    """
    """

__all__ = ["XPathObjectType"]

