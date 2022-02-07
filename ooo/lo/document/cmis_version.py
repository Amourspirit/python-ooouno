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
# Namespace: com.sun.star.document
# Libre Office Version: 7.2


class CmisVersion(object):
    """
    Struct Class

    specifies a CMIS document version.

    See Also:
        `API CmisVersion <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1CmisVersion.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.CmisVersion'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.document.CmisVersion'
    """Literal Constant ``com.sun.star.document.CmisVersion``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``CmisVersion`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``CmisVersion``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            Id (str, optional): Id value
            TimeStamp (object, optional): TimeStamp value
            Author (str, optional): Author value
            Comment (str, optional): Comment value
        """
        self._id = None
        self._time_stamp = None
        self._author = None
        self._comment = None

        key_order = ('Id', 'TimeStamp', 'Author', 'Comment')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], CmisVersion):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("CmisVersion.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def Id(self) -> str:
        """
        unique ID of the Cmis version
        """
        return self._id
    
    @Id.setter
    def Id(self, value: str) -> None:
        self._id = value

    @property
    def TimeStamp(self) -> object:
        """
        specifies the time when the revision was created.
        """
        return self._time_stamp
    
    @TimeStamp.setter
    def TimeStamp(self, value: object) -> None:
        self._time_stamp = value

    @property
    def Author(self) -> str:
        """
        contains the author that created the version.
        """
        return self._author
    
    @Author.setter
    def Author(self, value: str) -> None:
        self._author = value

    @property
    def Comment(self) -> str:
        """
        contains the comment the author has left.
        """
        return self._comment
    
    @Comment.setter
    def Comment(self, value: str) -> None:
        self._comment = value


__all__ = ['CmisVersion']
