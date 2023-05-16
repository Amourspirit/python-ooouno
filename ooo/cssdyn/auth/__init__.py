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
    from ...dyn.auth.authentication_failed_exception import AuthenticationFailedException as AuthenticationFailedException
with suppress(ImportError):
    from ...dyn.auth.invalid_argument_exception import InvalidArgumentException as InvalidArgumentException
with suppress(ImportError):
    from ...dyn.auth.invalid_context_exception import InvalidContextException as InvalidContextException
with suppress(ImportError):
    from ...dyn.auth.invalid_credential_exception import InvalidCredentialException as InvalidCredentialException
with suppress(ImportError):
    from ...dyn.auth.invalid_principal_exception import InvalidPrincipalException as InvalidPrincipalException
with suppress(ImportError):
    from ...dyn.auth.persistence_failure_exception import PersistenceFailureException as PersistenceFailureException
with suppress(ImportError):
    from ...dyn.auth.sso_manager_factory import SSOManagerFactory as SSOManagerFactory
with suppress(ImportError):
    from ...dyn.auth.sso_password_cache import SSOPasswordCache as SSOPasswordCache
with suppress(ImportError):
    from ...dyn.auth.unsupported_exception import UnsupportedException as UnsupportedException
with suppress(ImportError):
    from ...dyn.auth.xsso_acceptor_context import XSSOAcceptorContext as XSSOAcceptorContext
with suppress(ImportError):
    from ...dyn.auth.xsso_context import XSSOContext as XSSOContext
with suppress(ImportError):
    from ...dyn.auth.xsso_initiator_context import XSSOInitiatorContext as XSSOInitiatorContext
with suppress(ImportError):
    from ...dyn.auth.xsso_manager import XSSOManager as XSSOManager
with suppress(ImportError):
    from ...dyn.auth.xsso_manager_factory import XSSOManagerFactory as XSSOManagerFactory
with suppress(ImportError):
    from ...dyn.auth.xsso_password_cache import XSSOPasswordCache as XSSOPasswordCache
