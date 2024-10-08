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
# Namespace: com.sun.star.awt


class PopupMenuDirection(object):
    """
    Const Class

    These values are used to specify the direction in which a pop-up menu will grow.
    
    They may be expanded in future versions.

    See Also:
        `API PopupMenuDirection <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1PopupMenuDirection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.PopupMenuDirection'
    __ooo_type_name__: str = 'const'

    EXECUTE_DEFAULT = 0
    """
    opens on execute in a default direction.
    """
    EXECUTE_DOWN = 1
    """
    opens on execute downwards.
    """
    EXECUTE_UP = 2
    """
    opens on execute upwards.
    """
    EXECUTE_LEFT = 4
    """
    opens on execute to the left.
    """
    EXECUTE_RIGHT = 8
    """
    opens on execute to the right.
    """

__all__ = ['PopupMenuDirection']
