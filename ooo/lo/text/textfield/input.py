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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text.textfield
from __future__ import annotations
from abc import abstractmethod
from ..text_field import TextField as TextField_90260a56

class Input(TextField_90260a56):
    """
    Service Class

    specifies service of a text input field.

    See Also:
        `API Input <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1Input.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text.textfield'
    __ooo_full_ns__: str = 'com.sun.star.text.textfield.Input'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def Content(self) -> str:
        """
        contains the text content of the text field.
        
        The field displays the text content.
        """
        ...

    @property
    @abstractmethod
    def Help(self) -> str:
        """
        contains an internal-use-only multi purpose string.
        
        This is an internal multi purpose string used in WW8 import/export. Usually it holds the help text for form fields.
        
        It's content must NEVER be modified by the user.
        """
        ...

    @property
    @abstractmethod
    def Hint(self) -> str:
        """
        contains a hint text.
        
        This hint may be used as help tip or as headline of a corresponding dialog to edit the field content.
        """
        ...


__all__ = ['Input']

