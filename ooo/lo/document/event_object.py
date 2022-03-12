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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.document
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class EventObject(EventObject_a3d70b03):
    """
    Struct Class

    is thrown on document and document content events
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API EventObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1EventObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.EventObject'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.document.EventObject'
    """Literal Constant ``com.sun.star.document.EventObject``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, EventName: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            EventName (str, optional): EventName value.
        """
        kargs = {
            "Source": Source,
            "EventName": EventName,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._event_name = kwargs["EventName"]
        inst_keys = ('EventName',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def EventName(self) -> str:
        """
        specifies the name of the occurred event
        
        For a list of possible event names see Events.
        """
        return self._event_name
    
    @EventName.setter
    def EventName(self, value: str) -> None:
        self._event_name = value


__all__ = ['EventObject']
