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
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from com.sun.star.chart.ChartDataRowSource import ChartDataRowSourceProto  # type: ignore

class TabularDataProviderArguments(ABC):
    """
    Service Class


    See Also:
        `API TabularDataProviderArguments <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1data_1_1TabularDataProviderArguments.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.TabularDataProviderArguments'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def CellRangeRepresentation(self) -> str:
        """
        the range address string spanning all data.
        
        The range address string must be interpretable by the component that implements XDataProvider and gets this property as argument to XDataProvider.detectArguments().
        
        The representation string is of a form that may be used in the user interface. Example for OOo Calc: \"$Sheet1.$A$1:$D$7\", example for OOo Writer: \"&lt;Table1.A1:D7&gt;\".
        
        When used as input, this range will be split in columns or rows depending on the property DataRowSource.
        
        When used as output of XDataProvider.detectArguments() this is the range that spans the ranges of all given XDataSequences. If the result is ambiguous, i.e., a splitting of this range would not yield the same result, this property should be empty. The latter is the case, when ranges are overlapping, the lengths of sequences are not equal or even if the order of two sequences is swapped (e.g. data comes from column A, C, B).
        """
        ...

    @property
    @abstractmethod
    def DataRowSource(self) -> ChartDataRowSourceProto:
        """
        determines, whether data sequences are created out of columns or rows in a table.
        
        If this property is not given as argument it is assumed to com.sun.star.chart.ChartDataRowSource.COLUMNS, i.e., the default is \"take data from columns\".
        """
        ...

    @property
    @abstractmethod
    def FirstCellAsLabel(self) -> bool:
        """
        If data comes from columns, the first row will provide the labels for all sequences, if data comes from rows, the first column will provide the labels for all sequences.
        
        Even if this property is false, the XLabeledDataSequence may contain a label, but this will not be the first cell of the selection. It may be a generic string like \"Column C\".
        
        If this property is not given as argument it is assumed to be FALSE, i.e., the default is \"no labels\".
        """
        ...

    @property
    @abstractmethod
    def HasCategories(self) -> bool:
        """
        If FALSE the data provider may create a data sequence containing generated categories that fit the rest of the data, like e.g.
        
        \"Row 12\", \"Row 13\", etc.
        
        This property is not relevant for the splitting up of the data. It just indicates, if the chart wants to use part of the data as categories, so that generic categories can be returned if it doesn't.
        
        The generic category labeled sequence returned should be the first one in the returned XDataSource. It needs no label. The values should have their role set to \"categories\". The generic strings returned should also be localized.
        """
        ...

    @property
    @abstractmethod
    def SequenceMapping(self) -> typing.Tuple[int, ...]:
        """
        determines the order of the created labeled sequences
        
        For example a SequenceMapping of [3,0,2,1] indicates that the sequence from old position \"3\" should now be the first one. Then comes the sequence from old position \"0\". Then that one from old position \"2\" and then the sequence from old position \"1\".
        
        If the SequenceMapping contains invalid indexes just ignore those single indexes. For example if you only have three labeled sequences and a SequenceMapping [2,5,1,0], you should ignore the \"5\" and continue to place the sequence from old index \"1\" to the next new position and so on.
        
        If the given SequenceMapping does not cover all existing labeled sequences just put the remaining sequences in old order behind the others. For example you have 4 sequences and a SequenceMapping [3,1]. The result should be as if [3,1,0,2] was given.
        """
        ...

    @property
    @abstractmethod
    def TableNumberList(self) -> str:
        """
        This property is for providing proprietary table indexes for each table appearing in a range given in CellRangeRepresentation.
        
        This argument is supported by Spreadsheets in order to be able to export a document into the StarOffice 5.0 binary format.
        
        Example: If you have the sheets (Sheet1, Sheet2, Sheet3) in your document and a chart uses the range \"Sheet2.A1:.A5 Sheet3.A1:.A5 Sheet2.B1:.B5 Sheet1:B1:.B5\", your TableNumberList would be \"1 2 1 0\". A simple range like \"Sheet1.A1:.E4\" would have the TableNumberList in \"0\"
        
        .
        """
        ...


__all__ = ['TabularDataProviderArguments']