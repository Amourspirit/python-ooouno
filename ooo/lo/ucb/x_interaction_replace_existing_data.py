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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.ucb
from ..task.x_interaction_continuation import XInteractionContinuation as XInteractionContinuation_5af0108e

class XInteractionReplaceExistingData(XInteractionContinuation_5af0108e):
    """
    is an interaction continuation used to instruct the requester to replace existing data.
    
    For example, this continuation can be selected when handling a NameClashResolveRequest in order to instruct the requester to overwrite the clashing data.

    See Also:
        `API XInteractionReplaceExistingData <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XInteractionReplaceExistingData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XInteractionReplaceExistingData'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XInteractionReplaceExistingData'


__all__ = ['XInteractionReplaceExistingData']

