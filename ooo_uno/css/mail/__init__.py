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
from ...uno_obj.mail.mail_attachment import MailAttachment as MailAttachment
from ...uno_obj.mail.mail_exception import MailException as MailException
from ...uno_obj.mail.mail_message import MailMessage as MailMessage
from ...uno_obj.mail.mail_service_provider import MailServiceProvider as MailServiceProvider
from ...uno_obj.mail.mail_service_type import MailServiceType as MailServiceType
from ...uno_obj.mail.no_mail_service_provider_exception import NoMailServiceProviderException as NoMailServiceProviderException
from ...uno_obj.mail.no_mail_transport_provider_exception import NoMailTransportProviderException as NoMailTransportProviderException
from ...uno_obj.mail.send_mail_message_failed_exception import SendMailMessageFailedException as SendMailMessageFailedException
from ...uno_obj.mail.x_authenticator import XAuthenticator as XAuthenticator
from ...uno_obj.mail.x_connection_listener import XConnectionListener as XConnectionListener
from ...uno_obj.mail.x_mail_message import XMailMessage as XMailMessage
from ...uno_obj.mail.x_mail_service import XMailService as XMailService
from ...uno_obj.mail.x_mail_service_provider import XMailServiceProvider as XMailServiceProvider
from ...uno_obj.mail.x_smtp_service import XSmtpService as XSmtpService
