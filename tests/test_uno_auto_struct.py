import os
from typing import Optional, TYPE_CHECKING
from ooo_uno.oenv import UNO_ENVIRONMENT
from ooo_uno.uno_obj.beans.property_state import PropertyState
if TYPE_CHECKING:
    from ooo_uno.uno_obj.beans.property_state import PropertyState as PropertyState_c97b0c77
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ooo_uno.helper import uno_helper


class PropertyValue(object):
    """
    specifies a property value.

    See Also:
        `API PropertyValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyValue.html>`_

    """

    def __init__(self, Handle: Optional[int] = None, Name: Optional[str] = None, State: 'Optional[PropertyState_c97b0c77]' = None, Value: Optional[object] = None):
        self._handle = Handle
        self._name = Name
        self._state = State
        self._value = Value

    @property
    def Handle(self) -> int:
        """
        contains an implementation-specific handle for the property.
        
        It may be -1 if the implementation has no handle. If available it can be used for fast lookups.
        """
        return self._handle

    @Handle.setter
    def Handle(self, value: int) -> None:
        self._handle = value

    @property
    def Name(self) -> str:
        """
        specifies the name of the property.
        
        The name is unique within a sequence of PropertyValues. Upper and lower case are distinguished.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def State(self) -> 'PropertyState_c97b0c77':
        """
        determines if the value comes from the object itself or from a default and if the value cannot be determined exactly.
        """
        return self._state

    @State.setter
    def State(self, value: 'PropertyState_c97b0c77') -> None:
        self._state = value

    @property
    def Value(self) -> object:
        """
        contains the value of the property or VOID, if no value is available.
        """
        return self._value

    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value


class PropertyValue2(object):
    """
    specifies a property value.

    See Also:
        `API PropertyValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyValue.html>`_

    """

    Handle: int
    """
    contains an implementation-specific handle for the property.
    
    It may be -1 if the implementation has no handle. If available it can be used for fast lookups.
    """

    Name: str
    """
    specifies the name of the property.
    
    The name is unique within a sequence of PropertyValues. Upper and lower case are distinguished.
    """
    
    State: 'PropertyState_c97b0c77'
    """
    determines if the value comes from the object itself or from a default and if the value cannot be determined exactly.
    """

    Value: object
    """
    contains the value of the property or VOID, if no value is available.
    """

def _dynamic_struct() -> None:
    global PropertyValue
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
        order = ('Handle', 'Name', 'State', 'Value')
        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct(
                'com.sun.star.beans.PropertyValue')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        PropertyValue = _struct_init

if UNO_ENVIRONMENT:
    _dynamic_struct()

def test_property_value() -> None:
    pv: PropertyValue = PropertyValue()
    pv.Name = 'MyName'
    pv.Value = 2
    assert pv.Name == 'MyName'
    assert pv.Value == 2
    
    pv: PropertyValue = PropertyValue(3, 'hello', None, 22)
    assert pv.Handle == 3
    assert pv.Name == 'hello'
    assert pv.State == PropertyState.DIRECT_VALUE
    assert pv.Value == 22

    pv: PropertyValue = PropertyValue(Name='hello', Value=22, State=PropertyState.DEFAULT_VALUE)
    assert pv.Name == 'hello'
    assert pv.State == PropertyState.DEFAULT_VALUE
    assert pv.Value == 22
