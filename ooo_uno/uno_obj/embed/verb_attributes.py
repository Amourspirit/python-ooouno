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
# Namespace: com.sun.star.embed
from enum import IntFlag


class VerbAttributes(object):
    """
    Const Class

    The constant set specifies possible attributes of a verb.

    See Also:
        `API VerbAttributes <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1embed_1_1VerbAttributes.html>`_
    """
    MS_VERBATTR_NEVERDIRTIES = 1
    """
    Execution of the verb with this attribute must not modify the object.
    """
    MS_VERBATTR_ONCONTAINERMENU = 2
    """
    indicates that the verb should appear in the object's menu.
    """


class VerbAttributesEnum(IntFlag):
    """
    Enum of Const Class VerbAttributes

    The constant set specifies possible attributes of a verb.
    """
    MS_VERBATTR_NEVERDIRTIES = VerbAttributes.MS_VERBATTR_NEVERDIRTIES
    """
    Execution of the verb with this attribute must not modify the object.
    """
    MS_VERBATTR_ONCONTAINERMENU = VerbAttributes.MS_VERBATTR_ONCONTAINERMENU
    """
    indicates that the verb should appear in the object's menu.
    """

__all__ = ['VerbAttributes', 'VerbAttributesEnum']
