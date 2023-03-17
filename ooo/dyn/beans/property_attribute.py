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
# Libre Office Version: 7.4
# Namespace: com.sun.star.beans
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class PropertyAttribute(metaclass=UnoConstMeta, type_name="com.sun.star.beans.PropertyAttribute", name_space="com.sun.star.beans"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.beans.PropertyAttribute``"""
        pass

    class PropertyAttributeEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.beans.PropertyAttribute", name_space="com.sun.star.beans"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.beans.PropertyAttribute`` as Enum values"""
        pass

else:
    from ...lo.beans.property_attribute import PropertyAttribute as PropertyAttribute

    class PropertyAttributeEnum(IntFlag):
        """
        Enum of Const Class PropertyAttribute

        These values are used to specify the behavior of a Property.
        
        **since**
        
            OOo 1.1.2
        """
        MAYBEVOID = PropertyAttribute.MAYBEVOID
        """
        indicates that a property value can be void.
        
        It does not mean that the type of the property is void!
        """
        BOUND = PropertyAttribute.BOUND
        """
        indicates that a PropertyChangeEvent will be fired to all registered XPropertyChangeListeners whenever the value of this property changes.
        """
        CONSTRAINED = PropertyAttribute.CONSTRAINED
        """
        indicates that a PropertyChangeEvent will be fired to all registered XVetoableChangeListeners whenever the value of this property is about to change.
        """
        TRANSIENT = PropertyAttribute.TRANSIENT
        """
        indicates that the value of the property is not persistent.
        """
        READONLY = PropertyAttribute.READONLY
        """
        indicates that the value of the property is read-only.
        """
        MAYBEAMBIGUOUS = PropertyAttribute.MAYBEAMBIGUOUS
        """
        indicates that the value of the property can be ambiguous.
        """
        MAYBEDEFAULT = PropertyAttribute.MAYBEDEFAULT
        """
        indicates that the property can be set to default.
        """
        REMOVABLE = PropertyAttribute.REMOVABLE
        """
        indicates that the property can be removed (i.e., by calling XPropertyContainer.removeProperty()).
        """
        REMOVEABLE = PropertyAttribute.REMOVEABLE
        OPTIONAL = PropertyAttribute.OPTIONAL
        """
        indicates that a property is optional.
        
        This attribute is not of interest for concrete property implementations. It's needed for property specifications inside service specifications in UNOIDL.
        
        **since**
        
            OOo 1.1.2
        """

__all__ = ['PropertyAttribute', 'PropertyAttributeEnum']
