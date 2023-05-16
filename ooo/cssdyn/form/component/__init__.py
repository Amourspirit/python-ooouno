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


from contextlib import suppress
import warnings
warnings.filterwarnings('module')
warnings.warn('The cssdyn namespace is deprecated. Use dyn instead.', DeprecationWarning, stacklevel=2)

with suppress(ImportError):
    from ....dyn.form.component.check_box import CheckBox as CheckBox
with suppress(ImportError):
    from ....dyn.form.component.combo_box import ComboBox as ComboBox
with suppress(ImportError):
    from ....dyn.form.component.command_button import CommandButton as CommandButton
with suppress(ImportError):
    from ....dyn.form.component.currency_field import CurrencyField as CurrencyField
with suppress(ImportError):
    from ....dyn.form.component.data_form import DataForm as DataForm
with suppress(ImportError):
    from ....dyn.form.component.database_check_box import DatabaseCheckBox as DatabaseCheckBox
with suppress(ImportError):
    from ....dyn.form.component.database_combo_box import DatabaseComboBox as DatabaseComboBox
with suppress(ImportError):
    from ....dyn.form.component.database_currency_field import DatabaseCurrencyField as DatabaseCurrencyField
with suppress(ImportError):
    from ....dyn.form.component.database_date_field import DatabaseDateField as DatabaseDateField
with suppress(ImportError):
    from ....dyn.form.component.database_formatted_field import DatabaseFormattedField as DatabaseFormattedField
with suppress(ImportError):
    from ....dyn.form.component.database_image_control import DatabaseImageControl as DatabaseImageControl
with suppress(ImportError):
    from ....dyn.form.component.database_list_box import DatabaseListBox as DatabaseListBox
with suppress(ImportError):
    from ....dyn.form.component.database_numeric_field import DatabaseNumericField as DatabaseNumericField
with suppress(ImportError):
    from ....dyn.form.component.database_pattern_field import DatabasePatternField as DatabasePatternField
with suppress(ImportError):
    from ....dyn.form.component.database_radio_button import DatabaseRadioButton as DatabaseRadioButton
with suppress(ImportError):
    from ....dyn.form.component.database_text_field import DatabaseTextField as DatabaseTextField
with suppress(ImportError):
    from ....dyn.form.component.database_time_field import DatabaseTimeField as DatabaseTimeField
with suppress(ImportError):
    from ....dyn.form.component.date_field import DateField as DateField
with suppress(ImportError):
    from ....dyn.form.component.file_control import FileControl as FileControl
with suppress(ImportError):
    from ....dyn.form.component.fixed_text import FixedText as FixedText
with suppress(ImportError):
    from ....dyn.form.component.form import Form as Form
with suppress(ImportError):
    from ....dyn.form.component.formatted_field import FormattedField as FormattedField
with suppress(ImportError):
    from ....dyn.form.component.grid_control import GridControl as GridControl
with suppress(ImportError):
    from ....dyn.form.component.group_box import GroupBox as GroupBox
with suppress(ImportError):
    from ....dyn.form.component.html_form import HTMLForm as HTMLForm
with suppress(ImportError):
    from ....dyn.form.component.hidden_control import HiddenControl as HiddenControl
with suppress(ImportError):
    from ....dyn.form.component.image_button import ImageButton as ImageButton
with suppress(ImportError):
    from ....dyn.form.component.list_box import ListBox as ListBox
with suppress(ImportError):
    from ....dyn.form.component.navigation_tool_bar import NavigationToolBar as NavigationToolBar
with suppress(ImportError):
    from ....dyn.form.component.numeric_field import NumericField as NumericField
with suppress(ImportError):
    from ....dyn.form.component.pattern_field import PatternField as PatternField
with suppress(ImportError):
    from ....dyn.form.component.radio_button import RadioButton as RadioButton
with suppress(ImportError):
    from ....dyn.form.component.rich_text_control import RichTextControl as RichTextControl
with suppress(ImportError):
    from ....dyn.form.component.scroll_bar import ScrollBar as ScrollBar
with suppress(ImportError):
    from ....dyn.form.component.spin_button import SpinButton as SpinButton
with suppress(ImportError):
    from ....dyn.form.component.submit_button import SubmitButton as SubmitButton
with suppress(ImportError):
    from ....dyn.form.component.text_field import TextField as TextField
with suppress(ImportError):
    from ....dyn.form.component.time_field import TimeField as TimeField
