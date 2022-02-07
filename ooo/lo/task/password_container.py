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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.task
from .x_password_container2 import XPasswordContainer2 as XPasswordContainer2_ce70e3b

class PasswordContainer(XPasswordContainer2_ce70e3b):
    """
    Service Class

    this service is kind of storage that allows to store passwords and to retrieve already stored.
    
    A password can be stored for the session period or persistently. The persistent way is only possible if configuration allows to use storage. It stores passwords encrypted with a super password. An interaction is used to ask a user for a super password. To allow such an interaction, an object that implements XInteractionHandler interface should be provided. For this purpose InteractionHandler service can be used.
    
    In case no interaction handler is provided all passwords are stored for the session period. In case an interaction handler is provided, but the super password interaction does not return super password ( for any reason ), NoMasterException exception is thrown to let user use non-persistent way explicitly.

    See Also:
        `API PasswordContainer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1task_1_1PasswordContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.PasswordContainer'
    __ooo_type_name__: str = 'service'


__all__ = ['PasswordContainer']

