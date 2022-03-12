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
from ooo.oenv import UNO_NONE
import typing


class TimeIncrement(object):
    """
    Struct Class

    A TimeIncrement describes how tickmarks are positioned on the scale of a date-time axis.
    
    **since**
    
        OOo 3.4

    See Also:
        `API TimeIncrement <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1TimeIncrement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.TimeIncrement'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart.TimeIncrement'
    """Literal Constant ``com.sun.star.chart.TimeIncrement``"""

    def __init__(self, MajorTimeInterval: typing.Optional[object] = None, MinorTimeInterval: typing.Optional[object] = None, TimeResolution: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            MajorTimeInterval (object, optional): MajorTimeInterval value.
            MinorTimeInterval (object, optional): MinorTimeInterval value.
            TimeResolution (object, optional): TimeResolution value.
        """
        super().__init__()
        kargs = {
            "MajorTimeInterval": MajorTimeInterval,
            "MinorTimeInterval": MinorTimeInterval,
            "TimeResolution": TimeResolution,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._major_time_interval = kwargs["MajorTimeInterval"]
        self._minor_time_interval = kwargs["MinorTimeInterval"]
        self._time_resolution = kwargs["TimeResolution"]


    @property
    def MajorTimeInterval(self) -> object:
        """
        if the any contains a struct of type com.sun.star.chart.TimeInterval this is used as a fixed distance value for the major tickmarks.
        
        Otherwise, if the any is empty or contains an incompatible type, the distance between major tickmarks is calculated automatically by the application.
        """
        return self._major_time_interval
    
    @MajorTimeInterval.setter
    def MajorTimeInterval(self, value: object) -> None:
        self._major_time_interval = value

    @property
    def MinorTimeInterval(self) -> object:
        """
        if the any contains a struct of type com.sun.star.chart.TimeInterval this is used as a fixed distance value for the minor tickmarks.
        
        Otherwise, if the any is empty or contains an incompatible type, the distance between minor tickmarks is calculated automatically by the application.
        """
        return self._minor_time_interval
    
    @MinorTimeInterval.setter
    def MinorTimeInterval(self, value: object) -> None:
        self._minor_time_interval = value

    @property
    def TimeResolution(self) -> object:
        """
        if the any contains a constant of type com.sun.star.chart.TimeUnit this is the smallest time unit that is displayed on the date-time axis.
        
        Otherwise, if the any is empty or contains an incompatible type, the resolution is chosen automatically by the application.
        """
        return self._time_resolution
    
    @TimeResolution.setter
    def TimeResolution(self, value: object) -> None:
        self._time_resolution = value


__all__ = ['TimeIncrement']
