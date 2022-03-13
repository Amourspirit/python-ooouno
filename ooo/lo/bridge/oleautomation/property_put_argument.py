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
# Namespace: com.sun.star.bridge.oleautomation
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class PropertyPutArgument(object):
    """
    Struct Class

    contains a value that is used as argument in a \"property put&quot operation on an Automation object.
    
    If an Automation object is converted into a UNO object by a scripting bridge, such as com.sun.star.bridge.oleautomation.BridgeSupplier, then it is accessed through the com.sun.star.script.XInvocation interface. The methods com.sun.star.script.XInvocation.setValue() and com.sun.star.script.XInvocation.getValue() are used to access properties which do not have additional arguments. To access a property with additional arguments, the method com.sun.star.script.XInvocation.invoke() has to be used. The method implementation must decide, if the property is to be written or read so it can perform the proper operation on the Automation object. To make this decision, the caller has to provide the information if the current call is intended to be a write or read operation. This is done by providing either instances of PropertyPutArgument or PropertyGetArgument as arguments to com.sun.star.script.XInvocation.Invoke.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API PropertyPutArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1PropertyPutArgument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge.oleautomation'
    __ooo_full_ns__: str = 'com.sun.star.bridge.oleautomation.PropertyPutArgument'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.bridge.oleautomation.PropertyPutArgument'
    """Literal Constant ``com.sun.star.bridge.oleautomation.PropertyPutArgument``"""

    def __init__(self, Value: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Value (object, optional): Value value.
        """
        super().__init__()

        if isinstance(Value, PropertyPutArgument):
            oth: PropertyPutArgument = Value
            self.Value = oth.Value
            return

        kargs = {
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._value = kwargs["Value"]


    @property
    def Value(self) -> object:
        """
        contains the actual argument.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value


__all__ = ['PropertyPutArgument']
