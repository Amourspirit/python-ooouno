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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.ucb import PostCommandArgument as UPostCommandArgument
        # Dynamically create uno com.sun.star.ucb.PostCommandArgument using uno
        global PostCommandArgument

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.ucb'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.ucb.PostCommandArgument'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Source = UNO_NONE, Sink = UNO_NONE):
            ns = 'com.sun.star.ucb.PostCommandArgument'
            if isinstance(Source, UPostCommandArgument):
                inst = uno.createUnoStruct(ns, Source)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Source is UNO_NONE:
                if getattr(struct, 'Source') != Source:
                    setattr(struct, 'Source', Source)
            if not Sink is UNO_NONE:
                if getattr(struct, 'Sink') != Sink:
                    setattr(struct, 'Sink', Sink)
            _set_attr(struct)
            return struct
        PostCommandArgument = _struct_init

    _dynamic_struct()
else:
    from ...lo.ucb.post_command_argument import PostCommandArgument as PostCommandArgument

__all__ = ['PostCommandArgument']

