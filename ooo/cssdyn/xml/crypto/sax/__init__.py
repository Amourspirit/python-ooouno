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
    from .....dyn.xml.crypto.sax.const_of_security_id import ConstOfSecurityId as ConstOfSecurityId
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.const_of_security_id import ConstOfSecurityIdEnum as ConstOfSecurityIdEnum
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.element_mark_priority import ElementMarkPriority as ElementMarkPriority
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.element_mark_type import ElementMarkType as ElementMarkType
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.element_stack_item import ElementStackItem as ElementStackItem
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_blocker_monitor import XBlockerMonitor as XBlockerMonitor
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_decryption_result_broadcaster import XDecryptionResultBroadcaster as XDecryptionResultBroadcaster
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_decryption_result_listener import XDecryptionResultListener as XDecryptionResultListener
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_element_stack_keeper import XElementStackKeeper as XElementStackKeeper
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_encryption_result_broadcaster import XEncryptionResultBroadcaster as XEncryptionResultBroadcaster
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_encryption_result_listener import XEncryptionResultListener as XEncryptionResultListener
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_key_collector import XKeyCollector as XKeyCollector
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_mission_taker import XMissionTaker as XMissionTaker
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_reference_collector import XReferenceCollector as XReferenceCollector
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_reference_resolved_broadcaster import XReferenceResolvedBroadcaster as XReferenceResolvedBroadcaster
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_reference_resolved_listener import XReferenceResolvedListener as XReferenceResolvedListener
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.xsax_event_keeper import XSAXEventKeeper as XSAXEventKeeper
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.xsax_event_keeper_status_change_broadcaster import XSAXEventKeeperStatusChangeBroadcaster as XSAXEventKeeperStatusChangeBroadcaster
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.xsax_event_keeper_status_change_listener import XSAXEventKeeperStatusChangeListener as XSAXEventKeeperStatusChangeListener
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_security_sax_event_keeper import XSecuritySAXEventKeeper as XSecuritySAXEventKeeper
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_signature_creation_result_broadcaster import XSignatureCreationResultBroadcaster as XSignatureCreationResultBroadcaster
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_signature_creation_result_listener import XSignatureCreationResultListener as XSignatureCreationResultListener
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_signature_verify_result_broadcaster import XSignatureVerifyResultBroadcaster as XSignatureVerifyResultBroadcaster
with suppress(ImportError):
    from .....dyn.xml.crypto.sax.x_signature_verify_result_listener import XSignatureVerifyResultListener as XSignatureVerifyResultListener
