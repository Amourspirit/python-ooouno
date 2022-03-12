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
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .x_drag_source import XDragSource as XDragSource_49900fb2
from .x_drag_source_context import XDragSourceContext as XDragSourceContext_c2661297


class DragSourceEvent(EventObject_a3d70b03):
    """
    Struct Class

    This class is the base class for DragSourceDragEvent and DragSourceDropEvent.
    
    To access the XDragSource that originated this event, use the com.sun.star.lang.EventObject.Source member of this object.

    See Also:
        `API DragSourceEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DragSourceEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.DragSourceEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.datatransfer.dnd.DragSourceEvent'
    """Literal Constant ``com.sun.star.datatransfer.dnd.DragSourceEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, DragSourceContext: typing.Optional[XDragSourceContext_c2661297] = None, DragSource: typing.Optional[XDragSource_49900fb2] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            DragSourceContext (XDragSourceContext, optional): DragSourceContext value.
            DragSource (XDragSource, optional): DragSource value.
        """
        kargs = {
            "Source": Source,
            "DragSourceContext": DragSourceContext,
            "DragSource": DragSource,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._drag_source_context = kwargs["DragSourceContext"]
        self._drag_source = kwargs["DragSource"]
        inst_keys = ('DragSourceContext', 'DragSource')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def DragSourceContext(self) -> XDragSourceContext_c2661297:
        """
        The drag source context of the current drag operation.
        """
        return self._drag_source_context
    
    @DragSourceContext.setter
    def DragSourceContext(self, value: XDragSourceContext_c2661297) -> None:
        self._drag_source_context = value

    @property
    def DragSource(self) -> XDragSource_49900fb2:
        """
        The drag source on which the Drag and Drop operation was initiated.
        """
        return self._drag_source
    
    @DragSource.setter
    def DragSource(self, value: XDragSource_49900fb2) -> None:
        self._drag_source = value


__all__ = ['DragSourceEvent']
