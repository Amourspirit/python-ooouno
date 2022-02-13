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
# Namespace: com.sun.star.linguistic2
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME, UNO_NONE
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct():
        import uno
        from com.sun.star.linguistic2 import ProofreadingResult as UProofreadingResult
        # Dynamically create uno com.sun.star.linguistic2.ProofreadingResult using uno
        global ProofreadingResult

        def _set_attr(struct):
            struct.__dict__['__ooo_ns__'] = 'com.sun.star.linguistic2'
            struct.__dict__['__ooo_full_ns__'] = 'com.sun.star.linguistic2.ProofreadingResult'
            struct.__dict__['__ooo_type_name__'] = 'struct'

        def _struct_init(aErrors = UNO_NONE, aProperties = UNO_NONE, aDocumentIdentifier = UNO_NONE, xFlatParagraph = UNO_NONE, aText = UNO_NONE, aLocale = UNO_NONE, nStartOfSentencePosition = UNO_NONE, nBehindEndOfSentencePosition = UNO_NONE, nStartOfNextSentencePosition = UNO_NONE, xProofreader = UNO_NONE):
            ns = 'com.sun.star.linguistic2.ProofreadingResult'
            if isinstance(aErrors, UProofreadingResult):
                inst = uno.createUnoStruct(ns, aErrors)
                _set_attr(inst)
                return inst
            struct = uno.createUnoStruct(ns)

            if not aErrors is UNO_NONE:
                if getattr(struct, 'aErrors') != aErrors:
                    setattr(struct, 'aErrors', aErrors)
            if not aProperties is UNO_NONE:
                if getattr(struct, 'aProperties') != aProperties:
                    setattr(struct, 'aProperties', aProperties)
            if not aDocumentIdentifier is UNO_NONE:
                if getattr(struct, 'aDocumentIdentifier') != aDocumentIdentifier:
                    setattr(struct, 'aDocumentIdentifier', aDocumentIdentifier)
            if not xFlatParagraph is UNO_NONE:
                if getattr(struct, 'xFlatParagraph') != xFlatParagraph:
                    setattr(struct, 'xFlatParagraph', xFlatParagraph)
            if not aText is UNO_NONE:
                if getattr(struct, 'aText') != aText:
                    setattr(struct, 'aText', aText)
            if not aLocale is UNO_NONE:
                if getattr(struct, 'aLocale') != aLocale:
                    setattr(struct, 'aLocale', aLocale)
            if not nStartOfSentencePosition is UNO_NONE:
                if getattr(struct, 'nStartOfSentencePosition') != nStartOfSentencePosition:
                    setattr(struct, 'nStartOfSentencePosition', nStartOfSentencePosition)
            if not nBehindEndOfSentencePosition is UNO_NONE:
                if getattr(struct, 'nBehindEndOfSentencePosition') != nBehindEndOfSentencePosition:
                    setattr(struct, 'nBehindEndOfSentencePosition', nBehindEndOfSentencePosition)
            if not nStartOfNextSentencePosition is UNO_NONE:
                if getattr(struct, 'nStartOfNextSentencePosition') != nStartOfNextSentencePosition:
                    setattr(struct, 'nStartOfNextSentencePosition', nStartOfNextSentencePosition)
            if not xProofreader is UNO_NONE:
                if getattr(struct, 'xProofreader') != xProofreader:
                    setattr(struct, 'xProofreader', xProofreader)
            _set_attr(struct)
            return struct
        ProofreadingResult = _struct_init

    _dynamic_struct()
else:
    from ...lo.linguistic2.proofreading_result import ProofreadingResult as ProofreadingResult

__all__ = ['ProofreadingResult']

