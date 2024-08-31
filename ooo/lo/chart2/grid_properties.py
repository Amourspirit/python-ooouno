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
# Namespace: com.sun.star.chart2
from __future__ import annotations
from abc import abstractmethod
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9

class GridProperties(LineProperties_f13f0da9):
    """
    Service Class

    Must be supported by all grids.

    See Also:
        `API GridProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1GridProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.GridProperties'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def Show(self) -> bool:
        """
        Determines, whether the grid should be rendered by the view.
        """
        ...


__all__ = ['GridProperties']

