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
# Namespace: com.sun.star.configuration
from abc import abstractproperty
from .configuration_provider import ConfigurationProvider as ConfigurationProvider_cc8d1323
from ..lang.x_localizable import XLocalizable as XLocalizable_aee00b64
from ..util.x_flushable import XFlushable as XFlushable_9a420ab4
from ..util.x_refreshable import XRefreshable as XRefreshable_b0d60b81

class DefaultProvider(ConfigurationProvider_cc8d1323, XLocalizable_aee00b64, XFlushable_9a420ab4, XRefreshable_b0d60b81):
    """
    Service Class

    is a ConfigurationProvider, that is the default ConfigurationProvider for its com.sun.star.uno.XComponentContext.
    
    This object is accessible as singleton theDefaultProvider
    
    .
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DefaultProvider <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1DefaultProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.DefaultProvider'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def EnableAsync(self) -> bool:
        """
        Property to enable/disable asynchronous write-back from in-memory cache to backend(s)
        
        **since**
        
            OOo 2.0
        """
        ...



__all__ = ['DefaultProvider']

