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
import typing


class Currency(object):
    """
    Struct Class

    Symbols, names, and attributes of a specific currency, returned in a sequence by XLocaleData.getAllCurrencies().

    See Also:
        `API Currency <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1Currency.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.Currency'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.Currency'
    """Literal Constant ``com.sun.star.i18n.Currency``"""

    def __init__(self, ID: typing.Optional[str] = '', Symbol: typing.Optional[str] = '', BankSymbol: typing.Optional[str] = '', Name: typing.Optional[str] = '', Default: typing.Optional[bool] = False, UsedInCompatibleFormatCodes: typing.Optional[bool] = False, DecimalPlaces: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            ID (str, optional): ID value.
            Symbol (str, optional): Symbol value.
            BankSymbol (str, optional): BankSymbol value.
            Name (str, optional): Name value.
            Default (bool, optional): Default value.
            UsedInCompatibleFormatCodes (bool, optional): UsedInCompatibleFormatCodes value.
            DecimalPlaces (int, optional): DecimalPlaces value.
        """
        super().__init__()

        if isinstance(ID, Currency):
            oth: Currency = ID
            self.ID = oth.ID
            self.Symbol = oth.Symbol
            self.BankSymbol = oth.BankSymbol
            self.Name = oth.Name
            self.Default = oth.Default
            self.UsedInCompatibleFormatCodes = oth.UsedInCompatibleFormatCodes
            self.DecimalPlaces = oth.DecimalPlaces
            return

        kargs = {
            "ID": ID,
            "Symbol": Symbol,
            "BankSymbol": BankSymbol,
            "Name": Name,
            "Default": Default,
            "UsedInCompatibleFormatCodes": UsedInCompatibleFormatCodes,
            "DecimalPlaces": DecimalPlaces,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._id = kwargs["ID"]
        self._symbol = kwargs["Symbol"]
        self._bank_symbol = kwargs["BankSymbol"]
        self._name = kwargs["Name"]
        self._default = kwargs["Default"]
        self._used_in_compatible_format_codes = kwargs["UsedInCompatibleFormatCodes"]
        self._decimal_places = kwargs["DecimalPlaces"]


    @property
    def ID(self) -> str:
        """
        ISO 4217 currency code identifier, for example, EUR or USD.
        """
        return self._id
    
    @ID.setter
    def ID(self, value: str) -> None:
        self._id = value

    @property
    def Symbol(self) -> str:
        """
        Currency symbol, for example, $.
        """
        return self._symbol
    
    @Symbol.setter
    def Symbol(self, value: str) -> None:
        self._symbol = value

    @property
    def BankSymbol(self) -> str:
        """
        Currency abbreviation used by banks and in money exchange, for example, EUR or USD.
        
        This usually should be identical to the ISO 4217 currency code also used in the ID, but doesn't necessarily have to be.
        """
        return self._bank_symbol
    
    @BankSymbol.setter
    def BankSymbol(self, value: str) -> None:
        self._bank_symbol = value

    @property
    def Name(self) -> str:
        """
        Name of the currency, for example, Euro or US Dollar.
        
        Should be the localized name.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Default(self) -> bool:
        """
        If this currency is the default currency for a given locale.
        """
        return self._default
    
    @Default.setter
    def Default(self, value: bool) -> None:
        self._default = value

    @property
    def UsedInCompatibleFormatCodes(self) -> bool:
        """
        If this currency is the one used in compatible number format codes with FormatElement.formatIndex() values in the range 12..17.
        
        Those format codes are used to generate some old style currency format codes for compatibility with StarOffice5 and StarOffice4.
        """
        return self._used_in_compatible_format_codes
    
    @UsedInCompatibleFormatCodes.setter
    def UsedInCompatibleFormatCodes(self, value: bool) -> None:
        self._used_in_compatible_format_codes = value

    @property
    def DecimalPlaces(self) -> int:
        """
        The number of decimal places, for example, 2 for US Dollar or 0 for Italian Lira.
        """
        return self._decimal_places
    
    @DecimalPlaces.setter
    def DecimalPlaces(self, value: int) -> None:
        self._decimal_places = value


__all__ = ['Currency']
