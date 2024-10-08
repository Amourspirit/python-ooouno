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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
from .x_data_pilot_field import XDataPilotField as XDataPilotField_e0350cdf


class DataPilotFieldGroupInfo(object):
    """
    Struct Class

    contains the grouping information of a DataPilotField.

    See Also:
        `API DataPilotFieldGroupInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldGroupInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldGroupInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DataPilotFieldGroupInfo'
    """Literal Constant ``com.sun.star.sheet.DataPilotFieldGroupInfo``"""

    def __init__(self, HasAutoStart: typing.Optional[bool] = False, HasAutoEnd: typing.Optional[bool] = False, HasDateValues: typing.Optional[bool] = False, Start: typing.Optional[float] = 0.0, End: typing.Optional[float] = 0.0, Step: typing.Optional[float] = 0.0, GroupBy: typing.Optional[int] = 0, SourceField: typing.Optional[XDataPilotField_e0350cdf] = None, Groups: typing.Optional[XNameAccess_e2ab0cf6] = None) -> None:
        """
        Constructor

        Arguments:
            HasAutoStart (bool, optional): HasAutoStart value.
            HasAutoEnd (bool, optional): HasAutoEnd value.
            HasDateValues (bool, optional): HasDateValues value.
            Start (float, optional): Start value.
            End (float, optional): End value.
            Step (float, optional): Step value.
            GroupBy (int, optional): GroupBy value.
            SourceField (XDataPilotField, optional): SourceField value.
            Groups (XNameAccess, optional): Groups value.
        """
        super().__init__()

        if isinstance(HasAutoStart, DataPilotFieldGroupInfo):
            oth: DataPilotFieldGroupInfo = HasAutoStart
            self.HasAutoStart = oth.HasAutoStart
            self.HasAutoEnd = oth.HasAutoEnd
            self.HasDateValues = oth.HasDateValues
            self.Start = oth.Start
            self.End = oth.End
            self.Step = oth.Step
            self.GroupBy = oth.GroupBy
            self.SourceField = oth.SourceField
            self.Groups = oth.Groups
            return

        kargs = {
            "HasAutoStart": HasAutoStart,
            "HasAutoEnd": HasAutoEnd,
            "HasDateValues": HasDateValues,
            "Start": Start,
            "End": End,
            "Step": Step,
            "GroupBy": GroupBy,
            "SourceField": SourceField,
            "Groups": Groups,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._has_auto_start = kwargs["HasAutoStart"]
        self._has_auto_end = kwargs["HasAutoEnd"]
        self._has_date_values = kwargs["HasDateValues"]
        self._start = kwargs["Start"]
        self._end = kwargs["End"]
        self._step = kwargs["Step"]
        self._group_by = kwargs["GroupBy"]
        self._source_field = kwargs["SourceField"]
        self._groups = kwargs["Groups"]


    @property
    def HasAutoStart(self) -> bool:
        """
        specifies whether the start value for the grouping is taken automatically from the minimum of the item values.
        """
        return self._has_auto_start

    @HasAutoStart.setter
    def HasAutoStart(self, value: bool) -> None:
        self._has_auto_start = value

    @property
    def HasAutoEnd(self) -> bool:
        """
        specifies whether the end value for the grouping is taken automatically from the maximum of the item values.
        """
        return self._has_auto_end

    @HasAutoEnd.setter
    def HasAutoEnd(self, value: bool) -> None:
        self._has_auto_end = value

    @property
    def HasDateValues(self) -> bool:
        """
        specifies whether date values are grouped by ranges of days.
        """
        return self._has_date_values

    @HasDateValues.setter
    def HasDateValues(self, value: bool) -> None:
        self._has_date_values = value

    @property
    def Start(self) -> float:
        """
        specifies the start value for the grouping if HasAutoStart is set to FALSE.
        """
        return self._start

    @Start.setter
    def Start(self, value: float) -> None:
        self._start = value

    @property
    def End(self) -> float:
        """
        specifies the end value for the grouping if HasAutoEnd is set to FALSE.
        """
        return self._end

    @End.setter
    def End(self, value: float) -> None:
        self._end = value

    @property
    def Step(self) -> float:
        """
        specifies the size of the ranges for numeric or day grouping.
        
        Example: With HasAutoStart set to FALSE, Start set to 2, and Step set to 3, the first group will contain all values greater than or equal to 2 and less than 5. The second group will contain all values greater than or equal to 5 and less than 8, and so on.
        """
        return self._step

    @Step.setter
    def Step(self, value: float) -> None:
        self._step = value

    @property
    def GroupBy(self) -> int:
        """
        specifies the grouping of the date values.
        """
        return self._group_by

    @GroupBy.setter
    def GroupBy(self, value: int) -> None:
        self._group_by = value

    @property
    def SourceField(self) -> XDataPilotField_e0350cdf:
        """
        contains the source DataPilot field grouping is based on.
        
        Will be NULL if this field is not grouped or contains numeric grouping.
        """
        return self._source_field

    @SourceField.setter
    def SourceField(self, value: XDataPilotField_e0350cdf) -> None:
        self._source_field = value

    @property
    def Groups(self) -> XNameAccess_e2ab0cf6:
        """
        specifies the named groups in this field if there are some.
        
        The returned object is an instance of DataPilotFieldGroups . The collection of groups can be modified by inserting, removing, replacing, or renaming single groups or item names in the groups. When writing back this struct containing such a changed collection of groups to the DataPilotField.GroupInfo property, the modified grouping settings are applied at the DataPilot field.
        """
        return self._groups

    @Groups.setter
    def Groups(self, value: XNameAccess_e2ab0cf6) -> None:
        self._groups = value


__all__ = ['DataPilotFieldGroupInfo']
