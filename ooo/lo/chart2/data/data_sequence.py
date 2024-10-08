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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart2.data
from __future__ import annotations
import typing
from abc import abstractmethod
from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_data_sequence import XDataSequence as XDataSequence_11f00e1f
from .x_numerical_data_sequence import XNumericalDataSequence as XNumericalDataSequence_a43011bf
from .x_textual_data_sequence import XTextualDataSequence as XTextualDataSequence_82171106
from ...container.x_index_replace import XIndexReplace as XIndexReplace_feed0dd7
from ...util.x_cloneable import XCloneable as XCloneable_99d00aa3
from ...util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
if typing.TYPE_CHECKING:
    from .data_sequence_role import DataSequenceRole as DataSequenceRole_3f520f59

class DataSequence(XPropertySet_bc180bfa, XDataSequence_11f00e1f, XNumericalDataSequence_a43011bf, XTextualDataSequence_82171106, XIndexReplace_feed0dd7, XCloneable_99d00aa3, XModifyBroadcaster_fd990df0):
    """
    Service Class

    describes a container for a sequence of values.
    
    With the interface XDataSequence it is possible to transfer a complete sequence of values.
    
    With the optional com.sun.star.container.XIndexReplace it is possible to modify single elements, if the corresponding DataProvider supports modification of its values.

    See Also:
        `API DataSequence <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1data_1_1DataSequence.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.DataSequence'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def HiddenValues(self) -> typing.Tuple[int, ...]:
        """
        a sequence of indexes that identify values that are hidden in the underlying data provider.
        """
        ...

    @property
    @abstractmethod
    def IncludeHiddenCells(self) -> bool:
        """
        If set to false FALSE, values from hidden cells are not returned.
        """
        ...

    @property
    @abstractmethod
    def Role(self) -> DataSequenceRole_3f520f59:
        """
        The key (index) of the number format that this sequence should be formatted with.
        
        The key identifies a number format in an com.sun.star.util.XNumberFormats object. This object can be retrieved by the com.sun.star.util.XNumberFormatsSupplier interface supported by com.sun.star.chart.ChartDocument.
        
        The role of the series inside a data series. This may be any string. However some strings are predefined and should always be used in the same way.
        """
        ...


__all__ = ['DataSequence']

