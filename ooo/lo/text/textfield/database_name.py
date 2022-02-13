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
from ..dependent_text_field import DependentTextField as DependentTextField_fed90ded

class DatabaseName(DependentTextField_fed90ded):
    """
    Service Class

    specifies service of text field that displays the name of a database.
    
    Only one of the properties DataBaseName, DataBaseURL and DataBaseResource should be set. If more than one are set the last one will be used.
    
    **since**
    
        OOo 2.0

    See Also:
        `API DatabaseName <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1DatabaseName.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text.textfield'
    __ooo_full_ns__: str = 'com.sun.star.text.textfield.DatabaseName'
    __ooo_type_name__: str = 'service'



__all__ = ['DatabaseName']

