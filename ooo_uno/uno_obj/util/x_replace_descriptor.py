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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.util
from abc import abstractmethod
from .x_search_descriptor import XSearchDescriptor as XSearchDescriptor_ef600d93

class XReplaceDescriptor(XSearchDescriptor_ef600d93):
    """
    specifies a string replace operation.

    See Also:
        `API XReplaceDescriptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XReplaceDescriptor.html>`_
    """

    @abstractmethod
    def getReplaceString(self) -> str:
        """
        """
    @abstractmethod
    def setReplaceString(self, aReplaceString: str) -> None:
        """
        sets the string which replaces the found occurrences.
        """

__all__ = ['XReplaceDescriptor']

