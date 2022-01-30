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
# Namespace: com.sun.star.chart
# Libre Office Version: 7.2
import typing
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class ChartSeriesAddress(object):
        """
        Struct Class

        This structure describes a single data row, specified by its name and a sequence of data points.
        
        The cell addresses are in the format of the application that contains this chart.

        See Also:
            `API ChartSeriesAddress <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartSeriesAddress.html>`_


        Note:
            | At runtime ChartSeriesAddress will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | ChartSeriesAddress is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, DataRangeAddress: typing.Optional[str] = None, DomainRangeAddresses: 'typing.Optional[typing.List[str]]' = None, LabelAddress: typing.Optional[str] = None):
            self._data_range_address = DataRangeAddress
            self._domain_range_addresses = DomainRangeAddresses
            self._label_address = LabelAddress

        @property
        def DataRangeAddress(self) -> str:
            """
            contains the cell range address of the data for this series.
            """
            return self._data_range_address
        
        @DataRangeAddress.setter
        def DataRangeAddress(self, value: str) -> None:
            self._data_range_address = value

        @property
        def DomainRangeAddresses(self) -> 'typing.List[str]':
            """
            contains cell addresses for each domain of this series.
            
            For XY (scatter) diagrams at least one series has a domain. Most of the other chart types use an empty sequence here.
            """
            return self._domain_range_addresses
        
        @DomainRangeAddresses.setter
        def DomainRangeAddresses(self, value: 'typing.List[str]') -> None:
            self._domain_range_addresses = value

        @property
        def LabelAddress(self) -> str:
            """
            contains the cell address of label (i.e.
            
            name) of this series.
            """
            return self._label_address
        
        @LabelAddress.setter
        def LabelAddress(self, value: str) -> None:
            self._label_address = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global ChartSeriesAddress
        order = ('DataRangeAddress', 'DomainRangeAddresses', 'LabelAddress')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.chart.ChartSeriesAddress')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        ChartSeriesAddress = _struct_init

    _dynamic_struct()

__all__ = ['ChartSeriesAddress']
