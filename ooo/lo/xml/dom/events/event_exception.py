# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.xml.dom.events
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ....uno.exception import Exception as Exception_85530a09
from ....uno.x_interface import XInterface as XInterface_8f010a43

class EventException(Exception_85530a09):
    """
    Exception Class


    See Also:
        `API EventException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1xml_1_1dom_1_1events_1_1EventException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.xml.dom.events'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.events.EventException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.xml.dom.events.EventException'
    __pyunostruct__: str = 'com.sun.star.xml.dom.events.EventException'

    typeName: str = 'com.sun.star.xml.dom.events.EventException'
    """Literal Constant ``com.sun.star.xml.dom.events.EventException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, code: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            code (int, optional): code value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "code": code,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._code = kwargs["code"]
        inst_keys = ('code',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def code(self) -> int:
        """
        """
        return self._code
    
    @code.setter
    def code(self, value: int) -> None:
        self._code = value


__all__ = ['EventException']

