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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.xsd
import typing
from abc import abstractproperty
from .x_data_type import XDataType as XDataType_83f209cb
if typing.TYPE_CHECKING:
    from ..util.time import Time as Time_604e0855

class Time(XDataType_83f209cb):
    """
    Service Class

    specifies an XSD compliant time type

    See Also:
        `API Time <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xsd_1_1Time.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xsd'
    __ooo_full_ns__: str = 'com.sun.star.xsd.Time'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def MaxExclusiveTime(self) -> 'Time_604e0855':
        """
        specifies the exclusive upper bound for the value
        """
        ...

    @abstractproperty
    def MaxInclusiveTime(self) -> 'Time_604e0855':
        """
        specifies the inclusive upper bound for the value
        """
        ...

    @abstractproperty
    def MinExclusiveTime(self) -> 'Time_604e0855':
        """
        specifies the exclusive lower bound for the value
        """
        ...

    @abstractproperty
    def MinInclusiveTime(self) -> 'Time_604e0855':
        """
        specifies the inclusive lower bound for the value
        """
        ...



__all__ = ['Time']

