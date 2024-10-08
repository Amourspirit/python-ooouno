# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..beans.property import Property as Property_8f4e0a76


class ContentInfo(object):
    """
    Struct Class

    A structure for information about contents.

    See Also:
        `API ContentInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1ContentInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.ContentInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.ContentInfo'
    """Literal Constant ``com.sun.star.ucb.ContentInfo``"""

    def __init__(self, Type: typing.Optional[str] = '', Attributes: typing.Optional[int] = 0, Properties: typing.Optional[typing.Tuple[Property_8f4e0a76, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Type (str, optional): Type value.
            Attributes (int, optional): Attributes value.
            Properties (typing.Tuple[Property, ...], optional): Properties value.
        """
        super().__init__()

        if isinstance(Type, ContentInfo):
            oth: ContentInfo = Type
            self.Type = oth.Type
            self.Attributes = oth.Attributes
            self.Properties = oth.Properties
            return

        kargs = {
            "Type": Type,
            "Attributes": Attributes,
            "Properties": Properties,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._type = kwargs["Type"]
        self._attributes = kwargs["Attributes"]
        self._properties = kwargs["Properties"]


    @property
    def Type(self) -> str:
        """
        A type identifier string for a content.
        
        This is an implementation specific string characterizing the kind of a content (e.g. \"application/vnd.sun.star.hierarchy-link\"). The value of this member should match the value returned by XContent.getContentType() of an appropriate content.
        """
        return self._type

    @Type.setter
    def Type(self, value: str) -> None:
        self._type = value

    @property
    def Attributes(self) -> int:
        """
        Additional attributes.
        
        These flags contain extra information on the content, like its kind (KIND_FOLDER, KIND_DOCUMENT, KIND_LINK).
        
        It is highly recommended to fill these flags very accurately, as they are very important when transferring contents between different ContentProviders.
        
        The value can be one of the ContentInfoAttribute constants.
        """
        return self._attributes

    @Attributes.setter
    def Attributes(self, value: int) -> None:
        self._attributes = value

    @property
    def Properties(self) -> typing.Tuple[Property_8f4e0a76, ...]:
        """
        This field contains a list with the properties which must be set at a content that was just created using XContentCreator.createNewContent() before it can be committed (by executing the command \"insert\" at the new content).
        
        If one of the properties is missing, the insert command will fail.
        
        In example, a new file system folder content will need a title. The Properties member of the ContentInfo provided for this kind of content must include the property \"Title\".
        
        Important: The required properties must have one of the following basic data types (in order to make it possible to implement client applications with a small set of generic input methods for the values):
        """
        return self._properties

    @Properties.setter
    def Properties(self, value: typing.Tuple[Property_8f4e0a76, ...]) -> None:
        self._properties = value


__all__ = ['ContentInfo']
