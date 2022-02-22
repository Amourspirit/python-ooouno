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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.uno
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE

if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    import uno
 
    def _get_class():
        orig_init = None
        def init(self, Message = UNO_NONE, Context = UNO_NONE):
            if getattr(Message, "__class__", None) == self.__class__:
                orig_init(self, Message)
                return
            else:
                orig_init(self)
            if not Message is UNO_NONE:
                if getattr(self, 'Message') != Message:
                    setattr(self, 'Message', Message)
            if not Context is UNO_NONE:
                if getattr(self, 'Context') != Context:
                    setattr(self, 'Context', Context)

        type_name = 'com.sun.star.uno.Exception'
        ex = uno.getClass(type_name)
        ex.__ooo_ns__ = 'com.sun.star.uno'
        ex.__ooo_full_ns__= type_name
        ex.__ooo_type_name__ = 'exception'
        orig_init = ex.__init__
        ex.__init__ = init
        return ex

    Exception = _get_class()

else:
    from ...lo.uno.exception import Exception as Exception

__all__ = ['Exception']

