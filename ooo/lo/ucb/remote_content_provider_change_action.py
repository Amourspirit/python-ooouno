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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from enum import Enum


class RemoteContentProviderChangeAction(Enum):
    """
    Enum Class

    

    See Also:
        `API RemoteContentProviderChangeAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#abe4a959f1ea6647971dafe5b6c90c7ec>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.RemoteContentProviderChangeAction'
    __ooo_type_name__: str = 'enum'

    ADDED = 'ADDED'
    """
    The indicator that a remote content provider has been added.
    """
    REMOVED = 'REMOVED'
    """
    The indicator that a remote content provider has been removed.
    """

__all__ = ['RemoteContentProviderChangeAction']

