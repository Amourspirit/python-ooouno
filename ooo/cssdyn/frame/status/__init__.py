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
    from ....dyn.frame.status.clipboard_formats import ClipboardFormats as ClipboardFormats
except ImportError:
    pass
try:
    from ....dyn.frame.status.font_height import FontHeight as FontHeight
except ImportError:
    pass
try:
    from ....dyn.frame.status.item_state import ItemState as ItemState
except ImportError:
    pass
try:
    from ....dyn.frame.status.item_state import ItemStateEnum as ItemStateEnum
except ImportError:
    pass
try:
    from ....dyn.frame.status.item_status import ItemStatus as ItemStatus
except ImportError:
    pass
try:
    from ....dyn.frame.status.left_right_margin import LeftRightMargin as LeftRightMargin
except ImportError:
    pass
try:
    from ....dyn.frame.status.left_right_margin_scale import LeftRightMarginScale as LeftRightMarginScale
except ImportError:
    pass
try:
    from ....dyn.frame.status.template import Template as Template
except ImportError:
    pass
try:
    from ....dyn.frame.status.upper_lower_margin import UpperLowerMargin as UpperLowerMargin
except ImportError:
    pass
try:
    from ....dyn.frame.status.upper_lower_margin_scale import UpperLowerMarginScale as UpperLowerMarginScale
except ImportError:
    pass
try:
    from ....dyn.frame.status.verb import Verb as Verb
except ImportError:
    pass
try:
    from ....dyn.frame.status.visibility import Visibility as Visibility
except ImportError:
    pass
