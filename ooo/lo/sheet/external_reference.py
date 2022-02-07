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


class ExternalReference(object):
    """
    Struct Class

    Data structure to store information about an external reference.
    
    An external reference can be either a single cell reference, a cell range reference, or a named range.
    
    **since**
    
        OOo 3.1

    See Also:
        `API ExternalReference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1ExternalReference.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.ExternalReference'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.ExternalReference'
    """Literal Constant ``com.sun.star.sheet.ExternalReference``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``ExternalReference`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``ExternalReference``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Index (int, optional): Index value
            Reference (object, optional): Reference value
        """
        self._index = None
        self._reference = None

        key_order = ('Index', 'Reference')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], ExternalReference):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("ExternalReference.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Index(self) -> int:
        """
        Index of an externally linked document.
        
        Each externally-linked document has a unique index value.
        
        You can get the index value of an external document from the corresponding com.sun.star.sheet.ExternalDocLink instance through its attribute com.sun.star.sheet.ExternalDocLink.TokenIndex.
        """
        return self._index
    
    @Index.setter
    def Index(self, value: int) -> None:
        self._index = value

    @property
    def Reference(self) -> object:
        """
        Reference data.
        
        This can store either SingleReference for a single cell reference, ComplexReference for a cell range reference, or simply a string for a defined name.
        
        The SingleReference.Sheet member shall contain the index of the external sheet cache containing the values of the externally referenced cells.
        """
        return self._reference
    
    @Reference.setter
    def Reference(self, value: object) -> None:
        self._reference = value


__all__ = ['ExternalReference']
