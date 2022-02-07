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
# Namespace: com.sun.star.task
# Libre Office Version: 7.2
from .password_request import PasswordRequest as PasswordRequest_d7280cf7

class DocumentPasswordRequest(PasswordRequest_d7280cf7):
    """
    this request specifies the mode in which the password should be asked
    
    It is supported by InteractionHandler service, and can be used to interact for a document password. Continuations for using with the mentioned service are Abort and Approve.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DocumentPasswordRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1DocumentPasswordRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.DocumentPasswordRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.task.DocumentPasswordRequest'
    __pyunostruct__: str = 'com.sun.star.task.DocumentPasswordRequest'

    typeName: str = 'com.sun.star.task.DocumentPasswordRequest'
    """Literal Constant ``com.sun.star.task.DocumentPasswordRequest``"""

    Name: str = None
    """
        the name of the document (more properly, the URL of the document)
    """


