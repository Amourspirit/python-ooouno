# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.document
from __future__ import annotations
from .x_extended_filter_detection import XExtendedFilterDetection as XExtendedFilterDetection_9ff211f5

class ExtendedTypeDetection(XExtendedFilterDetection_9ff211f5):
    """
    Service Class

    describes a class of service which will be used for deep TypeDetection in a generic way
    
    Due to the registered types, flat TypeDetection is already possible, i.e. the assignment of types (e.g. to a URL) only on the basis of configuration data. If, however, you imagine special cases (e.g. modifying the file extension of a Writer file from .sdw to .doc), it quickly becomes clear that you cannot always get a correct result with flat detection. To be certain to get correct results, you need deep detection, i.e. the file itself has to be examined. And that is exactly the function of DetectServices. They get all the information collected so far on a document and then decide which type to assign it to. In the new modular model, such a detector is meant as UNO service which registers itself in the office and is requested by the generic type detection if necessary. Therefore you need two pieces of information:
    
    See service TypeDetection and his configuration for further information.

    See Also:
        `API ExtendedTypeDetection <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1ExtendedTypeDetection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.ExtendedTypeDetection'
    __ooo_type_name__: str = 'service'


__all__ = ['ExtendedTypeDetection']

