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
from enum import IntEnum


class AuthorDisplayFormat(object):
    """
    Const Class

    These constants are used to specify which parts of an author name are displayed in a field.

    See Also:
        `API AuthorDisplayFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1AuthorDisplayFormat.html>`_
    """
    FULL = 0
    """
    The full name of the author is displayed.
    """
    LAST_NAME = 1
    """
    Only the last name of the author is displayed.
    """
    FIRST_NAME = 2
    """
    Only the first name of the author is displayed.
    """
    INITIALS = 3
    """
    The initials of the author are displayed.
    """


class AuthorDisplayFormatEnum(IntEnum):
    """
    Enum of Const Class AuthorDisplayFormat

    These constants are used to specify which parts of an author name are displayed in a field.
    """
    FULL = AuthorDisplayFormat.FULL
    """
    The full name of the author is displayed.
    """
    LAST_NAME = AuthorDisplayFormat.LAST_NAME
    """
    Only the last name of the author is displayed.
    """
    FIRST_NAME = AuthorDisplayFormat.FIRST_NAME
    """
    Only the first name of the author is displayed.
    """
    INITIALS = AuthorDisplayFormat.INITIALS
    """
    The initials of the author are displayed.
    """

__all__ = ['AuthorDisplayFormat', 'AuthorDisplayFormatEnum']
