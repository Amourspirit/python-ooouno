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
# Namespace: com.sun.star.ui
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.ui import ImageType as ImageType
    if hasattr(ImageType, '_constants') and isinstance(ImageType._constants, dict):
        ImageType._constants['__ooo_ns__'] = 'com.sun.star.ui'
        ImageType._constants['__ooo_full_ns__'] = 'com.sun.star.ui.ImageType'
        ImageType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ImageTypeEnum
        ls = [f for f in dir(ImageType) if not callable(getattr(ImageType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ImageType, name)
        ImageTypeEnum = IntFlag('ImageTypeEnum', _dict)
    build_enum()
else:
    from ...lo.ui.image_type import ImageType as ImageType

    class ImageTypeEnum(IntFlag):
        """
        Enum of Const Class ImageType

        Determine the image set of an image manager.
        
        The constants describe bits in a bit field which determine the current image set of an image manager.
        
        **since**
        
            OOo 2.0
        """
        SIZE_DEFAULT = ImageType.SIZE_DEFAULT
        """
        an image with default size.
        """
        SIZE_LARGE = ImageType.SIZE_LARGE
        """
        an image with large size.
        """
        SIZE_32 = ImageType.SIZE_32
        """
        an image with size 32.
        
        **since**
        
            LibreOffice 5.3
        """
        COLOR_NORMAL = ImageType.COLOR_NORMAL
        """
        an image with normal colors.
        """
        COLOR_HIGHCONTRAST = ImageType.COLOR_HIGHCONTRAST
        """
        an image with high contrast colors.
        """

__all__ = ['ImageType', 'ImageTypeEnum']
