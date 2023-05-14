# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.text.textfield
from abc import abstractproperty
from ..text_field import TextField as TextField_90260a56

class TemplateName(TextField_90260a56):
    """
    Service Class

    specifies service text field that displays the name of the template the document has been created from.

    See Also:
        `API TemplateName <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1TemplateName.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text.textfield'
    __ooo_full_ns__: str = 'com.sun.star.text.textfield.TemplateName'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def FileFormat(self) -> int:
        """
        determines the format the template file name is displayed as specified in com.sun.star.text.FilenameDisplayFormat.
        """
        ...


__all__ = ['TemplateName']

