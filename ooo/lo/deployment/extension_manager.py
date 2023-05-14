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
# Singleton Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.deployment
# Libre Office Version: 7.4
from .x_extension_manager import XExtensionManager as XExtensionManager_4e471019


class ExtensionManager(XExtensionManager_4e471019):
    """
    Singleton Class

    the ExtensionManager service.
    
    The component context entry is  /singletons/com.sun.star.deployment.ExtensionManager .
    
    **since**
    
        OOo 3.3

    See Also:
        `API ExtensionManager <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1deployment_1_1ExtensionManager.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.ExtensionManager'
    __ooo_type_name__: str = 'singleton'
    _instance = None

    def __new__(cls, *args, **kwargs):
        # single instance only allowed
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


__all__ = ['ExtensionManager']

