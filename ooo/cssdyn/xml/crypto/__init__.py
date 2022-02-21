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
    from ....dyn.xml.crypto.cipher_id import CipherID as CipherID
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.cipher_id import CipherIDEnum as CipherIDEnum
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.digest_id import DigestID as DigestID
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.digest_id import DigestIDEnum as DigestIDEnum
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.gpgse_initializer import GPGSEInitializer as GPGSEInitializer
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.nss_initializer import NSSInitializer as NSSInitializer
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.nss_profile import NSSProfile as NSSProfile
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.se_initializer import SEInitializer as SEInitializer
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.security_environment import SecurityEnvironment as SecurityEnvironment
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.security_operation_status import SecurityOperationStatus as SecurityOperationStatus
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.x_certificate_creator import XCertificateCreator as XCertificateCreator
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.x_cipher_context import XCipherContext as XCipherContext
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.x_cipher_context_supplier import XCipherContextSupplier as XCipherContextSupplier
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.x_digest_context import XDigestContext as XDigestContext
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.x_digest_context_supplier import XDigestContextSupplier as XDigestContextSupplier
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xml_encryption_exception import XMLEncryptionException as XMLEncryptionException
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xml_security_context import XMLSecurityContext as XMLSecurityContext
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xml_signature import XMLSignature as XMLSignature
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xml_signature_exception import XMLSignatureException as XMLSignatureException
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xnss_initializer import XNSSInitializer as XNSSInitializer
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xse_initializer import XSEInitializer as XSEInitializer
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.x_security_environment import XSecurityEnvironment as XSecurityEnvironment
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.x_uri_binding import XUriBinding as XUriBinding
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xxml_encryption import XXMLEncryption as XXMLEncryption
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xxml_encryption_template import XXMLEncryptionTemplate as XXMLEncryptionTemplate
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xxml_security_context import XXMLSecurityContext as XXMLSecurityContext
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xxml_security_template import XXMLSecurityTemplate as XXMLSecurityTemplate
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xxml_signature import XXMLSignature as XXMLSignature
except ImportError:
    pass
try:
    from ....dyn.xml.crypto.xxml_signature_template import XXMLSignatureTemplate as XXMLSignatureTemplate
except ImportError:
    pass
