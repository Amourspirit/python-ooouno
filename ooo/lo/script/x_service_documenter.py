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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.script
import typing
from abc import abstractmethod, abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..lang.x_service_info import XServiceInfo as XServiceInfo_af180b5f
    from ..lang.x_type_provider import XTypeProvider as XTypeProvider_bbb40bef

class XServiceDocumenter(ABC):
    """
    provides documentation for UNO services
    
    **since**
    
        LibreOffice 5.1

    See Also:
        `API XServiceDocumenter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XServiceDocumenter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XServiceDocumenter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XServiceDocumenter'

    @abstractmethod
    def showCoreDocs(self, xService: 'XServiceInfo_af180b5f') -> None:
        """
        """
        ...
    @abstractmethod
    def showInterfaceDocs(self, xTypeProvider: 'XTypeProvider_bbb40bef') -> None:
        """
        """
        ...
    @abstractmethod
    def showServiceDocs(self, xService: 'XServiceInfo_af180b5f') -> None:
        """
        """
        ...
    @abstractproperty
    def CoreBaseUrl(self) -> str:
        """
        """
        ...

    @abstractproperty
    def ServiceBaseUrl(self) -> str:
        """
        """
        ...


__all__ = ['XServiceDocumenter']

