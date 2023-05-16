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
    from ....dyn.form.inspection.button_navigation_handler import ButtonNavigationHandler as ButtonNavigationHandler
with suppress(ImportError):
    from ....dyn.form.inspection.cell_binding_property_handler import CellBindingPropertyHandler as CellBindingPropertyHandler
with suppress(ImportError):
    from ....dyn.form.inspection.default_form_component_inspector_model import DefaultFormComponentInspectorModel as DefaultFormComponentInspectorModel
with suppress(ImportError):
    from ....dyn.form.inspection.edit_property_handler import EditPropertyHandler as EditPropertyHandler
with suppress(ImportError):
    from ....dyn.form.inspection.event_handler import EventHandler as EventHandler
with suppress(ImportError):
    from ....dyn.form.inspection.form_component_property_handler import FormComponentPropertyHandler as FormComponentPropertyHandler
with suppress(ImportError):
    from ....dyn.form.inspection.submission_property_handler import SubmissionPropertyHandler as SubmissionPropertyHandler
with suppress(ImportError):
    from ....dyn.form.inspection.xml_forms_property_handler import XMLFormsPropertyHandler as XMLFormsPropertyHandler
with suppress(ImportError):
    from ....dyn.form.inspection.xsd_validation_property_handler import XSDValidationPropertyHandler as XSDValidationPropertyHandler
