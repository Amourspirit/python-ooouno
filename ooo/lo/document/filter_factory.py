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
# Libre Office Version: 7.3
# Namespace: com.sun.star.document
from ..container.x_container_query import XContainerQuery as XContainerQuery_1cdd0edc
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
from ..util.x_flushable import XFlushable as XFlushable_9a420ab4

class FilterFactory(XContainerQuery_1cdd0edc, XNameContainer_cb90e47, XMultiServiceFactory_191e0eb6, XFlushable_9a420ab4):
    """
    Service Class

    factory to create filter components.
    
    After a generic TypeDetection an internal type name will be known. Further a generic com.sun.star.frame.FrameLoader can use this information, to search a suitable filter (may the default filter) at this factory and use it for loading the document into a specified frame.
    
    This factory implements read/write access on the underlying configuration set. and further a validate and flush mechanism for more performance and a special query mode can be used here too.

    See Also:
        `API FilterFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1FilterFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.FilterFactory'
    __ooo_type_name__: str = 'service'



__all__ = ['FilterFactory']

