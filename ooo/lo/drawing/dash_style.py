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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.3
from enum import Enum


class DashStyle(Enum):
    """
    Enum Class

    

    See Also:
        `API DashStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a89f0dc2e221d6f608088093da27764d1>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.DashStyle'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.drawing.DashStyle'

    RECT = 'RECT'
    """
    the dash is a rectangle
    """
    RECTRELATIVE = 'RECTRELATIVE'
    """
    the dash is a rectangle, with the size of the dash given in relation to the length of the line
    """
    ROUND = 'ROUND'
    """
    the dash is a point
    
    the lines join with an arc
    
    the line will get a half circle as additional cap
    """
    ROUNDRELATIVE = 'ROUNDRELATIVE'
    """
    the dash is a point, with the size of the dash given in relation to the length of the line
    """

__all__ = ['DashStyle']

