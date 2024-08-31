# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
    from ...dyn.security.access_control_exception import AccessControlException as AccessControlException
with suppress(ImportError):
    from ...dyn.security.access_controller import AccessController as AccessController
with suppress(ImportError):
    from ...dyn.security.all_permission import AllPermission as AllPermission
with suppress(ImportError):
    from ...dyn.security.cert_alt_name_entry import CertAltNameEntry as CertAltNameEntry
with suppress(ImportError):
    from ...dyn.security.certificate_characters import CertificateCharacters as CertificateCharacters
with suppress(ImportError):
    from ...dyn.security.certificate_characters import CertificateCharactersEnum as CertificateCharactersEnum
with suppress(ImportError):
    from ...dyn.security.certificate_container import CertificateContainer as CertificateContainer
with suppress(ImportError):
    from ...dyn.security.certificate_container_status import CertificateContainerStatus as CertificateContainerStatus
with suppress(ImportError):
    from ...dyn.security.certificate_exception import CertificateException as CertificateException
with suppress(ImportError):
    from ...dyn.security.certificate_kind import CertificateKind as CertificateKind
with suppress(ImportError):
    from ...dyn.security.certificate_validity import CertificateValidity as CertificateValidity
with suppress(ImportError):
    from ...dyn.security.certificate_validity import CertificateValidityEnum as CertificateValidityEnum
with suppress(ImportError):
    from ...dyn.security.cryptography_exception import CryptographyException as CryptographyException
with suppress(ImportError):
    from ...dyn.security.document_digital_signatures import DocumentDigitalSignatures as DocumentDigitalSignatures
with suppress(ImportError):
    from ...dyn.security.document_signature_information import DocumentSignatureInformation as DocumentSignatureInformation
with suppress(ImportError):
    from ...dyn.security.encryption_exception import EncryptionException as EncryptionException
with suppress(ImportError):
    from ...dyn.security.ext_alt_name_type import ExtAltNameType as ExtAltNameType
with suppress(ImportError):
    from ...dyn.security.key_exception import KeyException as KeyException
with suppress(ImportError):
    from ...dyn.security.key_usage import KeyUsage as KeyUsage
with suppress(ImportError):
    from ...dyn.security.key_usage import KeyUsageEnum as KeyUsageEnum
with suppress(ImportError):
    from ...dyn.security.no_password_exception import NoPasswordException as NoPasswordException
with suppress(ImportError):
    from ...dyn.security.policy import Policy as Policy
with suppress(ImportError):
    from ...dyn.security.runtime_permission import RuntimePermission as RuntimePermission
with suppress(ImportError):
    from ...dyn.security.security_infrastructure_exception import SecurityInfrastructureException as SecurityInfrastructureException
with suppress(ImportError):
    from ...dyn.security.signature_exception import SignatureException as SignatureException
with suppress(ImportError):
    from ...dyn.security.x_access_control_context import XAccessControlContext as XAccessControlContext
with suppress(ImportError):
    from ...dyn.security.x_access_controller import XAccessController as XAccessController
with suppress(ImportError):
    from ...dyn.security.x_action import XAction as XAction
with suppress(ImportError):
    from ...dyn.security.x_certificate import XCertificate as XCertificate
with suppress(ImportError):
    from ...dyn.security.x_certificate_container import XCertificateContainer as XCertificateContainer
with suppress(ImportError):
    from ...dyn.security.x_certificate_extension import XCertificateExtension as XCertificateExtension
with suppress(ImportError):
    from ...dyn.security.x_document_digital_signatures import XDocumentDigitalSignatures as XDocumentDigitalSignatures
with suppress(ImportError):
    from ...dyn.security.x_policy import XPolicy as XPolicy
with suppress(ImportError):
    from ...dyn.security.x_san_extension import XSanExtension as XSanExtension
