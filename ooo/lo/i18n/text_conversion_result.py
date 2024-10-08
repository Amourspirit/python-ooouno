# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.i18n
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .boundary import Boundary as Boundary_7fe2098c


class TextConversionResult(object):
    """
    Struct Class

    Text conversion result to be used with XTextConversion.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TextConversionResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1TextConversionResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.TextConversionResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.TextConversionResult'
    """Literal Constant ``com.sun.star.i18n.TextConversionResult``"""

    def __init__(self, Boundary: typing.Optional[Boundary_7fe2098c] = UNO_NONE, Candidates: typing.Optional[typing.Tuple[str, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Boundary (Boundary, optional): Boundary value.
            Candidates (typing.Tuple[str, ...], optional): Candidates value.
        """
        super().__init__()

        if isinstance(Boundary, TextConversionResult):
            oth: TextConversionResult = Boundary
            self.Boundary = oth.Boundary
            self.Candidates = oth.Candidates
            return

        kargs = {
            "Boundary": Boundary,
            "Candidates": Candidates,
        }
        if kargs["Boundary"] is UNO_NONE:
            kargs["Boundary"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._boundary = kwargs["Boundary"]
        self._candidates = kwargs["Candidates"]


    @property
    def Boundary(self) -> Boundary_7fe2098c:
        """
        The boundary of the first convertible word in the given text.
        
        If there is no convertible word found in the text, startPos and endPos for Boundary equal 0.
        """
        return self._boundary

    @Boundary.setter
    def Boundary(self, value: Boundary_7fe2098c) -> None:
        self._boundary = value

    @property
    def Candidates(self) -> typing.Tuple[str, ...]:
        """
        A list of replacement candidates for the first convertible word found in the given text.
        """
        return self._candidates

    @Candidates.setter
    def Candidates(self, value: typing.Tuple[str, ...]) -> None:
        self._candidates = value


__all__ = ['TextConversionResult']
