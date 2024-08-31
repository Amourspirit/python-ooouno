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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.i18n


class NumberFormatIndex(object):
    """
    Const Class

    Do NOT insert any new values! Locale data number format creation must match these values! Number formatter internals must match these values!
    
    Number format indices to be passed as the index argument to XNumberFormatCode.getFormatCode() or com.sun.star.util.XNumberFormatTypes.getFormatIndex().
    
    Each locale can support up to about 5000 arbitrary format codes. But for backward compatibility reasons, each locale MUST support some predefined format codes. These predefined format codes are accessed through indices as the following, and the locale data format code definitions in i18npool/source/localedata/data/*.xml MUST have matching entries in the form
    
    <FormatElement formatindex=\"0\">
    
    (see also FormatElement.formatIndex()).
    
    The index values are also used to define the enum NfIndexTableOffset in file svtools/inc/zforlist.hxx
    
    Note: This index has nothing to do with the index key used internally by the number formatter.
    
    Date formats may have a comment of DIN/EN/ISO, meaning
    
    Some names of date format constants indicate a special behavior of those formats in StarOffice 5.2 or older. Those are:

    See Also:
        `API NumberFormatIndex <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1NumberFormatIndex.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.NumberFormatIndex'
    __ooo_type_name__: str = 'const'

    NUMBER_START = 0
    """
    Start of simple numerical formats (first format)
    """
    NUMBER_STANDARD = NUMBER_START
    """
    The \"General\" standard format formatindex=\"0\".
    """
    NUMBER_INT = NUMBER_START + 1
    """
    0 Integer number formatindex=\"1\"
    """
    NUMBER_DEC2 = NUMBER_START + 2
    """
    0.00 Decimal number with 2 decimals formatindex=\"2\"
    """
    NUMBER_1000INT = NUMBER_START + 3
    """
    #,##0 Integer number with group separator formatindex=\"3\"
    """
    NUMBER_1000DEC2 = NUMBER_START + 4
    """
    #,##0.00 Decimal number with group separator formatindex=\"4\"
    """
    NUMBER_SYSTEM = NUMBER_START + 5
    """
    #,##0.00 In SO5/Win this format was retrieved from the Regional Settings formatindex=\"5\"
    """
    NUMBER_END = NUMBER_SYSTEM
    """
    End of simple numerical formats (last format)
    """
    SCIENTIFIC_START = NUMBER_END + 1
    """
    Start of Scientific formats (first format)
    """
    SCIENTIFIC_000E000 = SCIENTIFIC_START
    """
    0.00E+000 Number in scientific notation with exponent in 3 digit placeholders formatindex=\"6\"
    """
    SCIENTIFIC_000E00 = SCIENTIFIC_START + 1
    """
    0.00E+00 Number in scientific notation with exponent in 2 digit placeholders formatindex=\"7\"
    """
    SCIENTIFIC_END = SCIENTIFIC_000E00
    """
    End of Scientific formats (last format)
    """
    PERCENT_START = SCIENTIFIC_END + 1
    """
    Start of Percent formats (first format)
    """
    PERCENT_INT = PERCENT_START
    """
    0% Percentage format, rounded to integer formatindex=\"8\"
    """
    PERCENT_DEC2 = PERCENT_START + 1
    """
    0.00% Percentage format, rounded to 2 decimals formatindex=\"9\"
    """
    PERCENT_END = PERCENT_DEC2
    """
    End of Percent formats (last format)
    """
    FRACTION_START = PERCENT_END + 1
    """
    Start of Fraction formats (first format)
    """
    FRACTION_1 = FRACTION_START
    FRACTION_2 = FRACTION_START + 1
    FRACTION_END = FRACTION_2
    """
    End of Fraction formats (last format)
    """
    CURRENCY_START = FRACTION_END + 1
    """
    Start of Currency formats (first format)
    """
    CURRENCY_1000INT = CURRENCY_START
    """
    #,##0 DM Integer currency format with group separator formatindex=\"12\"
    """
    CURRENCY_1000DEC2 = CURRENCY_START + 1
    """
    #,##0.00 DM Decimal currency format with group separator formatindex=\"13\"
    """
    CURRENCY_1000INT_RED = CURRENCY_START + 2
    """
    #,##0 DM Integer currency format with negative in red formatindex=\"14\"
    """
    CURRENCY_1000DEC2_RED = CURRENCY_START + 3
    """
    #,##0.00 DM Decimal currency format with negative in red formatindex=\"15\"
    """
    CURRENCY_1000DEC2_CCC = CURRENCY_START + 4
    """
    #,##0.00 DEM Currency in ISO-4217 abbreviation format formatindex=\"16\"
    """
    CURRENCY_1000DEC2_DASHED = CURRENCY_START + 5
    """
    #,##0.– DM Currency format with dash representing 0 in decimals formatindex=\"17\"
    """
    CURRENCY_END = CURRENCY_1000DEC2_DASHED
    """
    End of Currency formats (last format)
    """
    DATE_START = CURRENCY_END + 1
    """
    Start of Date formats (first format)
    """
    DATE_SYSTEM_SHORT = DATE_START
    """
    08.10.97 see also DATE_SYSTEM_... explanation formatindex=\"18\"
    """
    DATE_SYSTEM_LONG = DATE_START + 1
    """
    Wednesday, 8.
    
    October 1997 see also DATE_SYSTEM_... explanation formatindex=\"19\"
    """
    DATE_SYS_DDMMYY = DATE_START + 2
    """
    08.10.97 see also DATE_SYS_... explanation formatindex=\"20\"
    """
    DATE_SYS_DDMMYYYY = DATE_START + 3
    """
    08.10.1997 see also DATE_SYS_...
    
    explanation Note: When editing already existing date data this format is forced in order to always edit the full century. formatindex=\"21\"
    """
    DATE_SYS_DMMMYY = DATE_START + 4
    DATE_SYS_DMMMYYYY = DATE_START + 5
    DATE_DIN_DMMMYYYY = DATE_START + 6
    DATE_SYS_DMMMMYYYY = DATE_START + 7
    DATE_DIN_DMMMMYYYY = DATE_START + 8
    DATE_SYS_NNDMMMYY = DATE_START + 9
    """
    Wed, 8. Oct 97 see also DATE_SYS_... explanation formatindex=\"27\".
    """
    DATE_DEF_NNDDMMMYY = DATE_START + 10
    """
    Wed 08.Oct 97 see also DATE_DEF_... explanation formatindex=\"28\".
    """
    DATE_SYS_NNDMMMMYYYY = DATE_START + 11
    """
    Wed, 8. October 1997 see also DATE_SYS_... explanation formatindex=\"29\".
    """
    DATE_SYS_NNNNDMMMMYYYY = DATE_START + 12
    """
    Wednesday, 8. October 1997 formatindex=\"30\".
    """
    DATE_DIN_MMDD = DATE_START + 13
    """
    10-08 DIN/EN formatindex=\"31\"
    """
    DATE_DIN_YYMMDD = DATE_START + 14
    """
    97-10-08 DIN/EN formatindex=\"32\"
    """
    DATE_DIN_YYYYMMDD = DATE_START + 15
    """
    1997-10-08 DIN/EN/ISO formatindex=\"33\"
    """
    DATE_SYS_MMYY = DATE_START + 16
    """
    10.97 see also DATE_SYS_... explanation formatindex=\"34\"
    """
    DATE_SYS_DDMMM = DATE_START + 17
    """
    08.Oct see also DATE_SYS_... explanation formatindex=\"35\"
    """
    DATE_MMMM = DATE_START + 18
    """
    October formatindex=\"36\".
    """
    DATE_QQJJ = DATE_START + 19
    """
    4th quarter 97 formatindex=\"37\"
    """
    DATE_WW = DATE_START + 20
    """
    week of year formatindex=\"38\"
    """
    DATE_END = DATE_WW
    """
    End of Date formats (last format)
    """
    TIME_START = DATE_END + 1
    """
    Start of Time formats (first format)
    """
    TIME_HHMM = TIME_START
    """
    HH:MM Time format with hour and minute formatindex=\"39\".
    """
    TIME_HHMMSS = TIME_START + 1
    """
    HH:MM:SS Time format with hour, minute and second formatindex=\"40\".
    """
    TIME_HHMMAMPM = TIME_START + 2
    """
    HH:MM AM/PM Time format with hour, minute and morning/afternoon notation formatindex=\"41\".
    """
    TIME_HHMMSSAMPM = TIME_START + 3
    """
    HH:MM:SS AM/PM Time format with hour, minute, second and morning/afternoon notation formatindex=\"42\".
    """
    TIME_HH_MMSS = TIME_START + 4
    """
    [HH]:MM:SS Time format with amount of hours formatindex=\"43\"
    """
    TIME_MMSS00 = TIME_START + 5
    """
    MM:SS,00 Time format with second in fraction formatindex=\"44\".
    """
    TIME_HH_MMSS00 = TIME_START + 6
    """
    [HH]:MM:SS,00 Time format with amount of hours and seconds with fraction formatindex=\"45\"
    """
    TIME_END = TIME_HH_MMSS00
    """
    End of Time formats (last format)
    """
    DATETIME_START = TIME_END + 1
    """
    Start of DateTime formats (first format)
    """
    DATETIME_SYSTEM_SHORT_HHMM = DATETIME_START
    """
    08.10.97 01:23 Date/time format formatindex=\"46\"
    """
    DATETIME_SYS_DDMMYYYY_HHMMSS = DATETIME_START + 1
    """
    08.10.1997 01:23:45 Date/time format with second Note: When editing already existing date/time data this format is forced in order to always edit the full century.
    
    formatindex=\"47\"
    """
    DATETIME_END = DATETIME_SYS_DDMMYYYY_HHMMSS
    """
    End of DateTime formats (last format)
    """
    BOOLEAN = DATETIME_END + 1
    """
    BOOLEAN format.
    """
    TEXT = BOOLEAN + 1
    """
    Text format.
    """
    INDEX_TABLE_ENTRIES = TEXT + 1
    """
    count of built-in format codes.
    """

__all__ = ['NumberFormatIndex']
