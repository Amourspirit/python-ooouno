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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
from __future__ import annotations
from ..lang.x_multi_component_factory import XMultiComponentFactory as XMultiComponentFactory_381b0f98

class CanvasFactory(XMultiComponentFactory_381b0f98):
    """
    Service Class

    The CanvasFactory is used to create the Canvas objects, evaluating the user's configuration preferences from.
    
    /org.openoffice.VCL/Settings/Canvas/PreferredServices.
    
    The latter specifies a string list of service names to use.
    
    Instantiating this service, you can use its com.sun.star.lang.XMultiComponentFactory interface to create Canvas objects, passing an empty string as service specifier (default). If you want to manually override the configured service list, you can pass a service name to try first.
    
    **since**
    
        OOo 2.0

    See Also:
        `API CanvasFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1rendering_1_1CanvasFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.CanvasFactory'
    __ooo_type_name__: str = 'service'


__all__ = ['CanvasFactory']

