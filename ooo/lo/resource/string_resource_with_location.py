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
# Namespace: com.sun.star.resource
import typing
from abc import abstractmethod
from .x_string_resource_with_location import XStringResourceWithLocation as XStringResourceWithLocation_dd27135c
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class StringResourceWithLocation(XStringResourceWithLocation_dd27135c):
    """
    Service Class

    specifies a service providing access to a resource string table implementing the com.sun.star.resource.XStringResourceWithLocation interface.

    See Also:
        `API StringResourceWithLocation <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1resource_1_1StringResourceWithLocation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.resource'
    __ooo_full_ns__: str = 'com.sun.star.resource.StringResourceWithLocation'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self, URL: str, ReadOnly: bool, locale: 'Locale_70d308fa', BaseName: str, Comment: str, Handler: 'XInteractionHandler_bf80e51') -> None:
        """
        is used to initialize the object on its creation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['StringResourceWithLocation']

