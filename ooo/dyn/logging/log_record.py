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
# Namespace: com.sun.star.logging
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.logging import LogRecord as ULogRecord
        # Dynamically create uno com.sun.star.logging.LogRecord using uno
        global LogRecord

        def _set_fn_attr(struct):
            type_name = 'com.sun.star.logging.LogRecord'
            struct.__dict__['typeName'] = type_name
            struct.__dict__['__pyunointerface__'] = type_name
            struct.__dict__['__pyunostruct__'] = type_name

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.logging'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.logging.LogRecord'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(LoggerName = UNO_NONE, SourceClassName = UNO_NONE, SourceMethodName = UNO_NONE, Message = UNO_NONE, LogTime = UNO_NONE, SequenceNumber = UNO_NONE, ThreadID = UNO_NONE, Level = UNO_NONE):
            ns = 'com.sun.star.logging.LogRecord'
            if isinstance(LoggerName, ULogRecord):
                inst = uno.createUnoStruct(ns, LoggerName)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not LoggerName is UNO_NONE:
                if getattr(struct, 'LoggerName') != LoggerName:
                    setattr(struct, 'LoggerName', LoggerName)
            if not SourceClassName is UNO_NONE:
                if getattr(struct, 'SourceClassName') != SourceClassName:
                    setattr(struct, 'SourceClassName', SourceClassName)
            if not SourceMethodName is UNO_NONE:
                if getattr(struct, 'SourceMethodName') != SourceMethodName:
                    setattr(struct, 'SourceMethodName', SourceMethodName)
            if not Message is UNO_NONE:
                if getattr(struct, 'Message') != Message:
                    setattr(struct, 'Message', Message)
            if not LogTime is UNO_NONE:
                if getattr(struct, 'LogTime') != LogTime:
                    setattr(struct, 'LogTime', LogTime)
            if not SequenceNumber is UNO_NONE:
                if getattr(struct, 'SequenceNumber') != SequenceNumber:
                    setattr(struct, 'SequenceNumber', SequenceNumber)
            if not ThreadID is UNO_NONE:
                if getattr(struct, 'ThreadID') != ThreadID:
                    setattr(struct, 'ThreadID', ThreadID)
            if not Level is UNO_NONE:
                if getattr(struct, 'Level') != Level:
                    setattr(struct, 'Level', Level)
            _set_attr(struct)
            return struct
        _set_attr(_struct_init)
        _set_fn_attr(_struct_init)
        LogRecord = _struct_init

    _dynamic_struct()
else:
    from ...lo.logging.log_record import LogRecord as LogRecord

__all__ = ['LogRecord']

