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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
import typing
from .numbered_sorting_info import NumberedSortingInfo as NumberedSortingInfo_fd0e0de6
from .open_command_argument import OpenCommandArgument as OpenCommandArgument_fb0a0dd6


class OpenCommandArgument2(OpenCommandArgument_fb0a0dd6):
    """
    Struct Class

    The argument for commands like \"open\", \"update\", and \"synchronize\".
    
    This struct extends the original OpenCommandArgument, which must not be changed for compatibility reasons.

    See Also:
        `API OpenCommandArgument2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1OpenCommandArgument2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.OpenCommandArgument2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.OpenCommandArgument2'
    """Literal Constant ``com.sun.star.ucb.OpenCommandArgument2``"""

    SortingInfo: typing.TypeAlias = typing.Tuple[NumberedSortingInfo_fd0e0de6, ...]
    """
    The sort criteria for the rows of the returned ContentResultSet.
    
    The result set implementation may ignore this parameter, if it cannot sort the data by the given criteria in an efficient way (i.e. directly using the underlying data source -> SQL-database -> ORDER BY).
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``OpenCommandArgument2`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``OpenCommandArgument2``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
        """

        key_order = ()
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], OpenCommandArgument2):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("OpenCommandArgument2.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


__all__ = ['OpenCommandArgument2']
