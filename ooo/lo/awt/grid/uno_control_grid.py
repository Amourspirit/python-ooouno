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
# Namespace: com.sun.star.awt.grid
from ..uno_control import UnoControl as UnoControl_8f2c0a67
from .x_grid_control import XGridControl as XGridControl_df2e0ce7
from .x_grid_row_selection import XGridRowSelection as XGridRowSelection_25440ee4

class UnoControlGrid(UnoControl_8f2c0a67, XGridControl_df2e0ce7, XGridRowSelection_25440ee4):
    """
    Service Class

    A control that displays a set of tabular data.
    
    The horizontal structure of the grid is defined by the XGridColumnModel implemented in DefaultGridColumnModel The XGridColumn implemented in GridColumn describes the properties and behavior of a single column. Use the XGridColumnModel.addColumn() to add a column to the column model.
    
    All row data are stored in the XGridDataModel. Use the DefaultGridDataModel to add XGridDataModel.addRow() or remove XGridDataModel.removeRow() rows.
    
    The column and data model must be set at the UnoControlGridModel.ColumnModel and UnoControlGridModel.GridDataModel properties.
    
    If you are interested in knowing when the selection changes implement a XGridSelectionListener and add the instance with the method XGridRowSelection.addSelectionListener(). You than will be notified for any selection change.
    
    **since**
    
        OOo 3.3

    See Also:
        `API UnoControlGrid <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1grid_1_1UnoControlGrid.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.UnoControlGrid'
    __ooo_type_name__: str = 'service'



__all__ = ['UnoControlGrid']
