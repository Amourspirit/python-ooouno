# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..lang.locale import Locale as Locale_70d308fa


class NativeNumberXmlAttributes(object):
    """
    Struct Class

    Attributes describing a native number mode for a specific locale, stored in XML file format.
    
    Used with XNativeNumberSupplier.convertToXmlAttributes() and XNativeNumberSupplier.convertFromXmlAttributes()
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API NativeNumberXmlAttributes <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1NativeNumberXmlAttributes.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.NativeNumberXmlAttributes'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.NativeNumberXmlAttributes'
    """Literal Constant ``com.sun.star.i18n.NativeNumberXmlAttributes``"""

    def __init__(self, Locale: typing.Optional[Locale_70d308fa] = UNO_NONE, Format: typing.Optional[str] = '', Style: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Locale (Locale, optional): Locale value.
            Format (str, optional): Format value.
            Style (str, optional): Style value.
        """
        super().__init__()

        if isinstance(Locale, NativeNumberXmlAttributes):
            oth: NativeNumberXmlAttributes = Locale
            self.Locale = oth.Locale
            self.Format = oth.Format
            self.Style = oth.Style
            return

        kargs = {
            "Locale": Locale,
            "Format": Format,
            "Style": Style,
        }
        if kargs["Locale"] is UNO_NONE:
            kargs["Locale"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._locale = kwargs["Locale"]
        self._format = kwargs["Format"]
        self._style = kwargs["Style"]


    @property
    def Locale(self) -> Locale_70d308fa:
        """
        The locale of the native number representation.
        """
        return self._locale

    @Locale.setter
    def Locale(self, value: Locale_70d308fa) -> None:
        self._locale = value

    @property
    def Format(self) -> str:
        """
        The number \"1\" expressed as a native number string.
        """
        return self._format

    @Format.setter
    def Format(self, value: str) -> None:
        self._format = value

    @property
    def Style(self) -> str:
        """
        The type of the number string, for example, \"short\" or \"medium\" or \"long\".
        """
        return self._style

    @Style.setter
    def Style(self, value: str) -> None:
        self._style = value


__all__ = ['NativeNumberXmlAttributes']
