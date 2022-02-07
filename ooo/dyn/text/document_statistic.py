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
# Namespace: com.sun.star.text
from enum import IntEnum
from ...lo.text.document_statistic import DocumentStatistic as DocumentStatistic


class DocumentStatisticEnum(IntEnum):
    """
    Enum of Const Class DocumentStatistic

    These constants are used to specify the type of a document statistic field.
    """
    PAGES = DocumentStatistic.PAGES
    PARAS = DocumentStatistic.PARAS
    WORDS = DocumentStatistic.WORDS
    CHARS = DocumentStatistic.CHARS

__all__ = ['DocumentStatistic', 'DocumentStatisticEnum']
