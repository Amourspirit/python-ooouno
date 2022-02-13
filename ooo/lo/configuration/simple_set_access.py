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
# Namespace: com.sun.star.configuration
from .x_template_container import XTemplateContainer as XTemplateContainer_928f11b7
from ..container.x_container import XContainer as XContainer_d6fb0cc6
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
from ..util.x_string_escape import XStringEscape as XStringEscape_bd090be6

class SimpleSetAccess(XTemplateContainer_928f11b7, XContainer_d6fb0cc6, XNameAccess_e2ab0cf6, XStringEscape_bd090be6):
    """
    Service Class

    provides access to a dynamic, homogeneous, nonhierarchical set of values or objects.
    
    Also provides information about the template for elements. Allows normalizing externally generated names.
    
    Sets are dynamic containers.
    
    The number and names of contained elements is not fixed in advance, but all elements have to be of one predetermined type.

    See Also:
        `API SimpleSetAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1SimpleSetAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.SimpleSetAccess'
    __ooo_type_name__: str = 'service'



__all__ = ['SimpleSetAccess']

