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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet


class MemberResultFlags(object):
    """
    Const Class

    used to give information about elements in data pilot member results.

    See Also:
        `API MemberResultFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1MemberResultFlags.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.MemberResultFlags'
    __ooo_type_name__: str = 'const'

    HASMEMBER = 1
    """
    The element contains a member.
    """
    SUBTOTAL = 2
    """
    The element contains a subtotal.
    """
    CONTINUE = 4
    """
    The element is a continuation of the previous one.
    """
    GRANDTOTAL = 8
    """
    The element contains a grand total.
    """
    NUMERIC = 16
    """
    The element is a numeric value.
    """

__all__ = ['MemberResultFlags']
