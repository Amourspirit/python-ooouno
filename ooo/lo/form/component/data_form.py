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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.component
from __future__ import annotations
import typing
from abc import abstractproperty
from ..x_database_parameter_broadcaster import XDatabaseParameterBroadcaster as XDatabaseParameterBroadcaster_ac7f1234
from ..x_loadable import XLoadable as XLoadable_8e680a28
from ..x_reset import XReset as XReset_71670917
from .form import Form as Form_ca1d0c51
from ...sdb.row_set import RowSet as RowSet_67d208a5
if typing.TYPE_CHECKING:
    from com.sun.star.form.TabulatorCycle import TabulatorCycleProto
    from com.sun.star.form.NavigationBarMode import NavigationBarModeProto

class DataForm(Form_ca1d0c51, RowSet_67d208a5, XDatabaseParameterBroadcaster_ac7f1234, XLoadable_8e680a28, XReset_71670917):
    """
    Service Class

    This service specifies a form which is connected to a database and displays the results of SQL queries.
    
    It provides the possibility of adding new data records, modifying existing ones, or deleting them.
    
    A database form is a special kind of enhanced database row set which provides all information for displaying the data and has more possibilities for configuring the data manipulation.

    See Also:
        `API DataForm <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1DataForm.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.DataForm'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DetailFields(self) -> typing.Tuple[str, ...]:
        """
        is used for subforms and contains the names of the columns of the subform which are related to the master fields of the parent form.
        
        Entries in this sequence can either denote column names in the sub form, or parameter names.For instance, you could base the form on the SQL statement SELECT * FROM invoices WHERE cust_ref = :cid, and add cid to the DetailFields property. In this case, the parameter will be filled from the corresponding master field.Alternatively, you could simply base your form on the table invoices, and add the column name cust_ref to the DetailFields. In this case, and implicit filter clause WHERE cust_ref = :<new_param_name> will be created, and the artificial parameter will be filled from the corresponding master field.If a string in this property denotes both a column name and a parameter name, it is undefined which way it is interpreted, but implementations of the service are required to either decide for the parameter or the column, and proceed as usual.
        
        The columns specified herein typically represent a part of the primary key fields or their aliases of the detail form.
        
        If the form is no sub form (e.g. its parent is not a form itself), this property is not evaluated.
        """
        ...

    @abstractproperty
    def MasterFields(self) -> typing.Tuple[str, ...]:
        """
        is used for subforms and contains the names of columns of the parent form.
        
        These columns are typically the foreign key fields of the parent form. The values of these columns are used to identify the data for the subform. Each time the parent form changes its current row, the subform requeries it's data based on the values of the master fields.
        
        If the form is no sub form (e.g. its parent is not a form itself), this property is not evaluated.
        """
        ...

    @abstractproperty
    def AllowDeletes(self) -> bool:
        """
        determines if deletions of records of the form are allowed.
        
        Note that this is a recommendation for user interface components displaying the form. Form implementations may decide to allow for deletions done via the API, even if the property is set to FALSE, but the user interface should respect the property value.
        """
        ...

    @abstractproperty
    def AllowInserts(self) -> bool:
        """
        determines if insertions into the form's row set are allowed.
        
        Note that this is a recommendation for user interface components displaying the form. Form implementations may decide to allow for insertions done via the API, even if the property is set to FALSE, but the user interface should respect the property value.
        """
        ...

    @abstractproperty
    def AllowUpdates(self) -> bool:
        """
        determines if modifications of the current record of the form are allowed.
        
        Note that this is a recommendation for user interface components displaying the form. Form implementations may decide to allow for updates done via the API, even if the property is set to FALSE, but the user interface should respect the property value.
        """
        ...

    @abstractproperty
    def Cycle(self) -> TabulatorCycleProto:
        """
        returns the kind of tabulator controlling.
        """
        ...

    @abstractproperty
    def NavigationBarMode(self) -> NavigationBarModeProto:
        """
        determines how a navigation bar for this form should act.
        """
        ...


__all__ = ['DataForm']

