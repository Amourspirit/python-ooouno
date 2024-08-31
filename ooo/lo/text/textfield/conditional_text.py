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

class ConditionalText(TextField_90260a56):
    """
    Service Class

    specifies service of a conditional text field.

    See Also:
        `API ConditionalText <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1ConditionalText.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text.textfield'
    __ooo_full_ns__: str = 'com.sun.star.text.textfield.ConditionalText'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def Condition(self) -> str:
        """
        contains the condition.
        """
        ...

    @property
    @abstractmethod
    def CurrentPresentation(self) -> str:
        """
        contains the current content of the text field.
        
        This property is especially useful for import/export purposes.
        """
        ...

    @property
    @abstractmethod
    def FalseContent(self) -> str:
        """
        contains the text that is displayed if the condition evaluates to FALSE.
        """
        ...

    @property
    @abstractmethod
    def IsConditionTrue(self) -> bool:
        """
        contains the result of the last evaluation of the condition.
        
        This property has to be read/written in file export/import to save and restore the result without initiation of a new evaluation.
        """
        ...

    @property
    @abstractmethod
    def TrueContent(self) -> str:
        """
        contains the text that is displayed if the condition evaluates to TRUE.
        """
        ...


__all__ = ['ConditionalText']

