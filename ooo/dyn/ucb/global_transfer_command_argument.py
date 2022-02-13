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
        from com.sun.star.ucb import GlobalTransferCommandArgument as UGlobalTransferCommandArgument
        # Dynamically create uno com.sun.star.ucb.GlobalTransferCommandArgument using uno
        global GlobalTransferCommandArgument

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.ucb.GlobalTransferCommandArgument'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.ucb'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.ucb.GlobalTransferCommandArgument'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(Operation = UNO_NONE, SourceURL = UNO_NONE, TargetURL = UNO_NONE, NewTitle = UNO_NONE, NameClash = UNO_NONE):
            ns = 'com.sun.star.ucb.GlobalTransferCommandArgument'
            if isinstance(Operation, UGlobalTransferCommandArgument):
                inst = uno.createUnoStruct(ns, Operation)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not Operation is UNO_NONE:
                if getattr(struct, 'Operation') != Operation:
                    setattr(struct, 'Operation', Operation)
            if not SourceURL is UNO_NONE:
                if getattr(struct, 'SourceURL') != SourceURL:
                    setattr(struct, 'SourceURL', SourceURL)
            if not TargetURL is UNO_NONE:
                if getattr(struct, 'TargetURL') != TargetURL:
                    setattr(struct, 'TargetURL', TargetURL)
            if not NewTitle is UNO_NONE:
                if getattr(struct, 'NewTitle') != NewTitle:
                    setattr(struct, 'NewTitle', NewTitle)
            if not NameClash is UNO_NONE:
                if getattr(struct, 'NameClash') != NameClash:
                    setattr(struct, 'NameClash', NameClash)
            _set_attr(struct)
            _set_fn_attr(struct)
            return struct
        _set_attr(_struct_init)
        GlobalTransferCommandArgument = _struct_init

    _dynamic_struct()
else:
    from ...lo.ucb.global_transfer_command_argument import GlobalTransferCommandArgument as GlobalTransferCommandArgument

__all__ = ['GlobalTransferCommandArgument']

