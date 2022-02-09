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
# Namespace: com.sun.star.inspection
# Libre Office Version: 7.2


class PropertyCategoryDescriptor(object):
    """
    Struct Class

    describes a category of properties
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API PropertyCategoryDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1inspection_1_1PropertyCategoryDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.inspection'
    __ooo_full_ns__: str = 'com.sun.star.inspection.PropertyCategoryDescriptor'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.inspection.PropertyCategoryDescriptor'
    """Literal Constant ``com.sun.star.inspection.PropertyCategoryDescriptor``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``PropertyCategoryDescriptor`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``PropertyCategoryDescriptor``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ProgrammaticName (str, optional): ProgrammaticName value
            UIName (str, optional): UIName value
            HelpURL (str, optional): HelpURL value
        """
        self._programmatic_name = None
        self._ui_name = None
        self._help_url = None

        key_order = ('ProgrammaticName', 'UIName', 'HelpURL')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], PropertyCategoryDescriptor):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("PropertyCategoryDescriptor.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def ProgrammaticName(self) -> str:
        """
        contains the programmatic name of the category.
        
        This programmatic name is used internally: XPropertyHandler.describePropertyLine() sets a programmatic category name at LineDescriptor.Category, and an object inspector uses this to find the proper PropertyCategoryDescriptor.
        """
        return self._programmatic_name
    
    @ProgrammaticName.setter
    def ProgrammaticName(self, value: str) -> None:
        self._programmatic_name = value

    @property
    def UIName(self) -> str:
        """
        provides a human-readable name (which can be presented at the UI) for a category.
        """
        return self._ui_name
    
    @UIName.setter
    def UIName(self, value: str) -> None:
        self._ui_name = value

    @property
    def HelpURL(self) -> str:
        """
        provides a help URL to be associated with a category
        """
        return self._help_url
    
    @HelpURL.setter
    def HelpURL(self, value: str) -> None:
        self._help_url = value


__all__ = ['PropertyCategoryDescriptor']
