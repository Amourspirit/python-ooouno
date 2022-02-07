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
# Namespace: com.sun.star.script
from .x_invocation_adapter_factory2 import XInvocationAdapterFactory2 as XInvocationAdapterFactory2_a0fe11da

class InvocationAdapterFactory(XInvocationAdapterFactory2_a0fe11da):
    """
    Service Class

    Provides functionality to create an adapter that supports (a) special interface type(s) and maps calls to the interface's methods to an invocation interface.
    
    An adapter like this allows generic dispatch interfaces to meet interface requirements, e.g. if a specific listener interface has to be passed to an add...Listener method.
    
    The adapter has to support com.sun.star.script.XInvocationAdapterFactory. The adapter may also support com.sun.star.script.XInvocationAdapterFactory2.

    See Also:
        `API InvocationAdapterFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1script_1_1InvocationAdapterFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.InvocationAdapterFactory'
    __ooo_type_name__: str = 'service'


__all__ = ['InvocationAdapterFactory']

