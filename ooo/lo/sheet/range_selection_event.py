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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from ..lang.event_object import EventObject as EventObject_a3d70b03


class RangeSelectionEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an event from range selection.

    See Also:
        `API RangeSelectionEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1RangeSelectionEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.RangeSelectionEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.RangeSelectionEvent'
    """Literal Constant ``com.sun.star.sheet.RangeSelectionEvent``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``RangeSelectionEvent`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``RangeSelectionEvent``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            RangeDescriptor (str, optional): RangeDescriptor value
        """
        self._range_descriptor = None

        key_order = ('RangeDescriptor',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], RangeSelectionEvent):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("RangeSelectionEvent.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def RangeDescriptor(self) -> str:
        """
        contains a textual representation of the selected range.
        """
        return self._range_descriptor
    
    @RangeDescriptor.setter
    def RangeDescriptor(self, value: str) -> None:
        self._range_descriptor = value


__all__ = ['RangeSelectionEvent']
