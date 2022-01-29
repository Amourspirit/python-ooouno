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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from ooo_uno.base.const import ConstIntBase


class UserFieldFormat(ConstIntBase):
    """
    These constants describe how the content of a user text field is formatted.

    See Also:
        `API UserFieldFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1UserFieldFormat.html>`_
    """
    SYSTEM = 0
    """
    The number format of the operating system is used.
    """
    TEXT = 1
    """
    The content is formatted as text.
    """
    NUM = 2
    """
    The number format of the property \"NumberFormat\" is used.
    """

