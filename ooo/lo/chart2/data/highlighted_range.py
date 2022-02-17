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
# Namespace: com.sun.star.chart2.data
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class HighlightedRange(object):
    """
    Struct Class


    See Also:
        `API HighlightedRange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1data_1_1HighlightedRange.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.HighlightedRange'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart2.data.HighlightedRange'
    """Literal Constant ``com.sun.star.chart2.data.HighlightedRange``"""

    def __init__(self, RangeRepresentation: str = '', Index: int = 0, PreferredColor: int = 0, AllowMerginigWithOtherRanges: bool = False) -> None:
        """
        Constructor

        Other Arguments:
            ``RangeRepresentation`` can be another ``HighlightedRange`` instance,
                in which case other named args are ignored.

        Arguments:
            RangeRepresentation (str, optional): RangeRepresentation value
            Index (int, optional): Index value
            PreferredColor (int, optional): PreferredColor value
            AllowMerginigWithOtherRanges (bool, optional): AllowMerginigWithOtherRanges value
        """
        if isinstance(RangeRepresentation, HighlightedRange):
            oth: HighlightedRange = RangeRepresentation
            self._range_representation = oth.RangeRepresentation
            self._index = oth.Index
            self._preferred_color = oth.PreferredColor
            self._allow_merginig_with_other_ranges = oth.AllowMerginigWithOtherRanges
            return
        else:
            self._range_representation = RangeRepresentation
            self._index = Index
            self._preferred_color = PreferredColor
            self._allow_merginig_with_other_ranges = AllowMerginigWithOtherRanges



    @property
    def RangeRepresentation(self) -> str:
        """
        The range representation string of the highlighted range.
        """
        return self._range_representation
    
    @RangeRepresentation.setter
    def RangeRepresentation(self, value: str) -> None:
        self._range_representation = value

    @property
    def Index(self) -> int:
        """
        Only take the cell at position Index out of the given Range.
        
        If this value is -1 take the whole sequence.
        """
        return self._index
    
    @Index.setter
    def Index(self, value: int) -> None:
        self._index = value

    @property
    def PreferredColor(self) -> int:
        """
        Use this color for marking the range.
        
        This color may be ignored and replaced by a better fitting color, if it would be otherwise not well visible.
        """
        return self._preferred_color
    
    @PreferredColor.setter
    def PreferredColor(self, value: int) -> None:
        self._preferred_color = value

    @property
    def AllowMerginigWithOtherRanges(self) -> bool:
        """
        If the highlighted range is visually highlighted and this member is TRUE, the range given in RangeRepresentation may be included in a merged range rectangle spanning a bigger range.
        """
        return self._allow_merginig_with_other_ranges
    
    @AllowMerginigWithOtherRanges.setter
    def AllowMerginigWithOtherRanges(self, value: bool) -> None:
        self._allow_merginig_with_other_ranges = value


__all__ = ['HighlightedRange']