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
from .transfer_info import TransferInfo as TransferInfo_a4600b13


class TransferInfo2(TransferInfo_a4600b13):
    """
    Struct Class

    extends TransferInfo structure to give some additional parameters for transfers.

    See Also:
        `API TransferInfo2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1TransferInfo2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.TransferInfo2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.TransferInfo2'
    """Literal Constant ``com.sun.star.ucb.TransferInfo2``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``TransferInfo2`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``TransferInfo2``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            MimeType (str, optional): MimeType value
        """
        self._mime_type = None

        key_order = ('MimeType',)
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], TransferInfo2):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("TransferInfo2.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def MimeType(self) -> str:
        """
        contains the MIME type of the source of the action
        """
        return self._mime_type
    
    @MimeType.setter
    def MimeType(self, value: str) -> None:
        self._mime_type = value


__all__ = ['TransferInfo2']
