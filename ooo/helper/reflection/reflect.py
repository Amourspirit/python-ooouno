from __future__ import annotations
from typing import Any

from .. import uno_helper

# https://github.com/Amourspirit/python_ooo_dev_tools/blob/e17ca074f19980b021631c949e816f956d12441b/ooodev/adapter/reflection/the_type_description_manager_comp.py

class Reflect:
    """
    Class for managing reflection.
    """

    @staticmethod
    def get_const_info(const_name: str) -> Any:
        """
        Gets information on a specific fully qualified type

        Args:
            const_name (str): The name of the constant.

        Returns:
            Any: The constant value.
        """
        dm = uno_helper.get_the_core_reflection()

        if dm.hasByHierarchicalName(const_name):
            return dm.getByHierarchicalName(const_name)
        return None