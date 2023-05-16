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
    from ....dyn.form.runtime.feature_state import FeatureState as FeatureState
with suppress(ImportError):
    from ....dyn.form.runtime.filter_event import FilterEvent as FilterEvent
with suppress(ImportError):
    from ....dyn.form.runtime.form_controller import FormController as FormController
with suppress(ImportError):
    from ....dyn.form.runtime.form_feature import FormFeature as FormFeature
with suppress(ImportError):
    from ....dyn.form.runtime.form_feature import FormFeatureEnum as FormFeatureEnum
with suppress(ImportError):
    from ....dyn.form.runtime.form_operations import FormOperations as FormOperations
with suppress(ImportError):
    from ....dyn.form.runtime.x_feature_invalidation import XFeatureInvalidation as XFeatureInvalidation
with suppress(ImportError):
    from ....dyn.form.runtime.x_filter_controller import XFilterController as XFilterController
with suppress(ImportError):
    from ....dyn.form.runtime.x_filter_controller_listener import XFilterControllerListener as XFilterControllerListener
with suppress(ImportError):
    from ....dyn.form.runtime.x_form_controller import XFormController as XFormController
with suppress(ImportError):
    from ....dyn.form.runtime.x_form_controller_context import XFormControllerContext as XFormControllerContext
with suppress(ImportError):
    from ....dyn.form.runtime.x_form_operations import XFormOperations as XFormOperations
