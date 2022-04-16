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
# Namespace: com.sun.star.beans
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .property_state import PropertyState as PropertyState_c97b0c77


class PropertyStateChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    is delivered whenever the state of a \"bound\" property is changed.
    
    It is sent as an argument to the method of XPropertyStateChangeListener.
    
    Normally these events are accompanied by the name, and the old and new values of the changed property.
    
    Void values may be provided for the old and new values if their true values are not known.

    See Also:
        `API PropertyStateChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyStateChangeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.PropertyStateChangeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.PropertyStateChangeEvent'
    """Literal Constant ``com.sun.star.beans.PropertyStateChangeEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, PropertyName: typing.Optional[str] = '', PropertyHandle: typing.Optional[int] = 0, OldValue: typing.Optional[PropertyState_c97b0c77] = PropertyState_c97b0c77.DIRECT_VALUE, NewValue: typing.Optional[PropertyState_c97b0c77] = PropertyState_c97b0c77.DIRECT_VALUE) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            PropertyName (str, optional): PropertyName value.
            PropertyHandle (int, optional): PropertyHandle value.
            OldValue (PropertyState, optional): OldValue value.
            NewValue (PropertyState, optional): NewValue value.
        """

        if isinstance(Source, PropertyStateChangeEvent):
            oth: PropertyStateChangeEvent = Source
            self.Source = oth.Source
            self.PropertyName = oth.PropertyName
            self.PropertyHandle = oth.PropertyHandle
            self.OldValue = oth.OldValue
            self.NewValue = oth.NewValue
            return

        kargs = {
            "Source": Source,
            "PropertyName": PropertyName,
            "PropertyHandle": PropertyHandle,
            "OldValue": OldValue,
            "NewValue": NewValue,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._property_name = kwargs["PropertyName"]
        self._property_handle = kwargs["PropertyHandle"]
        self._old_value = kwargs["OldValue"]
        self._new_value = kwargs["NewValue"]
        inst_keys = ('PropertyName', 'PropertyHandle', 'OldValue', 'NewValue')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def PropertyName(self) -> str:
        """
        specifies the name of the property which changes its value.
        
        This name identifies the property uniquely within an XPropertySet. Upper and lower case are distinguished.
        """
        return self._property_name
    
    @PropertyName.setter
    def PropertyName(self, value: str) -> None:
        self._property_name = value

    @property
    def PropertyHandle(self) -> int:
        """
        contains the implementation handle for the property.
        
        It may be -1 if the implementation has no handle. You can use this handle to get values from the XFastPropertySet interface.
        """
        return self._property_handle
    
    @PropertyHandle.setter
    def PropertyHandle(self, value: int) -> None:
        self._property_handle = value

    @property
    def OldValue(self) -> PropertyState_c97b0c77:
        """
        contains the old value of the property.
        """
        return self._old_value
    
    @OldValue.setter
    def OldValue(self, value: PropertyState_c97b0c77) -> None:
        self._old_value = value

    @property
    def NewValue(self) -> PropertyState_c97b0c77:
        """
        contains the new value of the property.
        """
        return self._new_value
    
    @NewValue.setter
    def NewValue(self, value: PropertyState_c97b0c77) -> None:
        self._new_value = value


__all__ = ['PropertyStateChangeEvent']
