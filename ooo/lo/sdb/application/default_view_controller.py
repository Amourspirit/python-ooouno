# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb.application
from ...frame.controller import Controller as Controller_a5330b37
from ...frame.x_title import XTitle as XTitle_7ab0096d
from ...frame.x_title_change_broadcaster import XTitleChangeBroadcaster as XTitleChangeBroadcaster_5529101d
from .x_database_document_ui import XDatabaseDocumentUI as XDatabaseDocumentUI_be9c124d

class DefaultViewController(Controller_a5330b37, XTitle_7ab0096d, XTitleChangeBroadcaster_5529101d, XDatabaseDocumentUI_be9c124d):
    """
    Service Class

    is the default controller implementation for OpenOffice.org's database application.

    See Also:
        `API DefaultViewController <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1application_1_1DefaultViewController.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.application'
    __ooo_full_ns__: str = 'com.sun.star.sdb.application.DefaultViewController'
    __ooo_type_name__: str = 'service'


__all__ = ['DefaultViewController']

