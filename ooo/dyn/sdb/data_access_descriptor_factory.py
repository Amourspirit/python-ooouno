# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdb
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False

if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_singleton() -> None:
        # Dynamically create uno singleton using component context
        import uno
        global DataAccessDescriptorFactory

        def _singleton_init():
            ctx = uno.getComponentContext()
            key = '/singletons/com.sun.star.sdb.DataAccessDescriptorFactory'
            singleton = ctx.getByName(key)
            return singleton
        DataAccessDescriptorFactory = _singleton_init
    _dynamic_singleton()
else:
    if TYPE_CHECKING:
        from com.sun.star.sdb import DataAccessDescriptorFactory as DataAccessDescriptorFactory
    else:
        from ...lo.sdb.data_access_descriptor_factory import DataAccessDescriptorFactory as DataAccessDescriptorFactory

__all__ = ['DataAccessDescriptorFactory']
