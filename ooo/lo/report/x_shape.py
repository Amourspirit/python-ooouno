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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.report
import typing
from abc import abstractproperty
from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
from .x_report_control_model import XReportControlModel as XReportControlModel_2d800f4a
if typing.TYPE_CHECKING:
    from ..drawing.homogen_matrix3 import HomogenMatrix3 as HomogenMatrix3_f0fb0d69

class XShape(XReportControlModel_2d800f4a):
    """

    See Also:
        `API XShape <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XShape'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XShape'

    CustomShapeGeometry: typing.TypeAlias = typing.Tuple[PropertyValue_c9610c73, ...]
    """
    This property describes the geometry of the CustomShape.
    
    The CustomShapeEngine that is used should be able to get on with the content of this property.
    
    If the CustomShapeEngine property is \"com.sun.star.drawing.EnhancedCustomShapeEngine\", then this property is containing properties as they are specified in the service com.sun.star.drawing.EnhancedCustomShapeGeometry
    """

    @abstractproperty
    def CustomShapeData(self) -> str:
        """
        This property can be used to store data that the CustomShapeEngine may use for rendering.
        """
    @abstractproperty
    def CustomShapeEngine(self) -> str:
        """
        This property contains the CustomShapeEngine service name that has to be used for rendering.
        """
    @abstractproperty
    def Opaque(self) -> bool:
        """
        determines if the object is opaque or transparent for text.
        """
    @abstractproperty
    def Transformation(self) -> 'HomogenMatrix3_f0fb0d69':
        """
        this property lets you get and set the transformation matrix for this shape.
        
        The transformation is a 3x3 homogeneous matrix and can contain translation, rotation, shearing and scaling.
        """
    @abstractproperty
    def ZOrder(self) -> int:
        """
        is used to query or change the ZOrder of this Shape.
        """


__all__ = ['XShape']

