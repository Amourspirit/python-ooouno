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
# Namespace: com.sun.star.document
# Libre Office Version: 7.2
from ..uno.exception import Exception as Exception_85530a09

class ReadOnlyOpenRequest(Exception_85530a09):
    """
    Is used for interaction handle to query user decision regarding whether to open a document read-only and whether to notify the user when the document becomes editable.
    
    **since**
    
        LibreOffice 7.2

    See Also:
        `API ReadOnlyOpenRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1document_1_1ReadOnlyOpenRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.ReadOnlyOpenRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.document.ReadOnlyOpenRequest'
    __pyunostruct__: str = 'com.sun.star.document.ReadOnlyOpenRequest'

    typeName: str = 'com.sun.star.document.ReadOnlyOpenRequest'
    """Literal Constant ``com.sun.star.document.ReadOnlyOpenRequest``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)



