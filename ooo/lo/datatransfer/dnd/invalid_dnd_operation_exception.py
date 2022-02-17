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
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 7.2
from ...uno.runtime_exception import RuntimeException as RuntimeException_d7390ced

class InvalidDNDOperationException(RuntimeException_d7390ced):
    """
    This exception is thrown by various methods in the datatransfer.dnd package.
    
    It is usually thrown to indicate that the target in question is unable to undertake the requested operation at the present time, since the underlying Drag and Drop system is not in the appropriate state.

    See Also:
        `API InvalidDNDOperationException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1InvalidDNDOperationException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.InvalidDNDOperationException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.datatransfer.dnd.InvalidDNDOperationException'
    __pyunostruct__: str = 'com.sun.star.datatransfer.dnd.InvalidDNDOperationException'

    typeName: str = 'com.sun.star.datatransfer.dnd.InvalidDNDOperationException'
    """Literal Constant ``com.sun.star.datatransfer.dnd.InvalidDNDOperationException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)


