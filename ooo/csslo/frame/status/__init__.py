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
import warnings
warnings.filterwarnings('module')
warnings.warn('The csslo namespace is deprecated. Use lo instead.', DeprecationWarning, stacklevel=2)
from ....lo.frame.status.clipboard_formats import ClipboardFormats as ClipboardFormats
from ....lo.frame.status.font_height import FontHeight as FontHeight
from ....lo.frame.status.item_state import ItemState as ItemState
from ....lo.frame.status.item_status import ItemStatus as ItemStatus
from ....lo.frame.status.left_right_margin import LeftRightMargin as LeftRightMargin
from ....lo.frame.status.left_right_margin_scale import LeftRightMarginScale as LeftRightMarginScale
from ....lo.frame.status.template import Template as Template
from ....lo.frame.status.upper_lower_margin import UpperLowerMargin as UpperLowerMargin
from ....lo.frame.status.upper_lower_margin_scale import UpperLowerMarginScale as UpperLowerMarginScale
from ....lo.frame.status.verb import Verb as Verb
from ....lo.frame.status.visibility import Visibility as Visibility
