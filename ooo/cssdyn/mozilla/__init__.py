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
    from ...dyn.mozilla.menu_multiple_change import MenuMultipleChange as MenuMultipleChange
except ImportError:
    pass
try:
    from ...dyn.mozilla.menu_proxy import MenuProxy as MenuProxy
except ImportError:
    pass
try:
    from ...dyn.mozilla.menu_proxy_listener import MenuProxyListener as MenuProxyListener
except ImportError:
    pass
try:
    from ...dyn.mozilla.menu_single_change import MenuSingleChange as MenuSingleChange
except ImportError:
    pass
try:
    from ...dyn.mozilla.mozilla_bootstrap import MozillaBootstrap as MozillaBootstrap
except ImportError:
    pass
try:
    from ...dyn.mozilla.mozilla_product_type import MozillaProductType as MozillaProductType
except ImportError:
    pass
try:
    from ...dyn.mozilla.x_close_session_listener import XCloseSessionListener as XCloseSessionListener
except ImportError:
    pass
try:
    from ...dyn.mozilla.x_code_proxy import XCodeProxy as XCodeProxy
except ImportError:
    pass
try:
    from ...dyn.mozilla.x_menu_proxy import XMenuProxy as XMenuProxy
except ImportError:
    pass
try:
    from ...dyn.mozilla.x_menu_proxy_listener import XMenuProxyListener as XMenuProxyListener
except ImportError:
    pass
try:
    from ...dyn.mozilla.x_mozilla_bootstrap import XMozillaBootstrap as XMozillaBootstrap
except ImportError:
    pass
try:
    from ...dyn.mozilla.x_profile_discover import XProfileDiscover as XProfileDiscover
except ImportError:
    pass
try:
    from ...dyn.mozilla.x_profile_manager import XProfileManager as XProfileManager
except ImportError:
    pass
try:
    from ...dyn.mozilla.x_proxy_runner import XProxyRunner as XProxyRunner
except ImportError:
    pass
