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
# Namespace: com.sun.star.uno
# Libre Office Version: 7.2
from .exception import Exception as Exception_85530a09

class RuntimeException(Exception_85530a09):
    """
    This exception or a subclass can occur at every interface method.
    
    It shall signal an error, which was not covered by the interface method specification. This exception (or a derived one) is thrown, when for instance an interprocess bridge to the object broke down, some explicitly forbidden invalid parameters were passed ( e.g. null references ) or the called object has been disposed before.

    See Also:
        `API RuntimeException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1uno_1_1RuntimeException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.RuntimeException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.uno.RuntimeException'
    __pyunostruct__: str = 'com.sun.star.uno.RuntimeException'

    typeName: str = 'com.sun.star.uno.RuntimeException'
    """Literal Constant ``com.sun.star.uno.RuntimeException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)


