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
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class TemplateIdentifier(object):
    """
    Struct Class

    holds the data needed to identify a template.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TemplateIdentifier <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1configuration_1_1backend_1_1TemplateIdentifier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.TemplateIdentifier'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.configuration.backend.TemplateIdentifier'
    """Literal Constant ``com.sun.star.configuration.backend.TemplateIdentifier``"""

    def __init__(self, Name: typing.Optional[str] = '', Component: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Component (str, optional): Component value.
        """
        super().__init__()

        if isinstance(Name, TemplateIdentifier):
            oth: TemplateIdentifier = Name
            self.Name = oth.Name
            self.Component = oth.Component
            return

        kargs = {
            "Name": Name,
            "Component": Component,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._component = kwargs["Component"]


    @property
    def Name(self) -> str:
        """
        specifies the name of the template.
        
        The name is unique within a component.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Component(self) -> str:
        """
        specifies the component where the template originates.
        """
        return self._component

    @Component.setter
    def Component(self, value: str) -> None:
        self._component = value


__all__ = ['TemplateIdentifier']
