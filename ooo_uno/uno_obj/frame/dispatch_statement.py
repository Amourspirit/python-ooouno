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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
import typing
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class DispatchStatement(object):
        """
        Struct Class

        represents a dispatch statement from a recorded macro
        
        **since**
        
            OOo 1.1.2

        See Also:
            `API DispatchStatement <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1DispatchStatement.html>`_


        Note:
            | At runtime DispatchStatement will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | DispatchStatement is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, aArgs: 'typing.Optional[typing.List[PropertyValue_c9610c73]]' = None, aCommand: typing.Optional[str] = None, aTarget: typing.Optional[str] = None, bIsComment: typing.Optional[bool] = None, nFlags: typing.Optional[int] = None):
            self._a_args = aArgs
            self._a_command = aCommand
            self._a_target = aTarget
            self._b_is_comment = bIsComment
            self._n_flags = nFlags

        @property
        def aArgs(self) -> 'typing.List[PropertyValue_c9610c73]':
            """
            specifies the dispatch command arguments
            
            That means the Arguments parameter of a corresponding XDispatch.dispatch() request.
            """
            return self._a_args
        
        @aArgs.setter
        def aArgs(self, value: 'typing.List[PropertyValue_c9610c73]') -> None:
            self._a_args = value

        @property
        def aCommand(self) -> str:
            """
            specifies the dispatch command
            
            That means the URL parameter of a corresponding XDispatchProvider.queryDispatch() request.
            """
            return self._a_command
        
        @aCommand.setter
        def aCommand(self, value: str) -> None:
            self._a_command = value

        @property
        def aTarget(self) -> str:
            """
            specifies the frame target
            
            That means the TargetFrameName parameter of a corresponding XDispatchProvider.queryDispatch() request.
            """
            return self._a_target
        
        @aTarget.setter
        def aTarget(self, value: str) -> None:
            self._a_target = value

        @property
        def bIsComment(self) -> bool:
            """
            specifies if this statement should be recorded as commented out or not
            """
            return self._b_is_comment
        
        @bIsComment.setter
        def bIsComment(self, value: bool) -> None:
            self._b_is_comment = value

        @property
        def nFlags(self) -> int:
            """
            specifies the optional search flags
            
            That means the SearchFlags parameter of a corresponding XDispatchProvider.queryDispatch() request.
            """
            return self._n_flags
        
        @nFlags.setter
        def nFlags(self, value: int) -> None:
            self._n_flags = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global DispatchStatement
        order = ('aArgs', 'aCommand', 'aTarget', 'bIsComment', 'nFlags')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.frame.DispatchStatement')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        DispatchStatement = _struct_init

    _dynamic_struct()

__all__ = ['DispatchStatement']
