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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.embed
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..awt.size import Size as Size_576707ef
    from ..awt.x_window_peer import XWindowPeer as XWindowPeer_99760ab0
    from .x_hatch_window import XHatchWindow as XHatchWindow_b9aa0bbd

class XHatchWindowFactory(XInterface_8f010a43):
    """
    creates a hatch window implementation.

    See Also:
        `API XHatchWindowFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XHatchWindowFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XHatchWindowFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XHatchWindowFactory'

    @abstractmethod
    def createHatchWindowInstance(self, xParent: 'XWindowPeer_99760ab0', aBounds: 'Rectangle_84b109e9', aSize: 'Size_576707ef') -> 'XHatchWindow_b9aa0bbd':
        """
        creates a new hatch window instance.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XHatchWindowFactory']

