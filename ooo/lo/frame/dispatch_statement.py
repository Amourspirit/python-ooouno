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
from ooo.oenv import UNO_NONE
import typing
from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class DispatchStatement(object):
    """
    Struct Class

    represents a dispatch statement from a recorded macro
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DispatchStatement <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1DispatchStatement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.DispatchStatement'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.DispatchStatement'
    """Literal Constant ``com.sun.star.frame.DispatchStatement``"""

    def __init__(self, aArgs: typing.Optional[typing.Tuple[PropertyValue_c9610c73, ...]] = UNO_NONE, aCommand: typing.Optional[str] = '', aTarget: typing.Optional[str] = '', nFlags: typing.Optional[int] = 0, bIsComment: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            aArgs (typing.Tuple[PropertyValue, ...], optional): aArgs value.
            aCommand (str, optional): aCommand value.
            aTarget (str, optional): aTarget value.
            nFlags (int, optional): nFlags value.
            bIsComment (bool, optional): bIsComment value.
        """
        super().__init__()
        kargs = {
            "aArgs": aArgs,
            "aCommand": aCommand,
            "aTarget": aTarget,
            "nFlags": nFlags,
            "bIsComment": bIsComment,
        }
        if kargs["aArgs"] is UNO_NONE:
            kargs["aArgs"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._a_args = kwargs["aArgs"]
        self._a_command = kwargs["aCommand"]
        self._a_target = kwargs["aTarget"]
        self._n_flags = kwargs["nFlags"]
        self._b_is_comment = kwargs["bIsComment"]


    @property
    def aArgs(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        specifies the dispatch command arguments
        
        That means the Arguments parameter of a corresponding XDispatch.dispatch() request.
        """
        return self._a_args
    
    @aArgs.setter
    def aArgs(self, value: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
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
    def nFlags(self) -> int:
        """
        specifies the optional search flags
        
        That means the SearchFlags parameter of a corresponding XDispatchProvider.queryDispatch() request.
        """
        return self._n_flags
    
    @nFlags.setter
    def nFlags(self, value: int) -> None:
        self._n_flags = value

    @property
    def bIsComment(self) -> bool:
        """
        specifies if this statement should be recorded as commented out or not
        """
        return self._b_is_comment
    
    @bIsComment.setter
    def bIsComment(self, value: bool) -> None:
        self._b_is_comment = value


__all__ = ['DispatchStatement']
