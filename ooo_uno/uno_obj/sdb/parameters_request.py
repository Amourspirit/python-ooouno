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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.2
import typing
from abc import abstractproperty
from ..task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
    from ..sdbc.x_connection import XConnection as XConnection_a36a0b0c

class ParametersRequest(ClassifiedInteractionRequest_9f72121b):
    """
    an error specifying the lack of parameters values
    
    Usually thrown if someone tries to execute an SQL statement containing parameters which can't be filled by the executing instance.

    See Also:
        `API ParametersRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdb_1_1ParametersRequest.html>`_
    """

    @abstractproperty
    def Connection(self) -> 'XConnection_a36a0b0c':
        """
        specifies the connection on which the statement is to be executed.
        
        Somebody handling the request could, e.g., use the connection for determining the identifier quote string, etc.
        """
    @abstractproperty
    def Parameters(self) -> 'XIndexAccess_f0910d6d':
        """
        is the list of parameters requested.
        
        The objects returned by the com.sun.star.container.XIndexAccess have to be property sets describing the respective parameter. For this, the objects have to support the service com.sun.star.sdbcx.Column.
        """

