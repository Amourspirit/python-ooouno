# coding: utf-8
from typing_extensions import TypeAlias
from .....uno_obj.beans.x_property_set import XPropertySet
from .....uno_obj.beans.x_fast_property_set import XFastPropertySet
from .....uno_obj.beans.x_property_change_listener import XPropertyChangeListener
from .....uno_obj.beans.x_vetoable_change_listener import XVetoableChangeListener
from .....uno_obj.beans.property_change_event import IPropertyChangeEvent
XPropertyChangeEvent: TypeAlias = IPropertyChangeEvent
