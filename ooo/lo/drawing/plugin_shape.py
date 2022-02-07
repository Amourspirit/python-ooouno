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
# Namespace: com.sun.star.drawing
import typing
from abc import abstractproperty
from .shape import Shape as Shape_85cc09e5
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class PluginShape(Shape_85cc09e5):
    """
    Service Class

    This Shape encapsulates a plugin.
    
    A plugin is a binary object that is plugged into a document to represent a media-type that is not handled natively by the application.

    See Also:
        `API PluginShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1PluginShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.PluginShape'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def PluginMimeType(self) -> str:
        """
        This property specifies the media-type to which this plugin should be registered.
        """
    @abstractproperty
    def PluginURL(self) -> str:
        """
        This property specifies the url to the binary object.
        """
    @abstractproperty
    def PluginCommands(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        This sequence contains parameters that are passed to the application that renders the plugin when it is initialized.
        """

__all__ = ['PluginShape']

