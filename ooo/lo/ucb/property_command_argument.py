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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..beans.property import Property as Property_8f4e0a76


class PropertyCommandArgument(object):
    """
    Struct Class

    The argument for the \"addProperty\" command.
    
    **since**
    
        Apache OpenOffice 4.0, LibreOffice 4.2

    See Also:
        `API PropertyCommandArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1PropertyCommandArgument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.PropertyCommandArgument'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.PropertyCommandArgument'
    """Literal Constant ``com.sun.star.ucb.PropertyCommandArgument``"""

    def __init__(self, Property: typing.Optional[Property_8f4e0a76] = UNO_NONE, DefaultValue: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Property (Property, optional): Property value.
            DefaultValue (object, optional): DefaultValue value.
        """
        super().__init__()

        if isinstance(Property, PropertyCommandArgument):
            oth: PropertyCommandArgument = Property
            self.Property = oth.Property
            self.DefaultValue = oth.DefaultValue
            return

        kargs = {
            "Property": Property,
            "DefaultValue": DefaultValue,
        }
        if kargs["Property"] is UNO_NONE:
            kargs["Property"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._property = kwargs["Property"]
        self._default_value = kwargs["DefaultValue"]


    @property
    def Property(self) -> Property_8f4e0a76:
        """
        The property that the command has to add.
        """
        return self._property
    
    @Property.setter
    def Property(self, value: Property_8f4e0a76) -> None:
        self._property = value

    @property
    def DefaultValue(self) -> object:
        """
        The default value of the property.
        """
        return self._default_value
    
    @DefaultValue.setter
    def DefaultValue(self, value: object) -> None:
        self._default_value = value


__all__ = ['PropertyCommandArgument']
