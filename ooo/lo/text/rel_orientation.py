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
# Namespace: com.sun.star.text


class RelOrientation(object):
    """
    Const Class

    These values define the reference position of relative orientations.
    
    **since**
    
        LibreOffice 7.0

    See Also:
        `API RelOrientation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1RelOrientation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.RelOrientation'
    __ooo_type_name__: str = 'const'

    FRAME = 0
    """
    paragraph, including margins
    """
    PRINT_AREA = 1
    """
    paragraph, without margins
    """
    CHAR = 2
    """
    at a character
    """
    PAGE_LEFT = 3
    """
    inside the left page margin
    """
    PAGE_RIGHT = 4
    """
    inside the right page margin
    """
    FRAME_LEFT = 5
    """
    inside the left paragraph margin
    """
    FRAME_RIGHT = 6
    """
    inside the right paragraph margin
    """
    PAGE_FRAME = 7
    """
    page includes margins for page-anchored frames identical with RelOrientation.FRAME
    """
    PAGE_PRINT_AREA = 8
    """
    page without borders (for page anchored frames identical with RelOrientation.PRINT_AREA).
    """
    TEXT_LINE = 9
    """
    at the top of the text line, only sensible for vertical orientation.
    
    **since**
    
        OOo 2.0
    """
    PAGE_PRINT_AREA_BOTTOM = 10
    """
    Bottom page border (page area below PAGE_PRINT_AREA).
    
    **since**
    
        LibreOffice 7.0
    """
    PAGE_PRINT_AREA_TOP = 11
    """
    Top page border (page area above PAGE_PRINT_AREA).
    
    **since**
    
        LibreOffice 7.1
    """

__all__ = ['RelOrientation']
