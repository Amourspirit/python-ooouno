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

class JavaVMCreationFailureException(JavaInitializationException_8b6211a3):
    """
    indicates that the Java Virtual Machine could not be created
    
    This exception can be thrown when the creation of the Java Virtual Machine failed, even if the runtime library could be loaded. Possible reasons for a failure are that JNI_CreateJavaVM returns an error code that reflects a failure, JNI_CreateJavaVM does not return because it tries to quit the process ( _exit), the shared library is corrupted, so that the symbols for JNI_GetDefaultVMInitArgs or JNI_CreateJavaVM cannot be found, etc.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API JavaVMCreationFailureException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1java_1_1JavaVMCreationFailureException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.java'
    __ooo_full_ns__: str = 'com.sun.star.java.JavaVMCreationFailureException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.java.JavaVMCreationFailureException'
    __pyunostruct__: str = 'com.sun.star.java.JavaVMCreationFailureException'

    typeName: str = 'com.sun.star.java.JavaVMCreationFailureException'
    """Literal Constant ``com.sun.star.java.JavaVMCreationFailureException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)


