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
# Namespace: com.sun.star.text
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..container.x_string_key_map import XStringKeyMap as XStringKeyMap_ffc60de1


class TextMarkupDescriptor(object):
    """
    Struct Class

    A descriptor for a single text markup.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API TextMarkupDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextMarkupDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.TextMarkupDescriptor'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.text.TextMarkupDescriptor'
    """Literal Constant ``com.sun.star.text.TextMarkupDescriptor``"""

    def __init__(self, nType: typing.Optional[int] = 0, aIdentifier: typing.Optional[str] = '', nOffset: typing.Optional[int] = 0, nLength: typing.Optional[int] = 0, xMarkupInfoContainer: typing.Optional[XStringKeyMap_ffc60de1] = None) -> None:
        """
        Constructor

        Arguments:
            nType (int, optional): nType value.
            aIdentifier (str, optional): aIdentifier value.
            nOffset (int, optional): nOffset value.
            nLength (int, optional): nLength value.
            xMarkupInfoContainer (XStringKeyMap, optional): xMarkupInfoContainer value.
        """
        super().__init__()

        if isinstance(nType, TextMarkupDescriptor):
            oth: TextMarkupDescriptor = nType
            self.nType = oth.nType
            self.aIdentifier = oth.aIdentifier
            self.nOffset = oth.nOffset
            self.nLength = oth.nLength
            self.xMarkupInfoContainer = oth.xMarkupInfoContainer
            return

        kargs = {
            "nType": nType,
            "aIdentifier": aIdentifier,
            "nOffset": nOffset,
            "nLength": nLength,
            "xMarkupInfoContainer": xMarkupInfoContainer,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._n_type = kwargs["nType"]
        self._a_identifier = kwargs["aIdentifier"]
        self._n_offset = kwargs["nOffset"]
        self._n_length = kwargs["nLength"]
        self._x_markup_info_container = kwargs["xMarkupInfoContainer"]


    @property
    def nType(self) -> int:
        """
        Type of text markup see TextMarkupType.
        """
        return self._n_type

    @nType.setter
    def nType(self, value: int) -> None:
        self._n_type = value

    @property
    def aIdentifier(self) -> str:
        """
        A string used to identify the caller.
        """
        return self._a_identifier

    @aIdentifier.setter
    def aIdentifier(self, value: str) -> None:
        self._a_identifier = value

    @property
    def nOffset(self) -> int:
        """
        Start of the markup range.
        """
        return self._n_offset

    @nOffset.setter
    def nOffset(self, value: int) -> None:
        self._n_offset = value

    @property
    def nLength(self) -> int:
        """
        Length of the markup range.
        """
        return self._n_length

    @nLength.setter
    def nLength(self, value: int) -> None:
        self._n_length = value

    @property
    def xMarkupInfoContainer(self) -> XStringKeyMap_ffc60de1:
        """
        contains additional information about the markup
        
        Supported properties:
        
        |
        
        **since**
        
            6.3: BOLDWAVE, BOLD | See: com::sun::star::awt::FontUnderline
        """
        return self._x_markup_info_container

    @xMarkupInfoContainer.setter
    def xMarkupInfoContainer(self, value: XStringKeyMap_ffc60de1) -> None:
        self._x_markup_info_container = value


__all__ = ['TextMarkupDescriptor']
