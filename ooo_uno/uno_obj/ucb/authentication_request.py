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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from abc import abstractproperty
from ..task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b

class AuthenticationRequest(ClassifiedInteractionRequest_9f72121b):
    """
    An error specifying lack of correct authentication data (e.g., to log into an account).

    See Also:
        `API AuthenticationRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1AuthenticationRequest.html>`_
    """

    @abstractproperty
    def Account(self) -> str:
        """
        Any already specified account.
        
        If HasAccount is false, this member should be ignored.
        """
    @abstractproperty
    def Diagnostic(self) -> str:
        """
        Any diagnostic message about the failure to log in (if applicable; it will typically be an English phrase or sentence).
        """
    @abstractproperty
    def HasAccount(self) -> bool:
        """
        Specifies if the authentication involves an \"account\" (as can be the case for FTP).
        """
    @abstractproperty
    def HasPassword(self) -> bool:
        """
        Specifies if the authentication involves a \"password\" (as is almost always the case).
        """
    @abstractproperty
    def HasRealm(self) -> bool:
        """
        Specifies if the authentication involves a \"realm\" (as can be the case for HTTP).
        """
    @abstractproperty
    def HasUserName(self) -> bool:
        """
        Specifies if the authentication involves a \"user name\" (as is almost always the case).
        """
    @abstractproperty
    def Password(self) -> str:
        """
        Any already specified password.
        
        If HasPassword is false, this member should be ignored.
        """
    @abstractproperty
    def Realm(self) -> str:
        """
        Any already specified realm.
        
        If HasRealm is false, this member should be ignored.
        """
    @abstractproperty
    def ServerName(self) -> str:
        """
        The name of the server (if applicable).
        """
    @abstractproperty
    def UserName(self) -> str:
        """
        Any already specified user name.
        
        If HasUserName is false, this member should be ignored.
        """

