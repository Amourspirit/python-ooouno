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
    from ...dyn.xforms.binding import Binding as Binding
except ImportError:
    pass
try:
    from ...dyn.xforms.invalid_data_on_submit_exception import InvalidDataOnSubmitException as InvalidDataOnSubmitException
except ImportError:
    pass
try:
    from ...dyn.xforms.model import Model as Model
except ImportError:
    pass
try:
    from ...dyn.xforms.x_data_type_repository import XDataTypeRepository as XDataTypeRepository
except ImportError:
    pass
try:
    from ...dyn.xforms.x_forms import XForms as XForms
except ImportError:
    pass
try:
    from ...dyn.xforms.x_forms_event import XFormsEvent as XFormsEvent
except ImportError:
    pass
try:
    from ...dyn.xforms.x_forms_supplier import XFormsSupplier as XFormsSupplier
except ImportError:
    pass
try:
    from ...dyn.xforms.x_forms_ui_helper1 import XFormsUIHelper1 as XFormsUIHelper1
except ImportError:
    pass
try:
    from ...dyn.xforms.x_model import XModel as XModel
except ImportError:
    pass
try:
    from ...dyn.xforms.x_model2 import XModel2 as XModel2
except ImportError:
    pass
try:
    from ...dyn.xforms.x_submission import XSubmission as XSubmission
except ImportError:
    pass
