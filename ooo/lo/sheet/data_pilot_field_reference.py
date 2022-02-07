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


class DataPilotFieldReference(object):
    """
    Struct Class

    controls how a data pilot field's results are shown in relation to a selected reference result.

    See Also:
        `API DataPilotFieldReference <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldReference.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotFieldReference'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.DataPilotFieldReference'
    """Literal Constant ``com.sun.star.sheet.DataPilotFieldReference``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DataPilotFieldReference`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DataPilotFieldReference``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ReferenceType (int, optional): ReferenceType value
            ReferenceField (str, optional): ReferenceField value
            ReferenceItemType (int, optional): ReferenceItemType value
            ReferenceItemName (str, optional): ReferenceItemName value
        """
        self._reference_type = None
        self._reference_field = None
        self._reference_item_type = None
        self._reference_item_name = None

        key_order = ('ReferenceType', 'ReferenceField', 'ReferenceItemType', 'ReferenceItemName')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DataPilotFieldReference):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DataPilotFieldReference.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def ReferenceType(self) -> int:
        """
        contains the type of the reference.
        """
        return self._reference_type
    
    @ReferenceType.setter
    def ReferenceType(self, value: int) -> None:
        self._reference_type = value

    @property
    def ReferenceField(self) -> str:
        """
        contains the reference field
        """
        return self._reference_field
    
    @ReferenceField.setter
    def ReferenceField(self, value: str) -> None:
        self._reference_field = value

    @property
    def ReferenceItemType(self) -> int:
        """
        selects between a named reference item and using the previous or next item for each item from the reference field.
        """
        return self._reference_item_type
    
    @ReferenceItemType.setter
    def ReferenceItemType(self, value: int) -> None:
        self._reference_item_type = value

    @property
    def ReferenceItemName(self) -> str:
        """
        contains the name of the reference item, when the DataPilotFieldReference.ReferenceItemType is NAMED otherwise is empty
        """
        return self._reference_item_name
    
    @ReferenceItemName.setter
    def ReferenceItemName(self, value: str) -> None:
        self._reference_item_name = value


__all__ = ['DataPilotFieldReference']
