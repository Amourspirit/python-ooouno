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
# Namespace: com.sun.star.drawing
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from com.sun.star.drawing.ConnectorType import ConnectorTypeProto  # type: ignore

class ConnectorProperties(ABC):
    """
    Service Class

    This is a set of properties to describe the style for rendering connector.
    
    **since**
    
        LibreOffice 24.2

    See Also:
        `API ConnectorProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1ConnectorProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.ConnectorProperties'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def EdgeKind(self) -> ConnectorTypeProto:
        """
        This property contains the kind of the connector.
        """
        ...

    @property
    @abstractmethod
    def EdgeNode1HorzDist(self) -> int:
        """
        This property contains the horizontal distance of node 1.
        """
        ...

    @property
    @abstractmethod
    def EdgeNode1VertDist(self) -> int:
        """
        This property contains the vertical distance of node 1.
        """
        ...

    @property
    @abstractmethod
    def EdgeNode2HorzDist(self) -> int:
        """
        This property contains the horizontal distance of node 2.
        """
        ...

    @property
    @abstractmethod
    def EdgeNode2VertDist(self) -> int:
        """
        This property contains the vertical distance of node 2.
        """
        ...

    @property
    @abstractmethod
    def EdgeOOXMLCurve(self) -> bool:
        """
        If 'TRUE' a curved connector is routed compatible to OOXML.
        
        The default value for new connectors is 'FALSE'. The property is only evaluated in case EdgeKind CURVE.
        
        **since**
        
            LibreOffice 24.2
        """
        ...


__all__ = ['ConnectorProperties']