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
# Namespace: com.sun.star.lang
# Libre Office Version: 7.2
from ..uno.exception import Exception as Exception_85530a09

class NullPointerException(Exception_85530a09):
    """
    This exception is thrown when an application attempts to use NULL in a case where an object is required.
    
    Applications should throw instances of this class to indicate other illegal uses of the NULL object.

    See Also:
        `API NullPointerException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1lang_1_1NullPointerException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.lang'
    __ooo_full_ns__: str = 'com.sun.star.lang.NullPointerException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.lang.NullPointerException'
    __pyunostruct__: str = 'com.sun.star.lang.NullPointerException'

    typeName: str = 'com.sun.star.lang.NullPointerException'
    """Literal Constant ``com.sun.star.lang.NullPointerException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)



