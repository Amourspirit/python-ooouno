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
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class PropertyChangeEvent(EventObject_a3d70b03):
        """
        Struct Class

        gets delivered whenever a \"bound\" or \"constrained\" property is changed.
        
        A PropertyChangeEvent object is sent as an argument to the methods of XPropertyChangeListener and XVetoableChangeListener.
        
        Normally such events contain the name and the old and new value of the changed property.
        
        Void values may be provided for the old and new values if their true values are not known.

        See Also:
            `API PropertyChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyChangeEvent.html>`_


        Note:
            | At runtime PropertyChangeEvent will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | PropertyChangeEvent is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, Further: typing.Optional[bool] = None, NewValue: typing.Optional[object] = None, OldValue: typing.Optional[object] = None, PropertyHandle: typing.Optional[int] = None, PropertyName: typing.Optional[str] = None):
            self._further = Further
            self._new_value = NewValue
            self._old_value = OldValue
            self._property_handle = PropertyHandle
            self._property_name = PropertyName

        @property
        def Further(self) -> bool:
            """
            contains TRUE if further events in the same transaction occur.
            """
            return self._further
        
        @Further.setter
        def Further(self, value: bool) -> None:
            self._further = value

        @property
        def NewValue(self) -> object:
            """
            contains the new value of the property.
            """
            return self._new_value
        
        @NewValue.setter
        def NewValue(self, value: object) -> None:
            self._new_value = value

        @property
        def OldValue(self) -> object:
            """
            contains the old value of the property.
            """
            return self._old_value
        
        @OldValue.setter
        def OldValue(self, value: object) -> None:
            self._old_value = value

        @property
        def PropertyHandle(self) -> int:
            """
            contains the implementation handle for the property.
            
            May be -1 if the implementation has no handle. You can use this handle to get values from the XFastPropertySet.
            """
            return self._property_handle
        
        @PropertyHandle.setter
        def PropertyHandle(self, value: int) -> None:
            self._property_handle = value

        @property
        def PropertyName(self) -> str:
            """
            contains the unique name of the property which changes its value.
            """
            return self._property_name
        
        @PropertyName.setter
        def PropertyName(self, value: str) -> None:
            self._property_name = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global PropertyChangeEvent
        order = ('Further', 'NewValue', 'OldValue', 'PropertyHandle', 'PropertyName')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.beans.PropertyChangeEvent')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        PropertyChangeEvent = _struct_init

    _dynamic_struct()

__all__ = ['PropertyChangeEvent']
