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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ...dyn.table.accessible_cell_view import AccessibleCellView as AccessibleCellView
with suppress(ImportError):
    from ...dyn.table.accessible_table_view import AccessibleTableView as AccessibleTableView
with suppress(ImportError):
    from ...dyn.table.border_line import BorderLine as BorderLine
with suppress(ImportError):
    from ...dyn.table.border_line2 import BorderLine2 as BorderLine2
with suppress(ImportError):
    from ...dyn.table.border_line_style import BorderLineStyle as BorderLineStyle
with suppress(ImportError):
    from ...dyn.table.border_line_style import BorderLineStyleEnum as BorderLineStyleEnum
with suppress(ImportError):
    from ...dyn.table.cell import Cell as Cell
with suppress(ImportError):
    from ...dyn.table.cell_address import CellAddress as CellAddress
with suppress(ImportError):
    from ...dyn.table.cell_content_type import CellContentType as CellContentType
with suppress(ImportError):
    from ...dyn.table.cell_cursor import CellCursor as CellCursor
with suppress(ImportError):
    from ...dyn.table.cell_hori_justify import CellHoriJustify as CellHoriJustify
with suppress(ImportError):
    from ...dyn.table.cell_justify_method import CellJustifyMethod as CellJustifyMethod
with suppress(ImportError):
    from ...dyn.table.cell_justify_method import CellJustifyMethodEnum as CellJustifyMethodEnum
with suppress(ImportError):
    from ...dyn.table.cell_orientation import CellOrientation as CellOrientation
with suppress(ImportError):
    from ...dyn.table.cell_properties import CellProperties as CellProperties
with suppress(ImportError):
    from ...dyn.table.cell_range import CellRange as CellRange
with suppress(ImportError):
    from ...dyn.table.cell_range_address import CellRangeAddress as CellRangeAddress
with suppress(ImportError):
    from ...dyn.table.cell_range_list_source import CellRangeListSource as CellRangeListSource
with suppress(ImportError):
    from ...dyn.table.cell_value_binding import CellValueBinding as CellValueBinding
with suppress(ImportError):
    from ...dyn.table.cell_vert_justify import CellVertJustify as CellVertJustify
with suppress(ImportError):
    from ...dyn.table.cell_vert_justify2 import CellVertJustify2 as CellVertJustify2
with suppress(ImportError):
    from ...dyn.table.cell_vert_justify2 import CellVertJustify2Enum as CellVertJustify2Enum
with suppress(ImportError):
    from ...dyn.table.list_position_cell_binding import ListPositionCellBinding as ListPositionCellBinding
with suppress(ImportError):
    from ...dyn.table.shadow_format import ShadowFormat as ShadowFormat
with suppress(ImportError):
    from ...dyn.table.shadow_location import ShadowLocation as ShadowLocation
with suppress(ImportError):
    from ...dyn.table.table_border import TableBorder as TableBorder
with suppress(ImportError):
    from ...dyn.table.table_border2 import TableBorder2 as TableBorder2
with suppress(ImportError):
    from ...dyn.table.table_border_distances import TableBorderDistances as TableBorderDistances
with suppress(ImportError):
    from ...dyn.table.table_chart import TableChart as TableChart
with suppress(ImportError):
    from ...dyn.table.table_charts import TableCharts as TableCharts
with suppress(ImportError):
    from ...dyn.table.table_charts_enumeration import TableChartsEnumeration as TableChartsEnumeration
with suppress(ImportError):
    from ...dyn.table.table_column import TableColumn as TableColumn
with suppress(ImportError):
    from ...dyn.table.table_columns import TableColumns as TableColumns
with suppress(ImportError):
    from ...dyn.table.table_columns_enumeration import TableColumnsEnumeration as TableColumnsEnumeration
with suppress(ImportError):
    from ...dyn.table.table_orientation import TableOrientation as TableOrientation
with suppress(ImportError):
    from ...dyn.table.table_row import TableRow as TableRow
with suppress(ImportError):
    from ...dyn.table.table_rows import TableRows as TableRows
with suppress(ImportError):
    from ...dyn.table.table_rows_enumeration import TableRowsEnumeration as TableRowsEnumeration
with suppress(ImportError):
    from ...dyn.table.table_sort_descriptor import TableSortDescriptor as TableSortDescriptor
with suppress(ImportError):
    from ...dyn.table.table_sort_descriptor2 import TableSortDescriptor2 as TableSortDescriptor2
with suppress(ImportError):
    from ...dyn.table.table_sort_field import TableSortField as TableSortField
with suppress(ImportError):
    from ...dyn.table.table_sort_field_type import TableSortFieldType as TableSortFieldType
with suppress(ImportError):
    from ...dyn.table.x_auto_formattable import XAutoFormattable as XAutoFormattable
with suppress(ImportError):
    from ...dyn.table.x_cell import XCell as XCell
with suppress(ImportError):
    from ...dyn.table.x_cell2 import XCell2 as XCell2
with suppress(ImportError):
    from ...dyn.table.x_cell_cursor import XCellCursor as XCellCursor
with suppress(ImportError):
    from ...dyn.table.x_cell_range import XCellRange as XCellRange
with suppress(ImportError):
    from ...dyn.table.x_column_row_range import XColumnRowRange as XColumnRowRange
with suppress(ImportError):
    from ...dyn.table.x_mergeable_cell import XMergeableCell as XMergeableCell
with suppress(ImportError):
    from ...dyn.table.x_mergeable_cell_range import XMergeableCellRange as XMergeableCellRange
with suppress(ImportError):
    from ...dyn.table.x_table import XTable as XTable
with suppress(ImportError):
    from ...dyn.table.x_table_chart import XTableChart as XTableChart
with suppress(ImportError):
    from ...dyn.table.x_table_charts import XTableCharts as XTableCharts
with suppress(ImportError):
    from ...dyn.table.x_table_charts_supplier import XTableChartsSupplier as XTableChartsSupplier
with suppress(ImportError):
    from ...dyn.table.x_table_columns import XTableColumns as XTableColumns
with suppress(ImportError):
    from ...dyn.table.x_table_pivot_chart import XTablePivotChart as XTablePivotChart
with suppress(ImportError):
    from ...dyn.table.x_table_pivot_charts import XTablePivotCharts as XTablePivotCharts
with suppress(ImportError):
    from ...dyn.table.x_table_pivot_charts_supplier import XTablePivotChartsSupplier as XTablePivotChartsSupplier
with suppress(ImportError):
    from ...dyn.table.x_table_rows import XTableRows as XTableRows
