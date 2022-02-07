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
# Namespace: com.sun.star.java
# Libre Office Version: 7.2
from .java_initialization_exception import JavaInitializationException as JavaInitializationException_8b6211a3

class MissingJavaRuntimeException(JavaInitializationException_8b6211a3):
    """
    indicates that the Java runtime library could not be found.
    
    This happens when a user moves or deletes a Java installation after the office has been configured to use that Java installation.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API MissingJavaRuntimeException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1java_1_1MissingJavaRuntimeException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.java'
    __ooo_full_ns__: str = 'com.sun.star.java.MissingJavaRuntimeException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.java.MissingJavaRuntimeException'
    __pyunostruct__: str = 'com.sun.star.java.MissingJavaRuntimeException'

    typeName: str = 'com.sun.star.java.MissingJavaRuntimeException'
    """Literal Constant ``com.sun.star.java.MissingJavaRuntimeException``"""

    URLRuntimeLib: str = None
    """
        contains the path to the runtime lib as file URL.
    """


