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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.text
# Libre Office Version: 7.2
import typing
from abc import abstractproperty
from ..uno.exception import Exception as Exception_85530a09
if typing.TYPE_CHECKING:
    from .x_text_content import XTextContent as XTextContent_b16e0ba5

class InvalidTextContentException(Exception_85530a09):
    """
    is thrown whenever a method gets a TextContent as an actual argument when the text content cannot be used for that operation.

    See Also:
        `API InvalidTextContentException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1text_1_1InvalidTextContentException.html>`_
    """

    @abstractproperty
    def TextContent(self) -> 'XTextContent_b16e0ba5':
        """
        contains the interface of the text content that caused the exception.
        """

