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

class AuthenticationFallbackRequest(ClassifiedInteractionRequest_9f72121b):
    """
    An interaction continuation handing back some authentication data.
    
    **since**
    
        LibreOffice 4.4

    See Also:
        `API AuthenticationFallbackRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1AuthenticationFallbackRequest.html>`_
    """

    @abstractproperty
    def instructions(self) -> str:
        """
        Instructions to be followed by the user.
        """
    @abstractproperty
    def url(self) -> str:
        """
        url to be opened in browser
        """

