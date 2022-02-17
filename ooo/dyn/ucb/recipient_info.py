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
        from com.sun.star.ucb import RecipientInfo as URecipientInfo
        # Dynamically create uno com.sun.star.ucb.RecipientInfo using uno
        global RecipientInfo

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.ucb.RecipientInfo'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.ucb'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.ucb.RecipientInfo'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(ProtocolType = UNO_NONE, State = UNO_NONE, To = UNO_NONE, CC = UNO_NONE, BCC = UNO_NONE, Newsgroups = UNO_NONE, Server = UNO_NONE, Username = UNO_NONE, Password = UNO_NONE, VIMPostOfficePath = UNO_NONE, ProtocolErrorString = UNO_NONE, ProtocolErrorNumber = UNO_NONE, SendTries = UNO_NONE):
            ns = 'com.sun.star.ucb.RecipientInfo'
            if isinstance(ProtocolType, URecipientInfo):
                inst = uno.createUnoStruct(ns, ProtocolType)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not ProtocolType is UNO_NONE:
                if getattr(struct, 'ProtocolType') != ProtocolType:
                    setattr(struct, 'ProtocolType', ProtocolType)
            if not State is UNO_NONE:
                if getattr(struct, 'State') != State:
                    setattr(struct, 'State', State)
            if not To is UNO_NONE:
                if getattr(struct, 'To') != To:
                    setattr(struct, 'To', To)
            if not CC is UNO_NONE:
                if getattr(struct, 'CC') != CC:
                    setattr(struct, 'CC', CC)
            if not BCC is UNO_NONE:
                if getattr(struct, 'BCC') != BCC:
                    setattr(struct, 'BCC', BCC)
            if not Newsgroups is UNO_NONE:
                if getattr(struct, 'Newsgroups') != Newsgroups:
                    setattr(struct, 'Newsgroups', Newsgroups)
            if not Server is UNO_NONE:
                if getattr(struct, 'Server') != Server:
                    setattr(struct, 'Server', Server)
            if not Username is UNO_NONE:
                if getattr(struct, 'Username') != Username:
                    setattr(struct, 'Username', Username)
            if not Password is UNO_NONE:
                if getattr(struct, 'Password') != Password:
                    setattr(struct, 'Password', Password)
            if not VIMPostOfficePath is UNO_NONE:
                if getattr(struct, 'VIMPostOfficePath') != VIMPostOfficePath:
                    setattr(struct, 'VIMPostOfficePath', VIMPostOfficePath)
            if not ProtocolErrorString is UNO_NONE:
                if getattr(struct, 'ProtocolErrorString') != ProtocolErrorString:
                    setattr(struct, 'ProtocolErrorString', ProtocolErrorString)
            if not ProtocolErrorNumber is UNO_NONE:
                if getattr(struct, 'ProtocolErrorNumber') != ProtocolErrorNumber:
                    setattr(struct, 'ProtocolErrorNumber', ProtocolErrorNumber)
            if not SendTries is UNO_NONE:
                if getattr(struct, 'SendTries') != SendTries:
                    setattr(struct, 'SendTries', SendTries)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        RecipientInfo = _struct_init

    _dynamic_struct()
else:
    from ...lo.ucb.recipient_info import RecipientInfo as RecipientInfo

__all__ = ['RecipientInfo']
