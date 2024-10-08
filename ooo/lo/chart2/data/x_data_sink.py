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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart2.data
from __future__ import annotations
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_labeled_data_sequence import XLabeledDataSequence as XLabeledDataSequence_7e1a10c8

class XDataSink(XInterface_8f010a43):
    """
    is a container for sequences of data.
    
    With this interface data can only be written to.
    
    If you want to be able to also read the data set here, your component must also implement XDataSource.

    See Also:
        `API XDataSink <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1data_1_1XDataSink.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.XDataSink'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.data.XDataSink'

    @abstractmethod
    def setData(self, aData: typing.Tuple[XLabeledDataSequence_7e1a10c8, ...]) -> None:
        """
        sets new data sequences.
        
        The elements set here must support the service DataSequence.
        
        If the data consist only of floating point numbers (double values), the instances set here should also support the service NumericalDataSequence.
        
        If the data consist only of strings, the instances set here should also support the service TextualDataSequence.
        
        If one of the derived services is supported by one element of the sequence, it should be available for all elements in the sequence.
        """
        ...

__all__ = ['XDataSink']

