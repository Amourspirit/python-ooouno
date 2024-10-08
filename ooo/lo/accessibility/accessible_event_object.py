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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.accessibility
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class AccessibleEventObject(EventObject_a3d70b03):
    """
    Struct Class

    this struct describes an accessible event, that is broadcasted from the XAccessibleEventBroadcaster and notified to XAccessibleEventListener.
    
    It is usually implemented by AccessibleContext.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleEventObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1accessibility_1_1AccessibleEventObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.AccessibleEventObject'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.accessibility.AccessibleEventObject'
    """Literal Constant ``com.sun.star.accessibility.AccessibleEventObject``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, EventId: typing.Optional[int] = 0, NewValue: typing.Optional[object] = None, OldValue: typing.Optional[object] = None, IndexHint: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            EventId (int, optional): EventId value.
            NewValue (object, optional): NewValue value.
            OldValue (object, optional): OldValue value.
            IndexHint (int, optional): IndexHint value.
        """

        if isinstance(Source, AccessibleEventObject):
            oth: AccessibleEventObject = Source
            self.Source = oth.Source
            self.EventId = oth.EventId
            self.NewValue = oth.NewValue
            self.OldValue = oth.OldValue
            self.IndexHint = oth.IndexHint
            return

        kargs = {
            "Source": Source,
            "EventId": EventId,
            "NewValue": NewValue,
            "OldValue": OldValue,
            "IndexHint": IndexHint,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._event_id = kwargs["EventId"]
        self._new_value = kwargs["NewValue"]
        self._old_value = kwargs["OldValue"]
        self._index_hint = kwargs["IndexHint"]
        inst_keys = ('EventId', 'NewValue', 'OldValue', 'IndexHint')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def EventId(self) -> int:
        """
        specifies the type of this event.
        
        For a list of possible events see AccessibleEventId.
        """
        return self._event_id

    @EventId.setter
    def EventId(self, value: int) -> None:
        self._event_id = value

    @property
    def NewValue(self) -> object:
        """
        for events that specifies a value change, this is the new value.
        
        Depending on the EventId, this can be void.
        """
        return self._new_value

    @NewValue.setter
    def NewValue(self, value: object) -> None:
        self._new_value = value

    @property
    def OldValue(self) -> object:
        """
        for events that specifies a value change, this is the old value.
        
        Depending on the EventId, this can be void.
        """
        return self._old_value

    @OldValue.setter
    def OldValue(self, value: object) -> None:
        self._old_value = value

    @property
    def IndexHint(self) -> int:
        """
        For events like add/remove/update of a child, this specifies the index of the object.
        
        For anything else, it should be -1.
        
        **since**
        
            LibreOffice 7.6
        """
        return self._index_hint

    @IndexHint.setter
    def IndexHint(self, value: int) -> None:
        self._index_hint = value


__all__ = ['AccessibleEventObject']
