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
# Namespace: com.sun.star.xsd
from enum import IntEnum
from ...lo.xsd.white_space_treatment import WhiteSpaceTreatment as WhiteSpaceTreatment


class WhiteSpaceTreatmentEnum(IntEnum):
    """
    Enum of Const Class WhiteSpaceTreatment

    specifies possibilities how to treat whitespace in strings
    """
    Preserve = WhiteSpaceTreatment.Preserve
    """
    White spaces should be preserved when processing the string.
    """
    Replace = WhiteSpaceTreatment.Replace
    """
    White spaces should be replaced with TODO when processing the string.
    """
    Collapse = WhiteSpaceTreatment.Collapse
    """
    Multiple successive white spaces should be collapsed to a single white space when processing the string.
    """

__all__ = ['WhiteSpaceTreatment', 'WhiteSpaceTreatmentEnum']
