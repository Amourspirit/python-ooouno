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
# Namespace: com.sun.star.text


class SizeType(object):
    """
    Const Class

    The height value of objects like text frames or table rows may be interpreted in different ways.
    
    The values may specify the absolute height (SIZETYPE_FIX), the minimum height (SIZETYPE_MIN), or they are ignored (SIZETYPE_VAR), in which case the real height depends on the content. This information is contained in a property called \"SizeType\".

    See Also:
        `API SizeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1SizeType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.SizeType'
    __ooo_type_name__: str = 'const'

    VARIABLE = 0
    FIX = 1
    MIN = 2
    """
    The height property determines the minimum height of the object, but the actual height will be increased if the content demands it.
    """

__all__ = ['SizeType']