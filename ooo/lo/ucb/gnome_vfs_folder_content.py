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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ucb
from __future__ import annotations
from ..beans.x_properties_change_notifier import XPropertiesChangeNotifier as XPropertiesChangeNotifier_7a7b111c
from ..beans.x_property_container import XPropertyContainer as XPropertyContainer_c600e71
from ..beans.x_property_set_info_change_notifier import XPropertySetInfoChangeNotifier as XPropertySetInfoChangeNotifier_d524130c
from ..container.x_child import XChild as XChild_a6390b07
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from .x_command_info_change_notifier import XCommandInfoChangeNotifier as XCommandInfoChangeNotifier_6358106b
from .x_command_processor import XCommandProcessor as XCommandProcessor_dfe80d19
from .x_command_processor2 import XCommandProcessor2 as XCommandProcessor2_ed330d4b
from .x_content import XContent as XContent_79db0975
from .x_content_creator import XContentCreator as XContentCreator_c6b80c45

class GnomeVFSFolderContent(XPropertiesChangeNotifier_7a7b111c, XPropertyContainer_c600e71, XPropertySetInfoChangeNotifier_d524130c, XChild_a6390b07, XComponent_98dc0ab5, XCommandInfoChangeNotifier_6358106b, XCommandProcessor2_ed330d4b, XCommandProcessor_dfe80d19, XContent_79db0975, XContentCreator_c6b80c45):
    """
    Service Class

    A DCP Folder is a container for other DCP Folders or Documents.

    See Also:
        `API GnomeVFSFolderContent <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1GnomeVFSFolderContent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.GnomeVFSFolderContent'
    __ooo_type_name__: str = 'service'


__all__ = ['GnomeVFSFolderContent']

