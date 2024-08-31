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
# Namespace: com.sun.star.document


class LinkUpdateModes(object):
    """
    Const Class


    See Also:
        `API LinkUpdateModes <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1document_1_1LinkUpdateModes.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.LinkUpdateModes'
    __ooo_type_name__: str = 'const'

    NEVER = 0
    """
    never update links
    """
    MANUAL = 1
    """
    update links when confirmed on request during loading the document
    """
    AUTO = 2
    """
    automatic update on load
    """
    GLOBAL_SETTING = 3
    """
    use the setting that is configured in your installed application.
    
    This may be one of the above behaviors.
    """

__all__ = ['LinkUpdateModes']
