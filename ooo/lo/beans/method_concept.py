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
# Namespace: com.sun.star.beans


class MethodConcept(object):
    """
    Const Class

    These constants are used to specify concepts of the introspection which apply to methods.
    
    This list is not necessarily complete; new constants may be added.

    See Also:
        `API MethodConcept <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1beans_1_1MethodConcept.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.MethodConcept'
    __ooo_type_name__: str = 'const'

    ALL = -1
    """
    This value is used to query for all methods, see XIntrospectionAccess.getMethod() and XIntrospectionAccess.getMethods()
    """
    DANGEROUS = 1
    """
    specifies methods which can result in an unstable state (i.e.
    
    deadlock, application crash, security hole, etc.) when called directly by the user.
    """
    PROPERTY = 2
    """
    specifies methods which are used to set and get the value of properties/attributes.
    
    These methods have the signature type get...() , void set...() or boolean is...() .
    """
    LISTENER = 4
    """
    specifies methods of the listener concept.
    
    These methods have the signature add...Listener()  or remove...Listener().
    """
    ENUMERATION = 8
    """
    specifies methods of the enumeration concept.
    
    These methods have the signature create...Enumeration and return an interface that is derived from com.sun.star.container.XEnumeration. Additionally, the method com.sun.star.container.XEnumerationAccess.getElementType() belongs to this concept.
    """
    NAMECONTAINER = 16
    """
    specifies methods of the name container concept.
    
    These methods have the signature get...ByName(), set...ByName(), replace...ByName(), remove...ByName(), has...ByName(), or get...Names. In addition, the method com.sun.star.container.XEnumerationAccess.getElementType() belongs to this concept.
    """
    INDEXCONTAINER = 32
    """
    specifies methods of the index container concept.
    
    These methods have the signature get...ByIndex(), insert...ByIndex(), replace...ByIndex(), or remove...ByIndex(). The method com.sun.star.container.XIndexAccess.getCount() also belongs to this concept.
    """

__all__ = ['MethodConcept']
