# coding: utf-8
from abc import ABC, abstractmethod, abstractproperty
from typing import Dict, Tuple
from ..args.event_args import ControlEventArgs, ControlCancelEventArgs


class IUnoControl(ABC):

    @abstractproperty
    def uno_default_control(self) -> str:
        """Then name of the control such as com.sun.star.awt.UnoControlButtonModel"""
    @abstractmethod
    def _get_property_names() -> Tuple[str]:
        """gets propert names of control"""

    @abstractmethod
    def _on_before_property_assign(seff, args: ControlCancelEventArgs):
        """on before propery assigned"""

    @abstractmethod
    def _on_after_property_assign(self, args: ControlEventArgs):
        """on after propery assigned"""

    @abstractmethod
    def gen_control_dict(self) -> Dict[str, object]:
        """Gets controls properties as a dictionary"""

    @abstractmethod
    def auto_fill_properties(self, obj: object):
        """
        Set all matching propeties of this instance with the property values from ``obj``

        Args:
            obj (object): Object containing matching properties
        """
