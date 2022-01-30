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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ui
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper.enum_helper import uno_enum_class_new
    from com.sun.star.ui.ContextMenuInterceptorAction import (CANCELLED, CONTINUE_MODIFIED, EXECUTE_MODIFIED, IGNORED)

if TYPE_CHECKING or _DYNAMIC is False:


    class ContextMenuInterceptorAction(Enum):
        """
        Enum Class

        

        See Also:
            `API ContextMenuInterceptorAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui.html#a6e0452a8960be949dce52c427920ebbe>`_
        """
        CANCELLED = 'CANCELLED'
        """
        the context menu must not be executed.
        
        The next registered XContextMenuInterceptor should not be notified.
        """
        CONTINUE_MODIFIED = 'CONTINUE_MODIFIED'
        """
        the menu has been modified and the next registered XContextMenuInterceptor should be notified.
        """
        EXECUTE_MODIFIED = 'EXECUTE_MODIFIED'
        """
        the menu has been modified and should be executed without notifying the next registered XContextMenuInterceptor.
        """
        IGNORED = 'IGNORED'
        """
        the XContextMenuInterceptor has ignored the call.
        
        The next registered XContextMenuInterceptor should be notified.
        """

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global ContextMenuInterceptorAction
        _dict = {
            "CANCELLED": CANCELLED,
            "CONTINUE_MODIFIED": CONTINUE_MODIFIED,
            "EXECUTE_MODIFIED": EXECUTE_MODIFIED,
            "IGNORED": IGNORED,
        }

        ContextMenuInterceptorAction = type('ContextMenuInterceptorAction', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(ContextMenuInterceptorAction, k, v)

    _dynamic_enum()

__all__ = ['ContextMenuInterceptorAction']

