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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ResultEvent(EventObject_a3d70b03):
    """
    Struct Class

    contains the new value of a volatile function result.

    See Also:
        `API ResultEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1ResultEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.ResultEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.ResultEvent'
    """Literal Constant ``com.sun.star.sheet.ResultEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Value: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Value (object, optional): Value value.
        """
        kargs = {
            "Source": Source,
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._value = kwargs["Value"]
        inst_keys = ('Value',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Value(self) -> object:
        """
        contains the value.
        
        This can be any of the possible return types described for the AddIn service, except XVolatileResult.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value


__all__ = ['ResultEvent']
