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
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_filter import XFilter as XFilter_a6300b25
from .x_importer import XImporter as XImporter_be230c11
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca

class ImportFilter(XNamed_a6520b08, XFilter_a6300b25, XImporter_be230c11, XInitialization_d46c0cca):
    """
    Service Class

    filter for imports
    
    Such filters can be used for importing a content. Of course it's possible to combine it with the service ExportFilter if export functionality should be available at same implementation too.

    See Also:
        `API ImportFilter <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1ImportFilter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.ImportFilter'
    __ooo_type_name__: str = 'service'



__all__ = ['ImportFilter']

