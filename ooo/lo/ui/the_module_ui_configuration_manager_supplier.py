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
# Singleton Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ui
# Libre Office Version: 7.3
from .x_module_ui_configuration_manager_supplier import XModuleUIConfigurationManagerSupplier as XModuleUIConfigurationManagerSupplier_20b814a9


class theModuleUIConfigurationManagerSupplier(XModuleUIConfigurationManagerSupplier_20b814a9):
    """
    Singleton Class

    specifies a central user interface configuration provider which gives access to module based user interface configuration managers.
    
    Controls module based user interface configuration managers.
    
    There can only exist one user interface configuration manager for a module. A user interface configuration manager supports to get and set user interface configuration data for configurable user interface elements.
    
    Prior to LibreOffice 4.3, this singleton was only available as a (single-instance) ModuleUIConfigurationManagerSupplier service.
    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API theModuleUIConfigurationManagerSupplier <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1ui_1_1theModuleUIConfigurationManagerSupplier.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.theModuleUIConfigurationManagerSupplier'
    __ooo_type_name__: str = 'singleton'
    _instance = None

    def __new__(cls, *args, **kwargs):
        # single instance only allowed
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


__all__ = ['theModuleUIConfigurationManagerSupplier']

