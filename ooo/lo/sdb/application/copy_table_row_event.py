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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sdb.application
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing
from ...sdbc.x_result_set import XResultSet as XResultSet_98e30aa7


class CopyTableRowEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an event happening while copying table data between databases.
    
    Whenever this event is fired to an XCopyTableListener, com.sun.star.lang.EventObject.Source contains the wizard instance which actually does the copying.

    See Also:
        `API CopyTableRowEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1application_1_1CopyTableRowEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.application'
    __ooo_full_ns__: str = 'com.sun.star.sdb.application.CopyTableRowEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sdb.application.CopyTableRowEvent'
    """Literal Constant ``com.sun.star.sdb.application.CopyTableRowEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, SourceData: typing.Optional[XResultSet_98e30aa7] = None, Error: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            SourceData (XResultSet, optional): SourceData value.
            Error (object, optional): Error value.
        """

        if isinstance(Source, CopyTableRowEvent):
            oth: CopyTableRowEvent = Source
            self.Source = oth.Source
            self.SourceData = oth.SourceData
            self.Error = oth.Error
            return

        kargs = {
            "Source": Source,
            "SourceData": SourceData,
            "Error": Error,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._source_data = kwargs["SourceData"]
        self._error = kwargs["Error"]
        inst_keys = ('SourceData', 'Error')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def SourceData(self) -> XResultSet_98e30aa7:
        """
        contains the result set which is being copied by the wizard currently.
        """
        return self._source_data

    @SourceData.setter
    def SourceData(self, value: XResultSet_98e30aa7) -> None:
        self._source_data = value

    @property
    def Error(self) -> object:
        """
        denotes the error which happened while copying the data.
        
        Usually, this contains an instance of com.sun.star.sdbc.SQLException.
        """
        return self._error

    @Error.setter
    def Error(self, value: object) -> None:
        self._error = value


__all__ = ['CopyTableRowEvent']
