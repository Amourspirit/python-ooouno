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
# Namespace: com.sun.star.text.textfield.docinfo
from abc import abstractproperty
from ...text_field import TextField as TextField_90260a56

class Custom(TextField_90260a56):
    """
    specifies service of a text field that refers to the content of a user-defined field in the document information.
    
    **since**
    
        OOo 3.0

    See Also:
        `API Custom <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1docinfo_1_1Custom.html>`_
    """

    @abstractproperty
    def CurrentPresentation(self) -> str:
        """
        contains the current content of the text field.
        
        This property is useful for import/export purposes.
        """
    @abstractproperty
    def IsFixed(self) -> bool:
        """
        If this flag is set to FALSE, the content is updated when the document information changes.
        """
    @abstractproperty
    def Name(self) -> str:
        """
        the name of the user-defined property that this field refers to.
        """

__all__ = ['Custom']

