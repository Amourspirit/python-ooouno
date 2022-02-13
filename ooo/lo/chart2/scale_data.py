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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing
from ..chart.time_increment import TimeIncrement as TimeIncrement_c7e70c4e
from .axis_orientation import AxisOrientation as AxisOrientation_ecba0d6d
from .increment_data import IncrementData as IncrementData_d2000c6b
from .x_scaling import XScaling as XScaling_97500a65
from .data.x_labeled_data_sequence import XLabeledDataSequence as XLabeledDataSequence_7e1a10c8


class ScaleData(object):
    """
    Struct Class


    See Also:
        `API ScaleData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1ScaleData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.ScaleData'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart2.ScaleData'
    """Literal Constant ``com.sun.star.chart2.ScaleData``"""

    def __init__(self, Minimum: object = None, Maximum: object = None, Origin: object = None, Orientation: AxisOrientation_ecba0d6d = AxisOrientation_ecba0d6d.MATHEMATICAL, Scaling: XScaling_97500a65 = None, Categories: XLabeledDataSequence_7e1a10c8 = None, AxisType: int = 0, AutoDateAxis: bool = False, ShiftedCategoryPosition: bool = False, IncrementData: IncrementData_d2000c6b = UNO_NONE, TimeIncrement: TimeIncrement_c7e70c4e = UNO_NONE) -> None:
        """
        Constructor

        Other Arguments:
            ``Minimum`` can be another ``ScaleData`` instance,
                in which case other named args are ignored.

        Arguments:
            Minimum (object, optional): Minimum value
            Maximum (object, optional): Maximum value
            Origin (object, optional): Origin value
            Orientation (AxisOrientation, optional): Orientation value
            Scaling (XScaling, optional): Scaling value
            Categories (XLabeledDataSequence, optional): Categories value
            AxisType (int, optional): AxisType value
            AutoDateAxis (bool, optional): AutoDateAxis value
            ShiftedCategoryPosition (bool, optional): ShiftedCategoryPosition value
            IncrementData (IncrementData, optional): IncrementData value
            TimeIncrement (TimeIncrement, optional): TimeIncrement value
        """
        if isinstance(Minimum, ScaleData):
            oth: ScaleData = Minimum
            self._minimum = oth.Minimum
            self._maximum = oth.Maximum
            self._origin = oth.Origin
            self._orientation = oth.Orientation
            self._scaling = oth.Scaling
            self._categories = oth.Categories
            self._axis_type = oth.AxisType
            self._auto_date_axis = oth.AutoDateAxis
            self._shifted_category_position = oth.ShiftedCategoryPosition
            self._increment_data = oth.IncrementData
            self._time_increment = oth.TimeIncrement
            return
        else:
            self._minimum = Minimum
            self._maximum = Maximum
            self._origin = Origin
            self._orientation = Orientation
            self._scaling = Scaling
            self._categories = Categories
            self._axis_type = AxisType
            self._auto_date_axis = AutoDateAxis
            self._shifted_category_position = ShiftedCategoryPosition
            if IncrementData is UNO_NONE:
                self._increment_data = IncrementData_d2000c6b()
            else:
                self._increment_data = IncrementData
            if TimeIncrement is UNO_NONE:
                self._time_increment = TimeIncrement_c7e70c4e()
            else:
                self._time_increment = TimeIncrement



    @property
    def Minimum(self) -> object:
        """
        if the any contains a double value this is used as a fixed maximum.
        
        Otherwise, if the any is empty or contains an incompatible type, the maximum is automatic.
        
        If the maximum is automatic, this means, each view that represents the model containing this scale, has to calculate a maximum by its own means.
        """
        return self._minimum
    
    @Minimum.setter
    def Minimum(self, value: object) -> None:
        self._minimum = value

    @property
    def Maximum(self) -> object:
        """
        if the any contains a double value this is used as a fixed minimum.
        
        Otherwise, if the any is empty or contains an incompatible type, the minimum is automatic.
        
        If the minimum is automatic, this means, each view that represents the model containing this scale, has to calculate a minimum by its own means.
        """
        return self._maximum
    
    @Maximum.setter
    def Maximum(self, value: object) -> None:
        self._maximum = value

    @property
    def Origin(self) -> object:
        """
        The Origin indicates where other axes cross this axis.
        
        If the any contains a double value that value is used. Otherwise an appropriate value has to be calculated by that instances using Origin.
        """
        return self._origin
    
    @Origin.setter
    def Origin(self, value: object) -> None:
        self._origin = value

    @property
    def Orientation(self) -> AxisOrientation_ecba0d6d:
        """
        Axis orientation (standard or reversed).
        
        If used at the Y axis in pie charts or doughnut charts, specifies the rotation direction of the pie. The value AxisOrientation.MATHEMATICAL rotates the pie counterclockwise, the value AxisOrientation.REVERSE rotates the pie clockwise.
        
        Note: Is this a good place for the axis orientation? Two axes may use the same scale, but point into two different directions.
        """
        return self._orientation
    
    @Orientation.setter
    def Orientation(self, value: AxisOrientation_ecba0d6d) -> None:
        self._orientation = value

    @property
    def Scaling(self) -> XScaling_97500a65:
        return self._scaling
    
    @Scaling.setter
    def Scaling(self, value: XScaling_97500a65) -> None:
        self._scaling = value

    @property
    def Categories(self) -> XLabeledDataSequence_7e1a10c8:
        return self._categories
    
    @Categories.setter
    def Categories(self, value: XLabeledDataSequence_7e1a10c8) -> None:
        self._categories = value

    @property
    def AxisType(self) -> int:
        """
        describes the type of the axis.
        
        It can be a real number axis or a category axis or something else. AxisType is one value out of the constant group AxisType.
        """
        return self._axis_type
    
    @AxisType.setter
    def AxisType(self, value: int) -> None:
        self._axis_type = value

    @property
    def AutoDateAxis(self) -> bool:
        """
        if true an AxisType CATEGORY is interpreted as DATE if the underlying data given in Categories are dates
        """
        return self._auto_date_axis
    
    @AutoDateAxis.setter
    def AutoDateAxis(self, value: bool) -> None:
        self._auto_date_axis = value

    @property
    def ShiftedCategoryPosition(self) -> bool:
        """
        describes whether data points on category or date axis are placed between tickmarks or not if true the maximum on the scale will be expanded for one interval
        """
        return self._shifted_category_position
    
    @ShiftedCategoryPosition.setter
    def ShiftedCategoryPosition(self, value: bool) -> None:
        self._shifted_category_position = value

    @property
    def IncrementData(self) -> IncrementData_d2000c6b:
        """
        increment data to be used for not date-time axis
        """
        return self._increment_data
    
    @IncrementData.setter
    def IncrementData(self, value: IncrementData_d2000c6b) -> None:
        self._increment_data = value

    @property
    def TimeIncrement(self) -> TimeIncrement_c7e70c4e:
        """
        increment data to be used in case of date-time axis
        """
        return self._time_increment
    
    @TimeIncrement.setter
    def TimeIncrement(self, value: TimeIncrement_c7e70c4e) -> None:
        self._time_increment = value


__all__ = ['ScaleData']
