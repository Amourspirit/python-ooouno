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
# Namespace: com.sun.star.sdbcx
from ooo_uno.base.const import ConstIntBase


class CompareBookmark(ConstIntBase):
    """
    describes the result of a comparison of two bookmarks.

    See Also:
        `API CompareBookmark <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbcx_1_1CompareBookmark.html>`_
    """
    LESS = -1
    """
    the first bookmark is before the second.
    """
    EQUAL = 0
    """
    the first bookmark is equal to the second.
    """
    GREATER = 1
    """
    the first bookmark is after the second one.
    """
    NOT_EQUAL = 2
    """
    the first bookmark is not the same as the second one.
    """
    NOT_COMPARABLE = 3
    """
    the two bookmarks are not comparable.
    """

