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
# Namespace: com.sun.star.frame
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..lang.x_component import XComponent as XComponent_98dc0ab5

class XComponentLoader(XInterface_8f010a43):
    """
    this is a simple interface to load components by a URL into a frame environment

    See Also:
        `API XComponentLoader <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XComponentLoader.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XComponentLoader'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XComponentLoader'

    @abstractmethod
    def loadComponentFromURL(self, URL: str, TargetFrameName: str, SearchFlags: int, Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'XComponent_98dc0ab5':
        """
        loads a component specified by a URL into the specified new or existing frame.
        
        To create new documents, use \"private:factory/scalc\", \"private:factory/swriter\", etc. Other special protocols (e.g. \"slot:\", \".uno\") are not allowed and raise a com.sun.star.lang.IllegalArgumentException.
        
        If a frame with the specified name already exists, it is used, otherwise it is created. There exist some special targets which never can be used as real frame names:
        
        Note: These flags are optional ones and will be used for non special target names only.
        
        For example, \"ReadOnly\" with a boolean value specifies whether the document is opened read-only. \"FilterName\" specifies the component type to create and the filter to use, for example: \"Text - CSV\". For more information see com.sun.star.document.MediaDescriptor.
        
        This interface is a generic one and can be used to start further requests on loaded document or control the lifetime of it (means dispose() it after using). The real document service behind this interface can be one of follow three ones:

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XComponentLoader']

