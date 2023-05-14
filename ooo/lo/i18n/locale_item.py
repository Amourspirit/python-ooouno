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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.i18n


class LocaleItem(object):
    """
    Const Class

    These are not used with the API but with an OOo internal wrapper class that caches the contents of an instance of LocaleDataItem and uses these values to access it's members for faster access.
    
    Whenever locale data items were added these values and the wrapper class would have to be adjusted to give the application an easier access.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API LocaleItem <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1LocaleItem.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.LocaleItem'
    __ooo_type_name__: str = 'const'

    DATE_SEPARATOR = 0
    THOUSAND_SEPARATOR = 1
    DECIMAL_SEPARATOR = 2
    TIME_SEPARATOR = 3
    TIME_100SEC_SEPARATOR = 4
    LIST_SEPARATOR = 5
    SINGLE_QUOTATION_START = 6
    SINGLE_QUOTATION_END = 7
    DOUBLE_QUOTATION_START = 8
    DOUBLE_QUOTATION_END = 9
    MEASUREMENT_SYSTEM = 10
    TIME_AM = 11
    TIME_PM = 12
    LONG_DATE_DAY_OF_WEEK_SEPARATOR = 13
    LONG_DATE_DAY_SEPARATOR = 14
    LONG_DATE_MONTH_SEPARATOR = 15
    LONG_DATE_YEAR_SEPARATOR = 16
    COUNT = 17
    """
    count of items available
    """
    DECIMAL_SEPARATOR_ALTERNATIVE = 17
    COUNT2 = 18
    """
    count of items available
    """

__all__ = ['LocaleItem']
