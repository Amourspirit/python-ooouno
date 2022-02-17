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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.linguistic2
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.linguistic2 import ConversionPropertyType as ConversionPropertyType
else:
    from ...lo.linguistic2.conversion_property_type import ConversionPropertyType as ConversionPropertyType


class ConversionPropertyTypeEnum(IntEnum):
    """
    Enum of Const Class ConversionPropertyType

    specifies the property type of an entry in a conversion dictionary.
    
    **since**
    
        OOo 2.0
    """
    NOT_DEFINED = ConversionPropertyType.NOT_DEFINED
    """
    There is no property type defined or available.
    """
    OTHER = ConversionPropertyType.OTHER
    """
    Any word that does not fit into any of the other properties.
    """
    FOREIGN = ConversionPropertyType.FOREIGN
    """
    A word or term that is transliterated or used from a non-Chinese language.
    """
    FIRST_NAME = ConversionPropertyType.FIRST_NAME
    """
    The first name (given name) of a person.
    """
    LAST_NAME = ConversionPropertyType.LAST_NAME
    """
    The last name (family name) of a person.
    """
    TITLE = ConversionPropertyType.TITLE
    """
    The academic or social title of a person.
    """
    STATUS = ConversionPropertyType.STATUS
    """
    The status of a situation.
    """
    PLACE_NAME = ConversionPropertyType.PLACE_NAME
    """
    The name of a location or place.
    """
    BUSINESS = ConversionPropertyType.BUSINESS
    """
    The description of a business.
    """
    ADJECTIVE = ConversionPropertyType.ADJECTIVE
    """
    An adjective.
    """
    IDIOM = ConversionPropertyType.IDIOM
    """
    A term that is used to literally describe a circumstance.
    """
    ABBREVIATION = ConversionPropertyType.ABBREVIATION
    """
    An abbreviation.
    """
    NUMERICAL = ConversionPropertyType.NUMERICAL
    """
    A numeric word.
    """
    NOUN = ConversionPropertyType.NOUN
    """
    A noun.
    """
    VERB = ConversionPropertyType.VERB
    """
    A verb.
    """
    BRAND_NAME = ConversionPropertyType.BRAND_NAME
    """
    The name of a product or a company.
    """

__all__ = ['ConversionPropertyType', 'ConversionPropertyTypeEnum']