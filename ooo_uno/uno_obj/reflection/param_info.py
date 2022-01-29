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
# Namespace: com.sun.star.reflection
# Libre Office Version: 7.2
import os
import typing
if typing.TYPE_CHECKING:
    from .param_mode import ParamMode as ParamMode_d7260ca9
    from .x_idl_class import XIdlClass as XIdlClass_d63a0c9a
from ooo_uno.oenv import UNO_ENVIRONMENT
if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class ParamInfo(object):
    """
    Struct Class

    Provides information about a formal parameter of a method.

    See Also:
        `API ParamInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1reflection_1_1ParamInfo.html>`_


    Note:
        | At runtime ParamInfo will be an actual uno struct however can seamlessly be treated as a regualr class.
        | At design time a class is presumed. This allows for better typings.
        | ParamInfo is a callable and can be treatead as a class and create instances.
    """

    def __init__(self, aMode: 'typing.Optional[ParamMode_d7260ca9]' = None, aName: typing.Optional[str] = None, aType: 'typing.Optional[XIdlClass_d63a0c9a]' = None):
        self._a_mode = aMode
        self._a_name = aName
        self._a_type = aType

    @property
    def aMode(self) -> 'ParamMode_d7260ca9':
        """
        parameter mode: in, out, inout
        """
        return self._a_mode
    
    @aMode.setter
    def aMode(self, value: 'ParamMode_d7260ca9') -> None:
        self._a_mode = value

    @property
    def aName(self) -> str:
        """
        name of the parameter
        """
        return self._a_name
    
    @aName.setter
    def aName(self, value: str) -> None:
        self._a_name = value

    @property
    def aType(self) -> 'XIdlClass_d63a0c9a':
        """
        formal type of the parameter
        """
        return self._a_type
    
    @aType.setter
    def aType(self, value: 'XIdlClass_d63a0c9a') -> None:
        self._a_type = value

def _dynamic_struct() -> None:
    # Dynamically create uno struct using uno
    global ParamInfo
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('aMode', 'aName', 'aType')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.reflection.ParamInfo')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ParamInfo = _struct_init

if (not typing.TYPE_CHECKING) and UNO_ENVIRONMENT:
    _dynamic_struct()

__all__ = ['ParamInfo']
