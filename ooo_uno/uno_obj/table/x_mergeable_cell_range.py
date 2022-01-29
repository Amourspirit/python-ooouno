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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.table
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XMergeableCellRange(XInterface_8f010a43):
    """
    represents a range of cells that can possibly be merged or unmerged.

    See Also:
        `API XMergeableCellRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XMergeableCellRange.html>`_
    """

    @abstractmethod
    def isMergeable(self) -> bool:
        """
        """
    @abstractmethod
    def merge(self) -> None:
        """
        merges the area specified by this range.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    @abstractmethod
    def split(self, Columns: int, Rows: int) -> None:
        """
        splits the cells in this range.
        
        This will be done by inserting rows and columns if needed or unmerging cells that are already split.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XMergeableCellRange']

