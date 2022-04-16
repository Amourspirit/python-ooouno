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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .x_content import XContent as XContent_79db0975
from .x_content_identifier import XContentIdentifier as XContentIdentifier_edc90d78


class ContentEvent(EventObject_a3d70b03):
    """
    Struct Class

    A structure for content events.

    See Also:
        `API ContentEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1ContentEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.ContentEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.ContentEvent'
    """Literal Constant ``com.sun.star.ucb.ContentEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Action: typing.Optional[int] = 0, Content: typing.Optional[XContent_79db0975] = None, Id: typing.Optional[XContentIdentifier_edc90d78] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Action (int, optional): Action value.
            Content (XContent, optional): Content value.
            Id (XContentIdentifier, optional): Id value.
        """

        if isinstance(Source, ContentEvent):
            oth: ContentEvent = Source
            self.Source = oth.Source
            self.Action = oth.Action
            self.Content = oth.Content
            self.Id = oth.Id
            return

        kargs = {
            "Source": Source,
            "Action": Action,
            "Content": Content,
            "Id": Id,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._action = kwargs["Action"]
        self._content = kwargs["Content"]
        self._id = kwargs["Id"]
        inst_keys = ('Action', 'Content', 'Id')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Action(self) -> int:
        """
        The action.
        
        The value can be one of the ContentAction constants.
        """
        return self._action
    
    @Action.setter
    def Action(self, value: int) -> None:
        self._action = value

    @property
    def Content(self) -> XContent_79db0975:
        """
        The content to that the action is related (e.g., the content that was just physically destroyed, the content that was just inserted into a folder content).
        
        This member must be filled as follows:
        """
        return self._content
    
    @Content.setter
    def Content(self, value: XContent_79db0975) -> None:
        self._content = value

    @property
    def Id(self) -> XContentIdentifier_edc90d78:
        """
        A content identifier, which must be filled according to the action notified (e.g., the id of the folder content into which another content was inserted).
        
        This member must be filled as follows:
        """
        return self._id
    
    @Id.setter
    def Id(self, value: XContentIdentifier_edc90d78) -> None:
        self._id = value


__all__ = ['ContentEvent']
