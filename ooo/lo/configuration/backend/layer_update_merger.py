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
# Namespace: com.sun.star.configuration.backend
from .x_update_handler import XUpdateHandler as XUpdateHandler_d8f512ef
from ...lang.x_initialization import XInitialization as XInitialization_d46c0cca

class LayerUpdateMerger(XUpdateHandler_d8f512ef, XInitialization_d46c0cca):
    """
    Service Class

    applies updates to a configuration layer.
    
    The configuration layer data is read from a XLayer and the changed layer is provided as XLayer again or described to a XLayerHandler.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API LayerUpdateMerger <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1LayerUpdateMerger.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.LayerUpdateMerger'
    __ooo_type_name__: str = 'service'


__all__ = ['LayerUpdateMerger']

