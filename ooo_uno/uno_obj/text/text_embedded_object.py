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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
import typing
from abc import abstractproperty
from ..document.x_embedded_object_supplier import XEmbeddedObjectSupplier as XEmbeddedObjectSupplier_8b631174
from .base_frame import BaseFrame as BaseFrame_8f020a33
if typing.TYPE_CHECKING:
    from ..frame.x_model import XModel as XModel_7a6e095c
    from ..lang.x_component import XComponent as XComponent_98dc0ab5

class TextEmbeddedObject(BaseFrame_8f020a33, XEmbeddedObjectSupplier_8b631174):
    """
    provides access to the properties and methods of an embedded object.

    See Also:
        `API TextEmbeddedObject <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextEmbeddedObject.html>`_
    """

    @abstractproperty
    def CLSID(self) -> str:
        """
        """
    @abstractproperty
    def Component(self) -> 'XComponent_98dc0ab5':
        """
        This is the component for the OLE2 object.
        """
    @abstractproperty
    def Model(self) -> 'XModel_7a6e095c':
        """
        This is the model for the OLE2 object.
        
        This property if void if the OLE2 is not an Office component.
        """

__all__ = ['TextEmbeddedObject']

