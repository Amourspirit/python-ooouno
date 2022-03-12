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
import typing


class CmisProperty(object):
    """
    Struct Class

    specifies a CMIS property.

    See Also:
        `API CmisProperty <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1CmisProperty.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.CmisProperty'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.document.CmisProperty'
    """Literal Constant ``com.sun.star.document.CmisProperty``"""

    def __init__(self, Id: typing.Optional[str] = '', Name: typing.Optional[str] = '', Type: typing.Optional[str] = '', Updatable: typing.Optional[bool] = False, Required: typing.Optional[bool] = False, MultiValued: typing.Optional[bool] = False, OpenChoice: typing.Optional[bool] = False, Choices: typing.Optional[object] = None, Value: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Id (str, optional): Id value.
            Name (str, optional): Name value.
            Type (str, optional): Type value.
            Updatable (bool, optional): Updatable value.
            Required (bool, optional): Required value.
            MultiValued (bool, optional): MultiValued value.
            OpenChoice (bool, optional): OpenChoice value.
            Choices (object, optional): Choices value.
            Value (object, optional): Value value.
        """
        super().__init__()
        kargs = {
            "Id": Id,
            "Name": Name,
            "Type": Type,
            "Updatable": Updatable,
            "Required": Required,
            "MultiValued": MultiValued,
            "OpenChoice": OpenChoice,
            "Choices": Choices,
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._id = kwargs["Id"]
        self._name = kwargs["Name"]
        self._type = kwargs["Type"]
        self._updatable = kwargs["Updatable"]
        self._required = kwargs["Required"]
        self._multi_valued = kwargs["MultiValued"]
        self._open_choice = kwargs["OpenChoice"]
        self._choices = kwargs["Choices"]
        self._value = kwargs["Value"]


    @property
    def Id(self) -> str:
        """
        unique ID of the Cmis property
        """
        return self._id
    
    @Id.setter
    def Id(self, value: str) -> None:
        self._id = value

    @property
    def Name(self) -> str:
        """
        specifies the display name of the CMIS property.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Type(self) -> str:
        """
        type of the property
        """
        return self._type
    
    @Type.setter
    def Type(self, value: str) -> None:
        self._type = value

    @property
    def Updatable(self) -> bool:
        """
        specifies if the property is updatable.
        """
        return self._updatable
    
    @Updatable.setter
    def Updatable(self, value: bool) -> None:
        self._updatable = value

    @property
    def Required(self) -> bool:
        """
        specifies if the property is required and can not be empty.
        """
        return self._required
    
    @Required.setter
    def Required(self, value: bool) -> None:
        self._required = value

    @property
    def MultiValued(self) -> bool:
        """
        specifies if the property has multiple value
        """
        return self._multi_valued
    
    @MultiValued.setter
    def MultiValued(self, value: bool) -> None:
        self._multi_valued = value

    @property
    def OpenChoice(self) -> bool:
        """
        specifies if the property value can be freely set or is restricted from a list of choices.
        """
        return self._open_choice
    
    @OpenChoice.setter
    def OpenChoice(self, value: bool) -> None:
        self._open_choice = value

    @property
    def Choices(self) -> object:
        """
        specifies the possible choices of the values.
        """
        return self._choices
    
    @Choices.setter
    def Choices(self, value: object) -> None:
        self._choices = value

    @property
    def Value(self) -> object:
        """
        specifies value of the property
        """
        return self._value
    
    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value


__all__ = ['CmisProperty']
