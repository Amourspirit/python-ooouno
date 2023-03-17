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
# Namespace: com.sun.star.configuration
# Libre Office Version: 7.4
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6


class theDefaultProvider(XMultiServiceFactory_191e0eb6):
    """
    Singleton Class

    The default ConfigurationProvider.
    
    This singleton somewhat arbitrarily makes available the com.sun.star.lang.XMultiServiceFactory interface of the (old-style) DefaultProvider service, as it is the most frequently used one. See the DefaultProvider service for details.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API theDefaultProvider <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1configuration_1_1theDefaultProvider.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.theDefaultProvider'
    __ooo_type_name__: str = 'singleton'
    _instance = None

    def __new__(cls, *args, **kwargs):
        # single instance only allowed
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


__all__ = ['theDefaultProvider']

