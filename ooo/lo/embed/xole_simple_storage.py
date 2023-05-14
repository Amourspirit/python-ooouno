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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.embed
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
from .x_classified_object import XClassifiedObject as XClassifiedObject_fa3b0dab
from .x_transacted_object import XTransactedObject as XTransactedObject_fb510dbd
from ..lang.x_component import XComponent as XComponent_98dc0ab5

class XOLESimpleStorage(XNameContainer_cb90e47, XClassifiedObject_fa3b0dab, XTransactedObject_fb510dbd, XComponent_98dc0ab5):
    """
    This interface allows to access and change contents of OLE storages.
    
    This is a simple container allowing the access to OLE storages. The subcomponents are either OLE storages themselves or streams.

    See Also:
        `API XOLESimpleStorage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XOLESimpleStorage.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XOLESimpleStorage'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XOLESimpleStorage'


__all__ = ['XOLESimpleStorage']

