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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdbc
from __future__ import annotations
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XOutParameters(XInterface_8f010a43):
    """
    is used to register Out-Parameters for stored procedures.
    
    SDBC provides a stored procedure SQL escape that allows stored procedures to be called in a standard way for all RDBMSs. This escape syntax has one form that includes a result parameter and one that does not. If used, the result parameter must be registered as an OUT parameter. The other parameters can be used for input, output, or both. Parameters are referred to sequentially, by number. The first parameter is 1.

    See Also:
        `API XOutParameters <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XOutParameters.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XOutParameters'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XOutParameters'

    @abstractmethod
    def registerNumericOutParameter(self, parameterIndex: int, sqlType: int, scale: int) -> None:
        """
        registers the OUT parameter in ordinal position parameterIndex to the SDBC type sqlType.
        
        All OUT parameters must be registered before a stored procedure is executed.
        
        The SDBC type specified by sqlType for an OUT parameter determines the type that must be used in the get method to read the value of that parameter. This version of com.sun.star.sdbc.XOutParameters.registerOutParameter() should be used when the parameter is of SDBC type com.sun.star.sdbc.DataType.NUMERIC or com.sun.star.sdbc.DataType.DECIMAL.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def registerOutParameter(self, parameterIndex: int, sqlType: int, typeName: str) -> None:
        """
        registers the designated output parameter.
        
        This version of the method com.sun.star.sdbc.XOutParameters.registerOutParameter() should be used for a user-named or REF output parameter. Examples of user-named types include: STRUCT, DISTINCT, OBJECT, and named array types.
        
        Before executing a stored procedure call, you must explicitly call com.sun.star.sdbc.XOutParameters.registerOutParameter() to register the type from com.sun.star.sdbc.DataType for each OUT parameter. For a user-named parameter the fully-qualified SQL type name of the parameter should also be given, while a REF parameter requires that the fully-qualified type name of the referenced type be given. An SDBC driver that does not need the type code and type name information may ignore it. To be portable, however, applications should always provide these values for user-named and REF parameters.
        
        Although it is intended for user-named and REF parameters, this method may be used to register a parameter of any SDBC type. If the parameter does not have a user-named or REF type, the typeName parameter is ignored.
        
        Note: When reading the value of an out parameter, you must use the getXXX method whose type XXX corresponds to the parameter's registered SQL type.

        Raises:
            SQLException: ``SQLException``
        """
        ...

__all__ = ['XOutParameters']

