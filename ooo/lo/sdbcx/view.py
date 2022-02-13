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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbcx
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_alter_view import XAlterView as XAlterView_a42a0b07
from .x_rename import XRename as XRename_848c09cc

class View(XPropertySet_bc180bfa, XAlterView_a42a0b07, XRename_848c09cc):
    """
    Service Class

    is used to specify views on data.
    
    A view object is only used for creation and deletion. Inspecting the command of a view is normally not supported.
    
    If a view is going to be added to a database, the view must have a unique name within the view and the table container, as it can be used like a table.  Note:  After addition, both the containers for views and the container for tables must contain an element for the view.

    See Also:
        `API View <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1View.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.View'
    __ooo_type_name__: str = 'service'



__all__ = ['View']

