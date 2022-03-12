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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class Verb(object):
    """
    Struct Class

    describes a command that can be send to an OLE object
    
    For example, this can be used to select a font.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Verb <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1Verb.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.Verb'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.Verb'
    """Literal Constant ``com.sun.star.frame.status.Verb``"""

    def __init__(self, VerbId: typing.Optional[int] = 0, VerbName: typing.Optional[str] = '', VerbIsOnMenu: typing.Optional[bool] = False, VerbIsConst: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            VerbId (int, optional): VerbId value.
            VerbName (str, optional): VerbName value.
            VerbIsOnMenu (bool, optional): VerbIsOnMenu value.
            VerbIsConst (bool, optional): VerbIsConst value.
        """
        super().__init__()
        kargs = {
            "VerbId": VerbId,
            "VerbName": VerbName,
            "VerbIsOnMenu": VerbIsOnMenu,
            "VerbIsConst": VerbIsConst,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._verb_id = kwargs["VerbId"]
        self._verb_name = kwargs["VerbName"]
        self._verb_is_on_menu = kwargs["VerbIsOnMenu"]
        self._verb_is_const = kwargs["VerbIsConst"]


    @property
    def VerbId(self) -> int:
        """
        specifies the Id of the command.
        """
        return self._verb_id
    
    @VerbId.setter
    def VerbId(self, value: int) -> None:
        self._verb_id = value

    @property
    def VerbName(self) -> str:
        """
        specifies the name of the command.
        
        The name is localized.
        """
        return self._verb_name
    
    @VerbName.setter
    def VerbName(self, value: str) -> None:
        self._verb_name = value

    @property
    def VerbIsOnMenu(self) -> bool:
        """
        specifies if the command should be visible in a menu.
        """
        return self._verb_is_on_menu
    
    @VerbIsOnMenu.setter
    def VerbIsOnMenu(self, value: bool) -> None:
        self._verb_is_on_menu = value

    @property
    def VerbIsConst(self) -> bool:
        """
        specifies if the command is available for a constant object.
        """
        return self._verb_is_const
    
    @VerbIsConst.setter
    def VerbIsConst(self, value: bool) -> None:
        self._verb_is_const = value


__all__ = ['Verb']
