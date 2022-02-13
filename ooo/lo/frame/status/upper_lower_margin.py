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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class UpperLowerMargin(object):
    """
    Struct Class

    specifies an upper and lower margin.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UpperLowerMargin <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1UpperLowerMargin.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.UpperLowerMargin'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.UpperLowerMargin'
    """Literal Constant ``com.sun.star.frame.status.UpperLowerMargin``"""

    def __init__(self, Upper: int = 0, Lower: int = 0) -> None:
        """
        Constructor

        Other Arguments:
            ``Upper`` can be another ``UpperLowerMargin`` instance,
                in which case other named args are ignored.

        Arguments:
            Upper (int, optional): Upper value
            Lower (int, optional): Lower value
        """
        if isinstance(Upper, UpperLowerMargin):
            oth: UpperLowerMargin = Upper
            self._upper = oth.Upper
            self._lower = oth.Lower
            return
        else:
            self._upper = Upper
            self._lower = Lower



    @property
    def Upper(self) -> int:
        """
        specifies a upper margin in 1/100th mm.
        """
        return self._upper
    
    @Upper.setter
    def Upper(self, value: int) -> None:
        self._upper = value

    @property
    def Lower(self) -> int:
        """
        specifies a lower margin in 1/100th mm.
        """
        return self._lower
    
    @Lower.setter
    def Lower(self, value: int) -> None:
        self._lower = value


__all__ = ['UpperLowerMargin']
