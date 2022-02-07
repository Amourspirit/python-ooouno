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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text.textfield
from abc import abstractproperty
from ..text_field import TextField as TextField_90260a56

class ExtendedUser(TextField_90260a56):
    """
    Service Class

    specifies service of a text field that shows and element of the user data (name, address, phone, ...)

    See Also:
        `API ExtendedUser <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1ExtendedUser.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text.textfield'
    __ooo_full_ns__: str = 'com.sun.star.text.textfield.ExtendedUser'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Content(self) -> str:
        """
        contains the content.
        """
    @abstractproperty
    def CurrentPresentation(self) -> str:
        """
        contains the current content of the text field.
        
        This property is especially useful for import/export purposes.
        """
    @abstractproperty
    def IsFixed(self) -> bool:
        """
        If this flag is set to FALSE the content is regularly updated.
        """
    @abstractproperty
    def UserDataType(self) -> int:
        """
        specifies which part of the user data is displayed as described in com.sun.star.text.UserDataPart.
        """

__all__ = ['ExtendedUser']

