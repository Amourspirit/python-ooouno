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
# Namespace: com.sun.star.sdb
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .single_select_query_analyzer import SingleSelectQueryAnalyzer as SingleSelectQueryAnalyzer_577c105f
from .x_single_select_query_composer import XSingleSelectQueryComposer as XSingleSelectQueryComposer_66e310b9

class SingleSelectQueryComposer(SingleSelectQueryAnalyzer_577c105f, XPropertySet_bc180bfa, XSingleSelectQueryComposer_66e310b9):
    """
    Service Class

    represents a service for composing a single select statement.
    
    It hides the complexity of parsing and evaluating a single select statement and provides sophisticated methods for expanding a statement with filter, group by, having and order criteria. To get the new extended statement use the methods from com.sun.star.sdb.SingleSelectQueryAnalyzer.
    
    A SingleSelectQueryComposer is usually obtained from a Connection using the com.sun.star.lang.XMultiServiceFactory interface.

    See Also:
        `API SingleSelectQueryComposer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1SingleSelectQueryComposer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.SingleSelectQueryComposer'
    __ooo_type_name__: str = 'service'



__all__ = ['SingleSelectQueryComposer']

