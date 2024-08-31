# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class AuthorDisplayFormat(metaclass=UnoConstMeta, type_name="com.sun.star.text.AuthorDisplayFormat", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.AuthorDisplayFormat``"""
        pass

    class AuthorDisplayFormatEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.AuthorDisplayFormat", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.AuthorDisplayFormat`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.text import AuthorDisplayFormat as AuthorDisplayFormat
    else:
        # keep document generators happy
        from ...lo.text.author_display_format import AuthorDisplayFormat as AuthorDisplayFormat

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
