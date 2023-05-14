# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_scaling import XScaling as XScaling_97500a65
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from ..util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7

class XRegressionCurveCalculator(XInterface_8f010a43):
    """

    See Also:
        `API XRegressionCurveCalculator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XRegressionCurveCalculator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XRegressionCurveCalculator'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XRegressionCurveCalculator'

    @abstractmethod
    def getCorrelationCoefficient(self) -> float:
        """
        Returns the value of the correlation coefficient for the given regression.
        
        This value is often denoted as r or R.
        
        The value of r is signed. Often r2 is used instead of r to denote a regression curve's accuracy.
        """
        ...
    @abstractmethod
    def getCurveValue(self, x: float) -> float:
        """
        calculates the value of the regression curve for x.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getCurveValues(self, min: float, max: float, nPointCount: int, xScalingX: 'XScaling_97500a65', xScalingY: 'XScaling_97500a65', bMaySkipPointsInCalculation: bool) -> 'typing.Tuple[RealPoint2D_d6e70c78, ...]':
        """
        calculate multiple points of a regression curve at once.
        
        Note that this method may optimize the output by returning less points, e.g. for a line you may get only two resulting points instead of nPointCount() points. This is only allowed if the parameter bMaySkipPointsInCalculation() is set to TRUE.
        
        It is important that a renderer takes the scalings into account. When one of these parameters is unknown, no optimization must be done.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getFormattedRepresentation(self, xNumFmtSupplier: 'XNumberFormatsSupplier_3afb0fb7', nNumberFormatKey: int, nFormulaLength: int) -> str:
        """
        Returns a representation using the given number format for formatting all numbers contained in the formula.
        
        Wrap equation to fit in nFormulaLength characters
        """
        ...
    @abstractmethod
    def getRepresentation(self) -> str:
        """
        Retrieve a string showing the regression curve's function with calculated parameters.
        """
        ...
    @abstractmethod
    def recalculateRegression(self, aXValues: 'typing.Tuple[float, ...]', aYValues: 'typing.Tuple[float, ...]') -> None:
        """
        recalculates the parameters of the internal regression curve according to the x- and y-values given.
        """
        ...
    @abstractmethod
    def setRegressionProperties(self, degree: int, forceIntercept: bool, interceptValue: float, period: int, movingType: int) -> None:
        """
        set calculation properties for curve calculation.
        """
        ...
    @abstractmethod
    def setXYNames(self, aXName: str, aYName: str) -> None:
        """
        Set the names of X and Y variables of the equation to replace \"x\" and \"f(x)\" in representation.
        """
        ...

__all__ = ['XRegressionCurveCalculator']

