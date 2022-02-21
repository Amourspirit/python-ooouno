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
    from ...dyn.mail.mail_attachment import MailAttachment as MailAttachment
except ImportError:
    pass
try:
    from ...dyn.mail.mail_exception import MailException as MailException
except ImportError:
    pass
try:
    from ...dyn.mail.mail_message import MailMessage as MailMessage
except ImportError:
    pass
try:
    from ...dyn.mail.mail_service_provider import MailServiceProvider as MailServiceProvider
except ImportError:
    pass
try:
    from ...dyn.mail.mail_service_type import MailServiceType as MailServiceType
except ImportError:
    pass
try:
    from ...dyn.mail.no_mail_service_provider_exception import NoMailServiceProviderException as NoMailServiceProviderException
except ImportError:
    pass
try:
    from ...dyn.mail.no_mail_transport_provider_exception import NoMailTransportProviderException as NoMailTransportProviderException
except ImportError:
    pass
try:
    from ...dyn.mail.send_mail_message_failed_exception import SendMailMessageFailedException as SendMailMessageFailedException
except ImportError:
    pass
try:
    from ...dyn.mail.x_authenticator import XAuthenticator as XAuthenticator
except ImportError:
    pass
try:
    from ...dyn.mail.x_connection_listener import XConnectionListener as XConnectionListener
except ImportError:
    pass
try:
    from ...dyn.mail.x_mail_message import XMailMessage as XMailMessage
except ImportError:
    pass
try:
    from ...dyn.mail.x_mail_service import XMailService as XMailService
except ImportError:
    pass
try:
    from ...dyn.mail.x_mail_service_provider import XMailServiceProvider as XMailServiceProvider
except ImportError:
    pass
try:
    from ...dyn.mail.x_smtp_service import XSmtpService as XSmtpService
except ImportError:
    pass
