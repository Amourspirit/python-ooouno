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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
from .native_number_xml_attributes import NativeNumberXmlAttributes as NativeNumberXmlAttributes_5e4f1070
import typing


class NativeNumberXmlAttributes2(NativeNumberXmlAttributes_5e4f1070):
    """
    Struct Class

    Attributes describing a native number mode for a specific locale, stored in XML file format.
    
    Used later with XNativeNumberSupplier2.convertToXmlAttributes() and XNativeNumberSupplier2.convertFromXmlAttributes()
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API NativeNumberXmlAttributes2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1NativeNumberXmlAttributes2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.NativeNumberXmlAttributes2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.NativeNumberXmlAttributes2'
    """Literal Constant ``com.sun.star.i18n.NativeNumberXmlAttributes2``"""

    def __init__(self, Spellout: str = '', **kwargs) -> None:
        """
        Constructor

        Other Arguments:
            ``Spellout`` can be another ``NativeNumberXmlAttributes2`` instance,
                in which case other named args are ignored.
                However ``**kwargs`` are still passed so parent class.

        Arguments:
            Spellout (str, optional): Spellout value
        """
        super().__init__(**kwargs)
        if isinstance(Spellout, NativeNumberXmlAttributes2):
            oth: NativeNumberXmlAttributes2 = Spellout
            self._spellout = oth.Spellout
            return
        else:
            self._spellout = Spellout



    @property
    def Spellout(self) -> str:
        """
        The format of the number string, for example, \"cardinal\", \"ordinal\" or \"ordinal-number\".
        """
        return self._spellout
    
    @Spellout.setter
    def Spellout(self, value: str) -> None:
        self._spellout = value


__all__ = ['NativeNumberXmlAttributes2']
