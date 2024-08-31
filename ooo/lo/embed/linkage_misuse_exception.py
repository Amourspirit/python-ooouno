# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.embed
# Libre Office Version: 2024.2
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class LinkageMisuseException(Exception_85530a09):
    """
    Exception Class

    This exception can be thrown in case a linked object is misused.
    
    Or if embedded object is misused as a linked object.

    See Also:
        `API LinkageMisuseException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1embed_1_1LinkageMisuseException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.LinkageMisuseException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.embed.LinkageMisuseException'
    __pyunostruct__: str = 'com.sun.star.embed.LinkageMisuseException'

    typeName: str = 'com.sun.star.embed.LinkageMisuseException'
    """Literal Constant ``com.sun.star.embed.LinkageMisuseException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        super()._init(**kwargs)


__all__ = ['LinkageMisuseException']

