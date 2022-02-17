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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.2
from enum import Enum


class FormSubmitMethod(Enum):
    """
    Enum Class

    

    See Also:
        `API FormSubmitMethod <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#ae9bf553104504664f5d2066375a414df>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.FormSubmitMethod'
    __ooo_type_name__: str = 'enum'

    GET = 'GET'
    """
    specifies to append the input information of a form to the target URL as parameters.
    """
    POST = 'POST'
    """
    specifies to send the input information in a data body.
    """

__all__ = ['FormSubmitMethod']
