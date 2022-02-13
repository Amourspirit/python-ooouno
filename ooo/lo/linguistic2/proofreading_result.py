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
from ooo.oenv import UNO_NONE
import typing
from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
from ..lang.locale import Locale as Locale_70d308fa
from .single_proofreading_error import SingleProofreadingError as SingleProofreadingError_c54812c1
from .x_proofreader import XProofreader as XProofreader_dab0e46
from ..text.x_flat_paragraph import XFlatParagraph as XFlatParagraph_c8310c42


class ProofreadingResult(object):
    """
    Struct Class

    holds the results from proofreading a sentence.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API ProofreadingResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1linguistic2_1_1ProofreadingResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.ProofreadingResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.linguistic2.ProofreadingResult'
    """Literal Constant ``com.sun.star.linguistic2.ProofreadingResult``"""

    def __init__(self, aErrors: typing.Tuple[SingleProofreadingError_c54812c1, ...] = UNO_NONE, aProperties: typing.Tuple[PropertyValue_c9610c73, ...] = UNO_NONE, aDocumentIdentifier: str = '', xFlatParagraph: XFlatParagraph_c8310c42 = None, aText: str = '', aLocale: Locale_70d308fa = UNO_NONE, nStartOfSentencePosition: int = 0, nBehindEndOfSentencePosition: int = 0, nStartOfNextSentencePosition: int = 0, xProofreader: XProofreader_dab0e46 = None) -> None:
        """
        Constructor

        Other Arguments:
            ``aErrors`` can be another ``ProofreadingResult`` instance,
                in which case other named args are ignored.

        Arguments:
            aErrors (Tuple[SingleProofreadingError, ...], optional): aErrors value
            aProperties (Tuple[PropertyValue, ...], optional): aProperties value
            aDocumentIdentifier (str, optional): aDocumentIdentifier value
            xFlatParagraph (XFlatParagraph, optional): xFlatParagraph value
            aText (str, optional): aText value
            aLocale (Locale, optional): aLocale value
            nStartOfSentencePosition (int, optional): nStartOfSentencePosition value
            nBehindEndOfSentencePosition (int, optional): nBehindEndOfSentencePosition value
            nStartOfNextSentencePosition (int, optional): nStartOfNextSentencePosition value
            xProofreader (XProofreader, optional): xProofreader value
        """
        if isinstance(aErrors, ProofreadingResult):
            oth: ProofreadingResult = aErrors
            self._a_errors = oth.aErrors
            self._a_properties = oth.aProperties
            self._a_document_identifier = oth.aDocumentIdentifier
            self._x_flat_paragraph = oth.xFlatParagraph
            self._a_text = oth.aText
            self._a_locale = oth.aLocale
            self._n_start_of_sentence_position = oth.nStartOfSentencePosition
            self._n_behind_end_of_sentence_position = oth.nBehindEndOfSentencePosition
            self._n_start_of_next_sentence_position = oth.nStartOfNextSentencePosition
            self._x_proofreader = oth.xProofreader
            return
        else:
            if aErrors is UNO_NONE:
                self._a_errors = None
            else:
                self._a_errors = aErrors
            if aProperties is UNO_NONE:
                self._a_properties = None
            else:
                self._a_properties = aProperties
            self._a_document_identifier = aDocumentIdentifier
            self._x_flat_paragraph = xFlatParagraph
            self._a_text = aText
            if aLocale is UNO_NONE:
                self._a_locale = Locale_70d308fa()
            else:
                self._a_locale = aLocale
            self._n_start_of_sentence_position = nStartOfSentencePosition
            self._n_behind_end_of_sentence_position = nBehindEndOfSentencePosition
            self._n_start_of_next_sentence_position = nStartOfNextSentencePosition
            self._x_proofreader = xProofreader



    @property
    def aErrors(self) -> typing.Tuple[SingleProofreadingError_c54812c1, ...]:
        return self._a_errors
    
    @aErrors.setter
    def aErrors(self, value: typing.Tuple[SingleProofreadingError_c54812c1, ...]) -> None:
        self._a_errors = value

    @property
    def aProperties(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        return self._a_properties
    
    @aProperties.setter
    def aProperties(self, value: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        self._a_properties = value

    @property
    def aDocumentIdentifier(self) -> str:
        return self._a_document_identifier
    
    @aDocumentIdentifier.setter
    def aDocumentIdentifier(self, value: str) -> None:
        self._a_document_identifier = value

    @property
    def xFlatParagraph(self) -> XFlatParagraph_c8310c42:
        return self._x_flat_paragraph
    
    @xFlatParagraph.setter
    def xFlatParagraph(self, value: XFlatParagraph_c8310c42) -> None:
        self._x_flat_paragraph = value

    @property
    def aText(self) -> str:
        return self._a_text
    
    @aText.setter
    def aText(self, value: str) -> None:
        self._a_text = value

    @property
    def aLocale(self) -> Locale_70d308fa:
        return self._a_locale
    
    @aLocale.setter
    def aLocale(self, value: Locale_70d308fa) -> None:
        self._a_locale = value

    @property
    def nStartOfSentencePosition(self) -> int:
        return self._n_start_of_sentence_position
    
    @nStartOfSentencePosition.setter
    def nStartOfSentencePosition(self, value: int) -> None:
        self._n_start_of_sentence_position = value

    @property
    def nBehindEndOfSentencePosition(self) -> int:
        return self._n_behind_end_of_sentence_position
    
    @nBehindEndOfSentencePosition.setter
    def nBehindEndOfSentencePosition(self, value: int) -> None:
        self._n_behind_end_of_sentence_position = value

    @property
    def nStartOfNextSentencePosition(self) -> int:
        return self._n_start_of_next_sentence_position
    
    @nStartOfNextSentencePosition.setter
    def nStartOfNextSentencePosition(self, value: int) -> None:
        self._n_start_of_next_sentence_position = value

    @property
    def xProofreader(self) -> XProofreader_dab0e46:
        return self._x_proofreader
    
    @xProofreader.setter
    def xProofreader(self, value: XProofreader_dab0e46) -> None:
        self._x_proofreader = value


__all__ = ['ProofreadingResult']
