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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_all_listener import XAllListener as XAllListener_c91b0c54

class XAllListenerAdapterService(XInterface_8f010a43):
    """
    allows the generation of adapters from specific interfaces to the XAllListener interface.

    See Also:
        `API XAllListenerAdapterService <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XAllListenerAdapterService.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.XAllListenerAdapterService'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.script.XAllListenerAdapterService'

    @abstractmethod
    def createAllListerAdapter(self, xListenerType: object, xListener: 'XAllListener_c91b0c54', aHelper: object) -> 'XInterface_8f010a43':
        """
        creates a wrapper from the listener of type xListenerType to the XAllListener listener.
        
        To get the correct listener interface the returned com.sun.star.uno.XInterface has to be queried for it.
        """

__all__ = ['XAllListenerAdapterService']
