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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_data_pilot_field import XDataPilotField as XDataPilotField_e0350cdf

class XDataPilotDataLayoutFieldSupplier(ABC):
    """
    Provides access to the DataPilotField used to layout multiple data fields.
    
    This data field can be inserted into the rows dimension or columns dimension by changing its DataPilotField.Orientation property. This interface can be used to access the data layout field before multiple data fields are inserted into the DataPilot table. It remains invisible as long as the DataPilot table contains at most one data field.

    See Also:
        `API XDataPilotDataLayoutFieldSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XDataPilotDataLayoutFieldSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XDataPilotDataLayoutFieldSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XDataPilotDataLayoutFieldSupplier'

    @abstractmethod
    def getDataLayoutField(self) -> 'XDataPilotField_e0350cdf':
        """
        Returns the DataPilotField used to layout multiple data fields.
        
        If the field does not exist yet, it will be created. It is possible to insert this field into the rows or columns dimension by changing its DataPilotField.Orientation property.
        """

__all__ = ['XDataPilotDataLayoutFieldSupplier']

