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


class CrossReference(object):
    """
    Struct Class

    This struct contains information describing a cross reference.
    
    Such references are kept by news servers for managing articles contained in multiple groups. An article can have a sequence of cross references.

    See Also:
        `API CrossReference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1CrossReference.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.CrossReference'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.CrossReference'
    """Literal Constant ``com.sun.star.ucb.CrossReference``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``CrossReference`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``CrossReference``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Group (str, optional): Group value
            Id (int, optional): Id value
        """
        self._group = None
        self._id = None

        key_order = ('Group', 'Id')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], CrossReference):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("CrossReference.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Group(self) -> str:
        """
        The name of a news group.
        """
        return self._group
    
    @Group.setter
    def Group(self, value: str) -> None:
        self._group = value

    @property
    def Id(self) -> int:
        """
        The unique identifier (relative to the server) of an article in the given group.
        """
        return self._id
    
    @Id.setter
    def Id(self, value: int) -> None:
        self._id = value


__all__ = ['CrossReference']
