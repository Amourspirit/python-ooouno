# coding: utf-8
from kwhelp.decorator import AcceptedTypes, DecFuncEnum, TypeCheckKw


class ControlEventArgs:
    """Base Class of control events"""
    def __init__(self, **kwargs):
        """
        Constructor

        Keyword Args:
            name (str, Optional): Name of the property
            value (obj, optional): Value of the property
        """
        self._property_name: str = kwargs.get("name", "")
        self._property_value = kwargs.get("value", None)

    @property
    def property_name(self) -> str:
        """
        Specifies property_name

        :getter: Gets property_name value.
        :setter: Sets property_name value.
        """
        return self._property_name

    @property_name.setter
    def property_name(self, value: str):
        self._property_name = value

    @property
    def property_value(self) -> object:
        """Specifies property_value

            :getter: Gets property_value value.
            :setter: Sets property_value value.
        """
        return self._property_value

    @property_value.setter
    def property_value(self, value: object):
        self._property_value = value


class ControlCancelEventArgs(ControlEventArgs):
    """Control Cancel Event args"""

    def __init__(self, **kwargs):
        """
        Constructor

        Keyword Args:
            name (str, Optional): Name of the property
            value (obj, optional): Value of the property
            
        """
        super().__init__(**kwargs)
        self._cancel = False

    @property
    def cancel(self) -> bool:
        """
        Specifies cancel

        :getter: Gets cancel value.
        :setter: Sets cancel value.
        """
        return self._cancel

    @cancel.setter
    def Cancel(self, value: bool):
        self._cancel = value
