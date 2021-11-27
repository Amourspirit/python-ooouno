# coding: utf-8
from typing import Dict
from ..args.event_args import ControlEventArgs, ControlCancelEventArgs
from ..interface.control import IUnoControl

class UnoCtlGen(IUnoControl):
    
    def _on_before_property_assign(self, args: ControlCancelEventArgs):
        """on before propery assigned"""
        

    def _on_after_property_assign(self, args: ControlEventArgs):
        """on after propery assigned"""
    

    def gen_control_dict(self) -> Dict[str, object]:
        """Gets controls properties as a dictionary"""
        d = {}
        names = self._get_property_names()
        for name in names:
            value = getattr(self,name, None)
            c_args = ControlCancelEventArgs(name=name, value=value)
            self._on_before_property_assign(args=c_args)
            if c_args.Cancel == True:
                raise Exception(f"Control Property '{name}' was canceled from being process in '{self.__class__.__name__}'")
            if not value is None:
                d[name] = value
            e_args = ControlEventArgs(name=name,value=value)
            self._on_after_property_assign(args=e_args)
        return d
    
    def auto_fill_properties(self, obj: object):
        """
        Set all matching propeties of this instance with the property values from ``obj``

        Args:
            obj (object): Object containing matching properties
        """
        if obj is self:
            return
        names = self._get_property_names()
        def auto_fill(o:object, key: str, value: object):
            if hasattr(o, key) is False:
                return
            if isinstance(o, IUnoControl):
                o.auto_fill_properties(obj=value)
            elif isinstance(value, dict):
                for _k, _v in value.items():
                    auto_fill(o=value, key=_k, value=_v)
            setattr(o, key, value)
        for name in names:
            auto_fill(o=self, key=name, value=getattr(obj, name, None))
