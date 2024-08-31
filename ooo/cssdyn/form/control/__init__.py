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
    from ....dyn.form.control.check_box import CheckBox as CheckBox
with suppress(ImportError):
    from ....dyn.form.control.combo_box import ComboBox as ComboBox
with suppress(ImportError):
    from ....dyn.form.control.command_button import CommandButton as CommandButton
with suppress(ImportError):
    from ....dyn.form.control.currency_field import CurrencyField as CurrencyField
with suppress(ImportError):
    from ....dyn.form.control.date_field import DateField as DateField
with suppress(ImportError):
    from ....dyn.form.control.filter_control import FilterControl as FilterControl
with suppress(ImportError):
    from ....dyn.form.control.formatted_field import FormattedField as FormattedField
with suppress(ImportError):
    from ....dyn.form.control.grid_control import GridControl as GridControl
with suppress(ImportError):
    from ....dyn.form.control.group_box import GroupBox as GroupBox
with suppress(ImportError):
    from ....dyn.form.control.image_button import ImageButton as ImageButton
with suppress(ImportError):
    from ....dyn.form.control.image_control import ImageControl as ImageControl
with suppress(ImportError):
    from ....dyn.form.control.interaction_grid_control import InteractionGridControl as InteractionGridControl
with suppress(ImportError):
    from ....dyn.form.control.list_box import ListBox as ListBox
with suppress(ImportError):
    from ....dyn.form.control.navigation_tool_bar import NavigationToolBar as NavigationToolBar
with suppress(ImportError):
    from ....dyn.form.control.numeric_field import NumericField as NumericField
with suppress(ImportError):
    from ....dyn.form.control.pattern_field import PatternField as PatternField
with suppress(ImportError):
    from ....dyn.form.control.radio_button import RadioButton as RadioButton
with suppress(ImportError):
    from ....dyn.form.control.submit_button import SubmitButton as SubmitButton
with suppress(ImportError):
    from ....dyn.form.control.text_field import TextField as TextField
with suppress(ImportError):
    from ....dyn.form.control.time_field import TimeField as TimeField
