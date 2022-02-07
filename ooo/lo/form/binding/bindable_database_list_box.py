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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.form.binding
from .bindable_data_aware_control_model import BindableDataAwareControlModel as BindableDataAwareControlModel_47091512
from ..component.database_list_box import DatabaseListBox as DatabaseListBox_6a371097

class BindableDatabaseListBox(BindableDataAwareControlModel_47091512, DatabaseListBox_6a371097):
    """
    Service Class

    This service specifies a list box model which is data-aware and thus can be bound to a database field, and additionally supports binding to arbitrary external values.
    
    There are six possible ways that a BindableDatabaseListBox exchanges values with an external binding. If a new binding is set at a BindableDatabaseListBox, the types from the following list are tried in descending order: The first type supported by the binding is used for data exchange.

    See Also:
        `API BindableDatabaseListBox <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1binding_1_1BindableDatabaseListBox.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.binding'
    __ooo_full_ns__: str = 'com.sun.star.form.binding.BindableDatabaseListBox'
    __ooo_type_name__: str = 'service'


__all__ = ['BindableDatabaseListBox']

