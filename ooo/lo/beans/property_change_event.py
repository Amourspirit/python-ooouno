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


class PropertyChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    gets delivered whenever a \"bound\" or \"constrained\" property is changed.
    
    A PropertyChangeEvent object is sent as an argument to the methods of XPropertyChangeListener and XVetoableChangeListener.
    
    Normally such events contain the name and the old and new value of the changed property.
    
    Void values may be provided for the old and new values if their true values are not known.

    See Also:
        `API PropertyChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyChangeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.PropertyChangeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.PropertyChangeEvent'
    """Literal Constant ``com.sun.star.beans.PropertyChangeEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``PropertyChangeEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``PropertyChangeEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            PropertyName (str, optional): PropertyName value
            Further (bool, optional): Further value
            PropertyHandle (int, optional): PropertyHandle value
            OldValue (object, optional): OldValue value
            NewValue (object, optional): NewValue value
        """
        self._property_name = None
        self._further = None
        self._property_handle = None
        self._old_value = None
        self._new_value = None

        key_order = ('PropertyName', 'Further', 'PropertyHandle', 'OldValue', 'NewValue')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], PropertyChangeEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("PropertyChangeEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def PropertyName(self) -> str:
        """
        contains the unique name of the property which changes its value.
        """
        return self._property_name
    
    @PropertyName.setter
    def PropertyName(self, value: str) -> None:
        self._property_name = value

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
    def OldValue(self) -> object:
        """
        contains the old value of the property.
        """
        return self._old_value
    
    @OldValue.setter
    def OldValue(self, value: object) -> None:
        self._old_value = value

    @property
    def NewValue(self) -> object:
        """
        contains the new value of the property.
        """
        return self._new_value
    
    @NewValue.setter
    def NewValue(self, value: object) -> None:
        self._new_value = value


__all__ = ['PropertyChangeEvent']
