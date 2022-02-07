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
# Libre Office Version: 7.2
# Namespace: com.sun.star.frame
from typing import Tuple, TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False

if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_singleton() -> None:
        # Dynamically create uno singleton using component context
        import uno
        global theStatusbarControllerFactory

        def _singleton_init():
            ctx = uno.getComponentContext()
            key = '/singletons/com.sun.star.frame.theStatusbarControllerFactory/service'
            en: Tuple[str] = ctx.getElementNames()
            if not key in en:
                raise KeyError("Key '%s' not found in Component Context Element Names", key)
            singleton = ctx.getValueByName(key)
            if not hasattr(singleton, '__ooo_ns__'):
                setattr(singleton, ' __ooo_ns__', 'com.sun.star.frame')
                setattr(singleton, ' __ooo_full_ns__', 'com.sun.star.frame.theStatusbarControllerFactory')
                setattr(singleton, ' __ooo_type_name__', 'singleton')
            return singleton
        theStatusbarControllerFactory = _singleton_init
    _dynamic_singleton()
else:
    from ...lo.frame.the_statusbar_controller_factory import theStatusbarControllerFactory as theStatusbarControllerFactory

__all__ = ['theStatusbarControllerFactory']
