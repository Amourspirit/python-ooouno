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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.system


class SimpleMailClientFlags(object):
    """
    Const Class

    These constants are used to specify how the SimpleMailClient Service should behave.

    See Also:
        `API SimpleMailClientFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1system_1_1SimpleMailClientFlags.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.system'
    __ooo_full_ns__: str = 'com.sun.star.system.SimpleMailClientFlags'
    __ooo_type_name__: str = 'const'

    DEFAULTS = 0
    """
    Uses the default settings when sending a mail, e.g.
    
    launches the current configured system mail client.
    """
    NO_USER_INTERFACE = 1
    """
    Does not show the current configured system mail client, but sends the mail without any further user interaction.
    
    If this flag is specified, a recipient address must have been specified for the given XSimpleMailMessage object given to the method com.sun.star.system.XSimpleMailClient.sendSimpleMailMessage().
    """
    NO_LOGON_DIALOG = 2
    """
    No logon dialog should be displayed to prompt the user for logon information if necessary.
    
    When this flag is specified and the user needs to logon in order to send a simple mail message via the method com.sun.star.system.XSimpleMailClient.sendSimpleMailMessage(), an Exception will be thrown.
    """

__all__ = ['SimpleMailClientFlags']
