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
    from ...dyn.uri.external_uri_reference_translator import ExternalUriReferenceTranslator as ExternalUriReferenceTranslator
with suppress(ImportError):
    from ...dyn.uri.relative_uri_excess_parent_segments import RelativeUriExcessParentSegments as RelativeUriExcessParentSegments
with suppress(ImportError):
    from ...dyn.uri.uri_reference_factory import UriReferenceFactory as UriReferenceFactory
with suppress(ImportError):
    from ...dyn.uri.uri_scheme_parser_vnd_do_tsun_do_tstar_do_texpand import UriSchemeParser_vndDOTsunDOTstarDOTexpand as UriSchemeParser_vndDOTsunDOTstarDOTexpand
with suppress(ImportError):
    from ...dyn.uri.uri_scheme_parser_vnd_do_tsun_do_tstar_do_tscript import UriSchemeParser_vndDOTsunDOTstarDOTscript as UriSchemeParser_vndDOTsunDOTstarDOTscript
with suppress(ImportError):
    from ...dyn.uri.vnd_sun_star_pkg_url_reference_factory import VndSunStarPkgUrlReferenceFactory as VndSunStarPkgUrlReferenceFactory
with suppress(ImportError):
    from ...dyn.uri.x_external_uri_reference_translator import XExternalUriReferenceTranslator as XExternalUriReferenceTranslator
with suppress(ImportError):
    from ...dyn.uri.x_uri_reference import XUriReference as XUriReference
with suppress(ImportError):
    from ...dyn.uri.x_uri_reference_factory import XUriReferenceFactory as XUriReferenceFactory
with suppress(ImportError):
    from ...dyn.uri.x_uri_scheme_parser import XUriSchemeParser as XUriSchemeParser
with suppress(ImportError):
    from ...dyn.uri.x_vnd_sun_star_expand_url import XVndSunStarExpandUrl as XVndSunStarExpandUrl
with suppress(ImportError):
    from ...dyn.uri.x_vnd_sun_star_expand_url_reference import XVndSunStarExpandUrlReference as XVndSunStarExpandUrlReference
with suppress(ImportError):
    from ...dyn.uri.x_vnd_sun_star_pkg_url_reference_factory import XVndSunStarPkgUrlReferenceFactory as XVndSunStarPkgUrlReferenceFactory
with suppress(ImportError):
    from ...dyn.uri.x_vnd_sun_star_script_url import XVndSunStarScriptUrl as XVndSunStarScriptUrl
with suppress(ImportError):
    from ...dyn.uri.x_vnd_sun_star_script_url_reference import XVndSunStarScriptUrlReference as XVndSunStarScriptUrlReference
