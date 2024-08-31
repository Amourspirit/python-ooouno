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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.document
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from ..frame.x_controller2 import XController2 as XController2_bbcf0bc1


class DocumentEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes an event happening in an OfficeDocument
    
    The com.sun.star.lang.EventObject.Source member of the base type refers to the document which broadcasts the event.
    
    This type is the successor of the EventObject type, which should not be used anymore.
    
    **since**
    
        OOo 3.1

    See Also:
        `API DocumentEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1DocumentEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.DocumentEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.document.DocumentEvent'
    """Literal Constant ``com.sun.star.document.DocumentEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, EventName: typing.Optional[str] = '', ViewController: typing.Optional[XController2_bbcf0bc1] = None, Supplement: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            EventName (str, optional): EventName value.
            ViewController (XController2, optional): ViewController value.
            Supplement (object, optional): Supplement value.
        """

        if isinstance(Source, DocumentEvent):
            oth: DocumentEvent = Source
            self.Source = oth.Source
            self.EventName = oth.EventName
            self.ViewController = oth.ViewController
            self.Supplement = oth.Supplement
            return

        kargs = {
            "Source": Source,
            "EventName": EventName,
            "ViewController": ViewController,
            "Supplement": Supplement,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._event_name = kwargs["EventName"]
        self._view_controller = kwargs["ViewController"]
        self._supplement = kwargs["Supplement"]
        inst_keys = ('EventName', 'ViewController', 'Supplement')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def EventName(self) -> str:
        """
        specifies the name of the event.
        
        It's the responsibility of the component supporting the XDocumentEventBroadcaster interface to specify which events it supports.
        """
        return self._event_name

    @EventName.setter
    def EventName(self, value: str) -> None:
        self._event_name = value

    @property
    def ViewController(self) -> XController2_bbcf0bc1:
        """
        denotes the view respectively controller which the event applies to.
        
        Might be NULL if the event is not related to a concrete view of the document.
        """
        return self._view_controller

    @ViewController.setter
    def ViewController(self, value: XController2_bbcf0bc1) -> None:
        self._view_controller = value

    @property
    def Supplement(self) -> object:
        """
        contains supplemental information about the event which is being notified
        
        The semantics of this additional information needs to be specified by the broadcaster of the event.
        """
        return self._supplement

    @Supplement.setter
    def Supplement(self, value: object) -> None:
        self._supplement = value


__all__ = ['DocumentEvent']
