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
# all imports are wrapped in try blocks for allowing of backwards compatibility.

try:
    from ...dyn.report.calculation import Calculation as Calculation
except ImportError:
    pass
try:
    from ...dyn.report.calculation import CalculationEnum as CalculationEnum
except ImportError:
    pass
try:
    from ...dyn.report.fixed_line import FixedLine as FixedLine
except ImportError:
    pass
try:
    from ...dyn.report.fixed_text import FixedText as FixedText
except ImportError:
    pass
try:
    from ...dyn.report.force_new_page import ForceNewPage as ForceNewPage
except ImportError:
    pass
try:
    from ...dyn.report.force_new_page import ForceNewPageEnum as ForceNewPageEnum
except ImportError:
    pass
try:
    from ...dyn.report.format_condition import FormatCondition as FormatCondition
except ImportError:
    pass
try:
    from ...dyn.report.formatted_field import FormattedField as FormattedField
except ImportError:
    pass
try:
    from ...dyn.report.function import Function as Function
except ImportError:
    pass
try:
    from ...dyn.report.group import Group as Group
except ImportError:
    pass
try:
    from ...dyn.report.group_keep_together import GroupKeepTogether as GroupKeepTogether
except ImportError:
    pass
try:
    from ...dyn.report.group_keep_together import GroupKeepTogetherEnum as GroupKeepTogetherEnum
except ImportError:
    pass
try:
    from ...dyn.report.group_on import GroupOn as GroupOn
except ImportError:
    pass
try:
    from ...dyn.report.group_on import GroupOnEnum as GroupOnEnum
except ImportError:
    pass
try:
    from ...dyn.report.groups import Groups as Groups
except ImportError:
    pass
try:
    from ...dyn.report.image_control import ImageControl as ImageControl
except ImportError:
    pass
try:
    from ...dyn.report.keep_together import KeepTogether as KeepTogether
except ImportError:
    pass
try:
    from ...dyn.report.keep_together import KeepTogetherEnum as KeepTogetherEnum
except ImportError:
    pass
try:
    from ...dyn.report.report_control_format import ReportControlFormat as ReportControlFormat
except ImportError:
    pass
try:
    from ...dyn.report.report_control_model import ReportControlModel as ReportControlModel
except ImportError:
    pass
try:
    from ...dyn.report.report_definition import ReportDefinition as ReportDefinition
except ImportError:
    pass
try:
    from ...dyn.report.report_engine import ReportEngine as ReportEngine
except ImportError:
    pass
try:
    from ...dyn.report.report_print_option import ReportPrintOption as ReportPrintOption
except ImportError:
    pass
try:
    from ...dyn.report.report_print_option import ReportPrintOptionEnum as ReportPrintOptionEnum
except ImportError:
    pass
try:
    from ...dyn.report.section import Section as Section
except ImportError:
    pass
try:
    from ...dyn.report.section_page_break import SectionPageBreak as SectionPageBreak
except ImportError:
    pass
try:
    from ...dyn.report.section_page_break import SectionPageBreakEnum as SectionPageBreakEnum
except ImportError:
    pass
try:
    from ...dyn.report.shape import Shape as Shape
except ImportError:
    pass
try:
    from ...dyn.report.x_fixed_line import XFixedLine as XFixedLine
except ImportError:
    pass
try:
    from ...dyn.report.x_fixed_text import XFixedText as XFixedText
except ImportError:
    pass
try:
    from ...dyn.report.x_format_condition import XFormatCondition as XFormatCondition
except ImportError:
    pass
try:
    from ...dyn.report.x_formatted_field import XFormattedField as XFormattedField
except ImportError:
    pass
try:
    from ...dyn.report.x_function import XFunction as XFunction
except ImportError:
    pass
try:
    from ...dyn.report.x_functions import XFunctions as XFunctions
except ImportError:
    pass
try:
    from ...dyn.report.x_functions_supplier import XFunctionsSupplier as XFunctionsSupplier
except ImportError:
    pass
try:
    from ...dyn.report.x_group import XGroup as XGroup
except ImportError:
    pass
try:
    from ...dyn.report.x_groups import XGroups as XGroups
except ImportError:
    pass
try:
    from ...dyn.report.x_image_control import XImageControl as XImageControl
except ImportError:
    pass
try:
    from ...dyn.report.x_report_component import XReportComponent as XReportComponent
except ImportError:
    pass
try:
    from ...dyn.report.x_report_control_format import XReportControlFormat as XReportControlFormat
except ImportError:
    pass
try:
    from ...dyn.report.x_report_control_model import XReportControlModel as XReportControlModel
except ImportError:
    pass
try:
    from ...dyn.report.x_report_definition import XReportDefinition as XReportDefinition
except ImportError:
    pass
try:
    from ...dyn.report.x_report_engine import XReportEngine as XReportEngine
except ImportError:
    pass
try:
    from ...dyn.report.x_section import XSection as XSection
except ImportError:
    pass
try:
    from ...dyn.report.x_shape import XShape as XShape
except ImportError:
    pass
