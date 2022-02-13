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
# Namespace: com.sun.star.packages.zip
# Libre Office Version: 7.2
from ...uno.exception import Exception as Exception_85530a09

class ZipException(Exception_85530a09):
    """
    used to indicate that a ZIP exception has occurred.
    
    This interface is an IDL version of the Java interface java.util.zip.ZipException with some minor adaptations.

    See Also:
        `API ZipException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1packages_1_1zip_1_1ZipException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.packages.zip'
    __ooo_full_ns__: str = 'com.sun.star.packages.zip.ZipException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.packages.zip.ZipException'
    __pyunostruct__: str = 'com.sun.star.packages.zip.ZipException'

    typeName: str = 'com.sun.star.packages.zip.ZipException'
    """Literal Constant ``com.sun.star.packages.zip.ZipException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)



