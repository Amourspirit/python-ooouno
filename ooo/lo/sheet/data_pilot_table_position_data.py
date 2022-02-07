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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2


class DataPilotTablePositionData(object):
    """
    Struct Class

    This structure contains information on a cell within a DataPilot table.
    
    This structure contains information on a particular cell within a DataPilot table, and is used to retrieve its metadata. The PositionType member specifies in which sub-area of the table the cell is positioned, which in turn determines the type of metadata contained in the PositionData member.
    
    **since**
    
        OOo 3.0

    See Also:
        `API DataPilotTablePositionData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotTablePositionData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotTablePositionData'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DataPilotTablePositionData'
    """Literal Constant ``com.sun.star.sheet.DataPilotTablePositionData``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DataPilotTablePositionData`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DataPilotTablePositionData``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            PositionType (int, optional): PositionType value
            PositionData (object, optional): PositionData value
        """
        self._position_type = None
        self._position_data = None

        key_order = ('PositionType', 'PositionData')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DataPilotTablePositionData):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DataPilotTablePositionData.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def PositionType(self) -> int:
        """
        This parameter specifies which sub-area of a DataPilot table a given cell is positioned.
        
        See DataPilotTablePositionType for how to interpret the value of this parameter.
        """
        return self._position_type
    
    @PositionType.setter
    def PositionType(self, value: int) -> None:
        self._position_type = value

    @property
    def PositionData(self) -> object:
        """
        This member contains a structure of different types depending on the position type specified in PositionType member.
        
        When the value of PositionType is DataPilotTablePositionType.RESULT, DataPilotTablePositionData.PositionData contains an instance of type DataPilotTableResultData, whereas when the value of DataPilotTablePositionData.PositionType is either DataPilotTablePositionType.ROW_HEADER or DataPilotTablePositionType.COLUMN_HEADER, then the PositionData member contains an instance of type DataPilotTableHeaderData.
        """
        return self._position_data
    
    @PositionData.setter
    def PositionData(self, value: object) -> None:
        self._position_data = value


__all__ = ['DataPilotTablePositionData']
