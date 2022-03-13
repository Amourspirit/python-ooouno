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
    from ...dyn.auth.authentication_failed_exception import AuthenticationFailedException as AuthenticationFailedException
except ImportError:
    pass
try:
    from ...dyn.auth.invalid_argument_exception import InvalidArgumentException as InvalidArgumentException
except ImportError:
    pass
try:
    from ...dyn.auth.invalid_context_exception import InvalidContextException as InvalidContextException
except ImportError:
    pass
try:
    from ...dyn.auth.invalid_credential_exception import InvalidCredentialException as InvalidCredentialException
except ImportError:
    pass
try:
    from ...dyn.auth.invalid_principal_exception import InvalidPrincipalException as InvalidPrincipalException
except ImportError:
    pass
try:
    from ...dyn.auth.persistence_failure_exception import PersistenceFailureException as PersistenceFailureException
except ImportError:
    pass
try:
    from ...dyn.auth.sso_manager_factory import SSOManagerFactory as SSOManagerFactory
except ImportError:
    pass
try:
    from ...dyn.auth.sso_password_cache import SSOPasswordCache as SSOPasswordCache
except ImportError:
    pass
try:
    from ...dyn.auth.unsupported_exception import UnsupportedException as UnsupportedException
except ImportError:
    pass
try:
    from ...dyn.auth.xsso_acceptor_context import XSSOAcceptorContext as XSSOAcceptorContext
except ImportError:
    pass
try:
    from ...dyn.auth.xsso_context import XSSOContext as XSSOContext
except ImportError:
    pass
try:
    from ...dyn.auth.xsso_initiator_context import XSSOInitiatorContext as XSSOInitiatorContext
except ImportError:
    pass
try:
    from ...dyn.auth.xsso_manager import XSSOManager as XSSOManager
except ImportError:
    pass
try:
    from ...dyn.auth.xsso_manager_factory import XSSOManagerFactory as XSSOManagerFactory
except ImportError:
    pass
try:
    from ...dyn.auth.xsso_password_cache import XSSOPasswordCache as XSSOPasswordCache
except ImportError:
    pass
