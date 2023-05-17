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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.form.FormSubmitMethod import GET as FORM_SUBMIT_METHOD_GET
    from com.sun.star.form.FormSubmitMethod import POST as FORM_SUBMIT_METHOD_POST

    class FormSubmitMethod(uno.Enum):
        """
        Enum Class


        See Also:
            `API FormSubmitMethod <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#ae9bf553104504664f5d2066375a414df>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.form.FormSubmitMethod', value)

        __ooo_ns__: str = 'com.sun.star.form'
        __ooo_full_ns__: str = 'com.sun.star.form.FormSubmitMethod'
        __ooo_type_name__: str = 'enum'

        GET = cast("FormSubmitMethod", FORM_SUBMIT_METHOD_GET)
        """
        specifies to append the input information of a form to the target URL as parameters.
        """
        POST = cast("FormSubmitMethod", FORM_SUBMIT_METHOD_POST)
        """
        specifies to send the input information in a data body.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class FormSubmitMethod(metaclass=UnoEnumMeta, type_name="com.sun.star.form.FormSubmitMethod", name_space="com.sun.star.form"):
        """Dynamically created class that represents ``com.sun.star.form.FormSubmitMethod`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['FormSubmitMethod']
