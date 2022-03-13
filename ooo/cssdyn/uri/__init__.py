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
    from ...dyn.uri.external_uri_reference_translator import ExternalUriReferenceTranslator as ExternalUriReferenceTranslator
except ImportError:
    pass
try:
    from ...dyn.uri.relative_uri_excess_parent_segments import RelativeUriExcessParentSegments as RelativeUriExcessParentSegments
except ImportError:
    pass
try:
    from ...dyn.uri.uri_reference_factory import UriReferenceFactory as UriReferenceFactory
except ImportError:
    pass
try:
    from ...dyn.uri.uri_scheme_parser_vnd_do_tsun_do_tstar_do_texpand import UriSchemeParser_vndDOTsunDOTstarDOTexpand as UriSchemeParser_vndDOTsunDOTstarDOTexpand
except ImportError:
    pass
try:
    from ...dyn.uri.uri_scheme_parser_vnd_do_tsun_do_tstar_do_tscript import UriSchemeParser_vndDOTsunDOTstarDOTscript as UriSchemeParser_vndDOTsunDOTstarDOTscript
except ImportError:
    pass
try:
    from ...dyn.uri.vnd_sun_star_pkg_url_reference_factory import VndSunStarPkgUrlReferenceFactory as VndSunStarPkgUrlReferenceFactory
except ImportError:
    pass
try:
    from ...dyn.uri.x_external_uri_reference_translator import XExternalUriReferenceTranslator as XExternalUriReferenceTranslator
except ImportError:
    pass
try:
    from ...dyn.uri.x_uri_reference import XUriReference as XUriReference
except ImportError:
    pass
try:
    from ...dyn.uri.x_uri_reference_factory import XUriReferenceFactory as XUriReferenceFactory
except ImportError:
    pass
try:
    from ...dyn.uri.x_uri_scheme_parser import XUriSchemeParser as XUriSchemeParser
except ImportError:
    pass
try:
    from ...dyn.uri.x_vnd_sun_star_expand_url import XVndSunStarExpandUrl as XVndSunStarExpandUrl
except ImportError:
    pass
try:
    from ...dyn.uri.x_vnd_sun_star_expand_url_reference import XVndSunStarExpandUrlReference as XVndSunStarExpandUrlReference
except ImportError:
    pass
try:
    from ...dyn.uri.x_vnd_sun_star_pkg_url_reference_factory import XVndSunStarPkgUrlReferenceFactory as XVndSunStarPkgUrlReferenceFactory
except ImportError:
    pass
try:
    from ...dyn.uri.x_vnd_sun_star_script_url import XVndSunStarScriptUrl as XVndSunStarScriptUrl
except ImportError:
    pass
try:
    from ...dyn.uri.x_vnd_sun_star_script_url_reference import XVndSunStarScriptUrlReference as XVndSunStarScriptUrlReference
except ImportError:
    pass
