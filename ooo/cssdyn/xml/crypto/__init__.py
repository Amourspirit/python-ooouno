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
    from ....dyn.xml.crypto.cipher_id import CipherID as CipherID
with suppress(ImportError):
    from ....dyn.xml.crypto.cipher_id import CipherIDEnum as CipherIDEnum
with suppress(ImportError):
    from ....dyn.xml.crypto.digest_id import DigestID as DigestID
with suppress(ImportError):
    from ....dyn.xml.crypto.digest_id import DigestIDEnum as DigestIDEnum
with suppress(ImportError):
    from ....dyn.xml.crypto.gpgse_initializer import GPGSEInitializer as GPGSEInitializer
with suppress(ImportError):
    from ....dyn.xml.crypto.nss_initializer import NSSInitializer as NSSInitializer
with suppress(ImportError):
    from ....dyn.xml.crypto.nss_profile import NSSProfile as NSSProfile
with suppress(ImportError):
    from ....dyn.xml.crypto.se_initializer import SEInitializer as SEInitializer
with suppress(ImportError):
    from ....dyn.xml.crypto.security_environment import SecurityEnvironment as SecurityEnvironment
with suppress(ImportError):
    from ....dyn.xml.crypto.security_operation_status import SecurityOperationStatus as SecurityOperationStatus
with suppress(ImportError):
    from ....dyn.xml.crypto.x_certificate_creator import XCertificateCreator as XCertificateCreator
with suppress(ImportError):
    from ....dyn.xml.crypto.x_cipher_context import XCipherContext as XCipherContext
with suppress(ImportError):
    from ....dyn.xml.crypto.x_cipher_context_supplier import XCipherContextSupplier as XCipherContextSupplier
with suppress(ImportError):
    from ....dyn.xml.crypto.x_digest_context import XDigestContext as XDigestContext
with suppress(ImportError):
    from ....dyn.xml.crypto.x_digest_context_supplier import XDigestContextSupplier as XDigestContextSupplier
with suppress(ImportError):
    from ....dyn.xml.crypto.xml_encryption_exception import XMLEncryptionException as XMLEncryptionException
with suppress(ImportError):
    from ....dyn.xml.crypto.xml_security_context import XMLSecurityContext as XMLSecurityContext
with suppress(ImportError):
    from ....dyn.xml.crypto.xml_signature import XMLSignature as XMLSignature
with suppress(ImportError):
    from ....dyn.xml.crypto.xml_signature_exception import XMLSignatureException as XMLSignatureException
with suppress(ImportError):
    from ....dyn.xml.crypto.xnss_initializer import XNSSInitializer as XNSSInitializer
with suppress(ImportError):
    from ....dyn.xml.crypto.xse_initializer import XSEInitializer as XSEInitializer
with suppress(ImportError):
    from ....dyn.xml.crypto.x_security_environment import XSecurityEnvironment as XSecurityEnvironment
with suppress(ImportError):
    from ....dyn.xml.crypto.x_uri_binding import XUriBinding as XUriBinding
with suppress(ImportError):
    from ....dyn.xml.crypto.xxml_encryption import XXMLEncryption as XXMLEncryption
with suppress(ImportError):
    from ....dyn.xml.crypto.xxml_encryption_template import XXMLEncryptionTemplate as XXMLEncryptionTemplate
with suppress(ImportError):
    from ....dyn.xml.crypto.xxml_security_context import XXMLSecurityContext as XXMLSecurityContext
with suppress(ImportError):
    from ....dyn.xml.crypto.xxml_security_template import XXMLSecurityTemplate as XXMLSecurityTemplate
with suppress(ImportError):
    from ....dyn.xml.crypto.xxml_signature import XXMLSignature as XXMLSignature
with suppress(ImportError):
    from ....dyn.xml.crypto.xxml_signature_template import XXMLSignatureTemplate as XXMLSignatureTemplate
