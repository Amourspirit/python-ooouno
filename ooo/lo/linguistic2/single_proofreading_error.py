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
import typing
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class SingleProofreadingError(object):
    """
    Struct Class

    holds a single error found by the proofreader.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API SingleProofreadingError <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1linguistic2_1_1SingleProofreadingError.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.SingleProofreadingError'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.linguistic2.SingleProofreadingError'
    """Literal Constant ``com.sun.star.linguistic2.SingleProofreadingError``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``SingleProofreadingError`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``SingleProofreadingError``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            nErrorStart (int, optional): nErrorStart value
            nErrorLength (int, optional): nErrorLength value
            nErrorType (int, optional): nErrorType value
            aRuleIdentifier (str, optional): aRuleIdentifier value
            aShortComment (str, optional): aShortComment value
            aFullComment (str, optional): aFullComment value
            aSuggestions (Tuple[str, ...], optional): aSuggestions value
            aProperties (Tuple[PropertyValue, ...], optional): aProperties value
        """
        self._n_error_start = None
        self._n_error_length = None
        self._n_error_type = None
        self._a_rule_identifier = None
        self._a_short_comment = None
        self._a_full_comment = None
        self._a_suggestions = None
        self._a_properties = None

        key_order = ('nErrorStart', 'nErrorLength', 'nErrorType', 'aRuleIdentifier', 'aShortComment', 'aFullComment', 'aSuggestions', 'aProperties')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], SingleProofreadingError):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("SingleProofreadingError.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def nErrorStart(self) -> int:
        return self._n_error_start
    
    @nErrorStart.setter
    def nErrorStart(self, value: int) -> None:
        self._n_error_start = value

    @property
    def nErrorLength(self) -> int:
        return self._n_error_length
    
    @nErrorLength.setter
    def nErrorLength(self, value: int) -> None:
        self._n_error_length = value

    @property
    def nErrorType(self) -> int:
        return self._n_error_type
    
    @nErrorType.setter
    def nErrorType(self, value: int) -> None:
        self._n_error_type = value

    @property
    def aRuleIdentifier(self) -> str:
        return self._a_rule_identifier
    
    @aRuleIdentifier.setter
    def aRuleIdentifier(self, value: str) -> None:
        self._a_rule_identifier = value

    @property
    def aShortComment(self) -> str:
        return self._a_short_comment
    
    @aShortComment.setter
    def aShortComment(self, value: str) -> None:
        self._a_short_comment = value

    @property
    def aFullComment(self) -> str:
        return self._a_full_comment
    
    @aFullComment.setter
    def aFullComment(self, value: str) -> None:
        self._a_full_comment = value

    @property
    def aSuggestions(self) -> 'typing.Tuple[str, ...]':
        return self._a_suggestions
    
    @aSuggestions.setter
    def aSuggestions(self, value: 'typing.Tuple[str, ...]') -> None:
        self._a_suggestions = value

    @property
    def aProperties(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        return self._a_properties
    
    @aProperties.setter
    def aProperties(self, value: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        self._a_properties = value


__all__ = ['SingleProofreadingError']
