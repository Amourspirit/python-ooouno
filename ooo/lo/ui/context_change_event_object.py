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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ui
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ContextChangeEventObject(EventObject_a3d70b03):
    """
    Struct Class


    See Also:
        `API ContextChangeEventObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1ContextChangeEventObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.ContextChangeEventObject'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ui.ContextChangeEventObject'
    """Literal Constant ``com.sun.star.ui.ContextChangeEventObject``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, ApplicationName: typing.Optional[str] = '', ContextName: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            ApplicationName (str, optional): ApplicationName value.
            ContextName (str, optional): ContextName value.
        """

        if isinstance(Source, ContextChangeEventObject):
            oth: ContextChangeEventObject = Source
            self.Source = oth.Source
            self.ApplicationName = oth.ApplicationName
            self.ContextName = oth.ContextName
            return

        kargs = {
            "Source": Source,
            "ApplicationName": ApplicationName,
            "ContextName": ContextName,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._application_name = kwargs["ApplicationName"]
        self._context_name = kwargs["ContextName"]
        inst_keys = ('ApplicationName', 'ContextName')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def ApplicationName(self) -> str:
        """
        Return the name of the application.
        """
        return self._application_name

    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None:
        self._application_name = value

    @property
    def ContextName(self) -> str:
        """
        Return the application specific context name.
        """
        return self._context_name

    @ContextName.setter
    def ContextName(self, value: str) -> None:
        self._context_name = value


__all__ = ['ContextChangeEventObject']
