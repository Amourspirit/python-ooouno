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


class FontEmphasis(object):
    """
    Const Class

    Determines the type and position of an emphasis mark in Asian texts.

    See Also:
        `API FontEmphasis <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1FontEmphasis.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.FontEmphasis'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    no emphasis mark is used.
    """
    DOT_ABOVE = 1
    """
    a dot is set above (or right from vertical text) the text.
    """
    CIRCLE_ABOVE = 2
    """
    a circle is set above (or right from vertical text) the text.
    """
    DISK_ABOVE = 3
    """
    a disc is set above (or right from vertical text) the text.
    """
    ACCENT_ABOVE = 4
    """
    an accent is set above (or right from vertical text) the text.
    """
    DOT_BELOW = 11
    """
    a dot is set below (or left from vertical text) the text.
    """
    CIRCLE_BELOW = 12
    """
    a circle is set below (or left from vertical text) the text.
    """
    DISK_BELOW = 13
    """
    a disk is set below (or left from vertical text) the text.
    """
    ACCENT_BELOW = 14
    """
    an accent is set below (or left from vertical text) the text.
    """

__all__ = ['FontEmphasis']