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
# Namespace: com.sun.star.form
import typing
from abc import abstractmethod
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XInsertListener(XEventListener_c7230c4a):
    """
    allows to receive notifications about insertions into a database form.
    
    Please do not use anymore, this interface is deprecated, and superseded by functionality from the com.sun.star.form.component.DataForm service, as well as the com.sun.star.sdbc.XRowSetListener and com.sun.star.sdb.XRowSetApproveListener interfaces.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XInsertListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XInsertListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.XInsertListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.XInsertListener'

    @abstractmethod
    def inserted(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is invoked after a database form has inserted a record to a data source.
        """
    @abstractmethod
    def inserting(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is invoked when a database form starts inserting a record.
        """


__all__ = ['XInsertListener']

