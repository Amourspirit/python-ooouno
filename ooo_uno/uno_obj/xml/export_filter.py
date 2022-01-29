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
# Namespace: com.sun.star.xml
from .x_export_filter import XExportFilter as XExportFilter_b0c20b99
from .sax.x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28

class ExportFilter(XExportFilter_b0c20b99, XDocumentHandler_9b90e28):
    """
    describes an export filter for XML-based file formats.
    
    First, the XExportFilter.exporter() method must be called to provide the export component with the target location to which the data should be exported. Then, the source document's XML representation will be generated by calling the appropriate methods of the com.sun.star.xml.sax.XDocumentHandler interface. Error conditions must be signaled by throwing a com.sun.star.xml.sax.SAXException in the com.sun.star.xml.sax.XDocumentHandler calls.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ExportFilter <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xml_1_1ExportFilter.html>`_
    """


__all__ = ['ExportFilter']

