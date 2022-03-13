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
    from ...dyn.smarttags.smart_tag_action import SmartTagAction as SmartTagAction
except ImportError:
    pass
try:
    from ...dyn.smarttags.smart_tag_recognizer import SmartTagRecognizer as SmartTagRecognizer
except ImportError:
    pass
try:
    from ...dyn.smarttags.smart_tag_recognizer_mode import SmartTagRecognizerMode as SmartTagRecognizerMode
except ImportError:
    pass
try:
    from ...dyn.smarttags.x_range_based_smart_tag_recognizer import XRangeBasedSmartTagRecognizer as XRangeBasedSmartTagRecognizer
except ImportError:
    pass
try:
    from ...dyn.smarttags.x_smart_tag_action import XSmartTagAction as XSmartTagAction
except ImportError:
    pass
try:
    from ...dyn.smarttags.x_smart_tag_recognizer import XSmartTagRecognizer as XSmartTagRecognizer
except ImportError:
    pass
