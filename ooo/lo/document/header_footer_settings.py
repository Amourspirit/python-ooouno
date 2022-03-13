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
# Namespace: com.sun.star.document
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class HeaderFooterSettings(XPropertySet_bc180bfa):
    """
    Service Class

    describes properties that control the formatting of headers and footers for documents that do not allow individual settings for individual parts like pages or slides.

    See Also:
        `API HeaderFooterSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1HeaderFooterSettings.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.HeaderFooterSettings'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def IsPrintDate(self) -> bool:
        """
        enables or disables the printing of the date in the header or footer
        """

    @abstractproperty
    def IsPrintPageName(self) -> bool:
        """
        enables or disables the printing of the page name in the header or footer
        """

    @abstractproperty
    def IsPrintTime(self) -> bool:
        """
        enables or disables the printing of the current time in the header or footer
        """



__all__ = ['HeaderFooterSettings']

