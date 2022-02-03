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
# Namespace: com.sun.star.util
from enum import IntFlag


class SearchFlags(object):
    """
    Const Class

    Flags for search methods.
    
    **since**
    
        LibreOffice 5.2

    See Also:
        `API SearchFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1util_1_1SearchFlags.html>`_
    """
    ALL_IGNORE_CASE = 1
    NORM_WORD_ONLY = 16
    """
    Flag for normal (Boyer-Moore) search / Search for word only.
    """
    REG_EXTENDED = 256
    """
    Flag for \"regular expression\" search / Interpret as extended regular expression.
    """
    REG_NOSUB = 512
    """
    Flag for \"regular expression\" search / No register information or backreferences, i.e., avoid sub expressions.
    
    Return only true/false if matched or not.
    """
    REG_NEWLINE = 1024
    """
    Flag for \"regular expression\" search / Special new line treatment.
    
    A NEWLINE character in string will not be matched by a period outside bracket expression or by any form of a non matching list.
    
    A circumflex (^) in pattern when used to specify expression anchoring will match the zero length string immediately after a newline in string, regardless of the setting of REG_NOT_BEGINOFLINE.
    
    A dollar-sign ($) in pattern when used to specify expression anchoring, will match zero-length string immediately before a new line in string, regardless of the setting of REG_NOT_ENDOFLINE.
    """
    REG_NOT_BEGINOFLINE = 2048
    """
    The first character in the string is not the beginning of the line therefore ^ will not match with first character of the string.
    """
    REG_NOT_ENDOFLINE = 4096
    """
    The last character in the string is not the end of the line therefore $ will not match with last character of the string.
    """
    LEV_RELAXED = 65536
    """
    Flag for \"Weighted Levenshtein Distance\" search / Relaxed checking of limit, split weigh pools.
    
    If not specified (strict), the search is successful if the WLD is within a calculated limit where each insertion, deletion and replacement adds a weight to a common pool of weights. This is the mathematically correct WLD.
    
    From a user's point of view the strict WLD is an exclusive-OR of the arguments given, for example if allowed insertions=2 and allowed replacements=2, the search fails if 2 characters had been inserted and an additional operation would be needed to match. Depending on the weights it may also fail if 1 character was inserted and 1 character replaced and an additional operation would be needed to match. The strict algorithm may match less than expected from a first glance of the specified arguments, but does not return false positives.
    
    If specified (relaxed), the search is also successful if the combined pool for insertions and deletions is below a doubled calculated limit and replacements are treated differently. Additionally, swapped characters are counted as one replacement.
    
    From a user's point of view the relaxed WLD is an inclusive-OR of the arguments given, for example if allowed insertions=2 and allowed replacements=2, the search succeeds if 2 characters had been inserted and an additional replacement is needed to match. The relaxed algorithm may return false positives, but meets user expectation better.
    """
    WILD_MATCH_SELECTION = 1048576
    """
    Flag for wildcards search if entire selection must match the pattern.
    
    If com.sun.star.util.SearchOptions2.AlgorithmType2 is com.sun.star.util.SearchAlgorithms2.WILDCARD specifies whether a wildcard pattern must match the entire selected range of the string from start position to end position or a substring match is allowed.
    
    If set, the entire selection must match. If not set, a substring match is allowed.
    
    **since**
    
        LibreOffice 5.2
    """


class SearchFlagsEnum(IntFlag):
    """
    Enum of Const Class SearchFlags

    Flags for search methods.
    
    **since**
    
        LibreOffice 5.2
    """
    ALL_IGNORE_CASE = SearchFlags.ALL_IGNORE_CASE
    NORM_WORD_ONLY = SearchFlags.NORM_WORD_ONLY
    """
    Flag for normal (Boyer-Moore) search / Search for word only.
    """
    REG_EXTENDED = SearchFlags.REG_EXTENDED
    """
    Flag for \"regular expression\" search / Interpret as extended regular expression.
    """
    REG_NOSUB = SearchFlags.REG_NOSUB
    """
    Flag for \"regular expression\" search / No register information or backreferences, i.e., avoid sub expressions.
    
    Return only true/false if matched or not.
    """
    REG_NEWLINE = SearchFlags.REG_NEWLINE
    """
    Flag for \"regular expression\" search / Special new line treatment.
    
    A NEWLINE character in string will not be matched by a period outside bracket expression or by any form of a non matching list.
    
    A circumflex (^) in pattern when used to specify expression anchoring will match the zero length string immediately after a newline in string, regardless of the setting of REG_NOT_BEGINOFLINE.
    
    A dollar-sign ($) in pattern when used to specify expression anchoring, will match zero-length string immediately before a new line in string, regardless of the setting of REG_NOT_ENDOFLINE.
    """
    REG_NOT_BEGINOFLINE = SearchFlags.REG_NOT_BEGINOFLINE
    """
    The first character in the string is not the beginning of the line therefore ^ will not match with first character of the string.
    """
    REG_NOT_ENDOFLINE = SearchFlags.REG_NOT_ENDOFLINE
    """
    The last character in the string is not the end of the line therefore $ will not match with last character of the string.
    """
    LEV_RELAXED = SearchFlags.LEV_RELAXED
    """
    Flag for \"Weighted Levenshtein Distance\" search / Relaxed checking of limit, split weigh pools.
    
    If not specified (strict), the search is successful if the WLD is within a calculated limit where each insertion, deletion and replacement adds a weight to a common pool of weights. This is the mathematically correct WLD.
    
    From a user's point of view the strict WLD is an exclusive-OR of the arguments given, for example if allowed insertions=2 and allowed replacements=2, the search fails if 2 characters had been inserted and an additional operation would be needed to match. Depending on the weights it may also fail if 1 character was inserted and 1 character replaced and an additional operation would be needed to match. The strict algorithm may match less than expected from a first glance of the specified arguments, but does not return false positives.
    
    If specified (relaxed), the search is also successful if the combined pool for insertions and deletions is below a doubled calculated limit and replacements are treated differently. Additionally, swapped characters are counted as one replacement.
    
    From a user's point of view the relaxed WLD is an inclusive-OR of the arguments given, for example if allowed insertions=2 and allowed replacements=2, the search succeeds if 2 characters had been inserted and an additional replacement is needed to match. The relaxed algorithm may return false positives, but meets user expectation better.
    """
    WILD_MATCH_SELECTION = SearchFlags.WILD_MATCH_SELECTION
    """
    Flag for wildcards search if entire selection must match the pattern.
    
    If com.sun.star.util.SearchOptions2.AlgorithmType2 is com.sun.star.util.SearchAlgorithms2.WILDCARD specifies whether a wildcard pattern must match the entire selected range of the string from start position to end position or a substring match is allowed.
    
    If set, the entire selection must match. If not set, a substring match is allowed.
    
    **since**
    
        LibreOffice 5.2
    """

__all__ = ['SearchFlags', 'SearchFlagsEnum']
