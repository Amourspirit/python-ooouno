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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.ui
import typing
from abc import abstractmethod
from .x_accelerator_configuration import XAcceleratorConfiguration as XAcceleratorConfiguration_46580ffb
if typing.TYPE_CHECKING:
    from ..embed.x_storage import XStorage as XStorage_8e460a32

class DocumentAcceleratorConfiguration(XAcceleratorConfiguration_46580ffb):
    """
    Service Class

    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API DocumentAcceleratorConfiguration <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1DocumentAcceleratorConfiguration.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.DocumentAcceleratorConfiguration'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithDocumentRoot(self, DocumentRoot: 'XStorage_8e460a32') -> None:
        """
        """

__all__ = ['DocumentAcceleratorConfiguration']

