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
# Namespace: com.sun.star.lang
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_ex() -> None:
        import uno
        # Dynamically create uno com.sun.star.lang.IllegalArgumentException using uno
        global IllegalArgumentException

        def _set_fn_attr(ex):
            type_name = 'com.sun.star.lang.IllegalArgumentException'
            ex.__dict__['typeName'] = type_name
            ex.__dict__['__pyunointerface__'] = type_name
            ex.__dict__['__pyunostruct__'] = type_name

        def _set_attr(ex):
            ex.__dict__['__ooo_ns__'] = 'com.sun.star.lang'
            ex.__dict__['__ooo_full_ns__'] = 'com.sun.star.lang.IllegalArgumentException'
            ex.__dict__['__ooo_type_name__'] = 'exception'

        def _ex_init(**kwargs):
            ns = 'com.sun.star.lang.IllegalArgumentException'
            ex = uno.createUnoStruct(ns)
            for k, v in kwargs.items():
                if v is UNO_NONE:
                    continue
                else:
                    setattr(ex, k, v)
            _set_attr(ex)
            return ex
        _set_attr(_ex_init)
        _set_fn_attr(_ex_init)
        IllegalArgumentException = _ex_init

    _dynamic_ex()
else:
    from ...lo.lang.illegal_argument_exception import IllegalArgumentException as IllegalArgumentException
    
__all__ = ['IllegalArgumentException']

