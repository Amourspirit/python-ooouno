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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_dispatch import XDispatch as XDispatch_98ff0a9b
    from .x_dispatch_recorder import XDispatchRecorder as XDispatchRecorder_fbd70dd1
    from ..util.url import URL as URL_57ad07b9

class XDispatchRecorderSupplier(XInterface_8f010a43):
    """
    provides access to the record mechanism of dispatches
    
    With a XDispatchRecorder it's possible to record calls of XDispatch.dispatch(). The recorded data (may a script) can be used to automate recorded dispatch and start it at later time again. This supplier provides access to the recorder and supports some functionality to work with the macro recording mechanism in an easy manner.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XDispatchRecorderSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDispatchRecorderSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XDispatchRecorderSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XDispatchRecorderSupplier'

    @abstractmethod
    def dispatchAndRecord(self, URL: 'URL_57ad07b9', Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]', Dispatcher: 'XDispatch_98ff0a9b') -> None:
        """
        dispatch given URL and record it if recording is enabled
        
        Parameter Dispatcher is used internally to make the dispatch. If recording isn't enabled it will be a normal XDispatch.dispatch() call. Otherwise follow algorithm is used:
        """
    @abstractmethod
    def getDispatchRecorder(self) -> 'XDispatchRecorder_fbd70dd1':
        """
        provides access on the recorder of this supplier
        
        Returned recorder can be used to record dispatches manually or to get recorded data for further using e.g. saving. He is internally used too due to the method XDispatchRecorderSupplier.dispatchAndRecord().
        """
    @abstractmethod
    def setDispatchRecorder(self, Recorder: 'XDispatchRecorder_fbd70dd1') -> None:
        """
        set a dispatch recorder on this supplier
        
        Setting of a new recorder make it possible to change recording mode. May there can exist different implementations of a recorder (e.g. to generate Java, Basic or other formats). Changing between local recording inside one Frame or global one by using more than ones can be forced too.
        """

__all__ = ['XDispatchRecorderSupplier']

