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
# Namespace: com.sun.star.ui.dialogs
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

    class FilePreviewImageFormats(metaclass=UnoConstMeta, type_name="com.sun.star.ui.dialogs.FilePreviewImageFormats", name_space="com.sun.star.ui.dialogs"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.ui.dialogs.FilePreviewImageFormats``"""
        pass

    class FilePreviewImageFormatsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.ui.dialogs.FilePreviewImageFormats", name_space="com.sun.star.ui.dialogs"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.ui.dialogs.FilePreviewImageFormats`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.ui.dialogs import FilePreviewImageFormats as FilePreviewImageFormats
    else:
        # keep document generators happy
        from ....lo.ui.dialogs.file_preview_image_formats import FilePreviewImageFormats as FilePreviewImageFormats

    class FilePreviewImageFormatsEnum(IntEnum):
        """
        Enum of Const Class FilePreviewImageFormats

        These constants are used to specify image formats supported by an implementation of the interface com.sun.star.ui.dialogs.XFilePreview.
        """
        BITMAP = FilePreviewImageFormats.BITMAP
        """
        A LibreOffice bitmap which is similar to the device independent bitmap (DIB) format on windows.
        
        The bitmap data should be provided as a sequence of sal_Int8.
        """

__all__ = ['FilePreviewImageFormats', 'FilePreviewImageFormatsEnum']
