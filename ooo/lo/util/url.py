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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
from ooo.oenv import UNO_NONE
import typing


class URL(object):
    """
    Struct Class

    represents the structure of a Uniform Resource Locator.
    
    If the structure represents a valid URL or not depends on prior usage of the functions of XURLTransformer. Only after one of the functions returned TRUE this can be assumed.
    It is not necessary to set all of the fields; either URL.Complete or (some of) the others are set. Additionally, most of the other fields, like URL.Host, URL.Port, URL.User, URL.Password, or URL.Mark, are optional.

    See Also:
        `API URL <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1URL.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.URL'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.URL'
    """Literal Constant ``com.sun.star.util.URL``"""

    def __init__(self, Complete: str = '', Main: str = '', Protocol: str = '', User: str = '', Password: str = '', Server: str = '', Port: int = 0, Path: str = '', Name: str = '', Arguments: str = '', Mark: str = '') -> None:
        """
        Constructor

        Other Arguments:
            ``Complete`` can be another ``URL`` instance,
                in which case other named args are ignored.

        Arguments:
            Complete (str, optional): Complete value
            Main (str, optional): Main value
            Protocol (str, optional): Protocol value
            User (str, optional): User value
            Password (str, optional): Password value
            Server (str, optional): Server value
            Port (int, optional): Port value
            Path (str, optional): Path value
            Name (str, optional): Name value
            Arguments (str, optional): Arguments value
            Mark (str, optional): Mark value
        """
        if isinstance(Complete, URL):
            oth: URL = Complete
            self._complete = oth.Complete
            self._main = oth.Main
            self._protocol = oth.Protocol
            self._user = oth.User
            self._password = oth.Password
            self._server = oth.Server
            self._port = oth.Port
            self._path = oth.Path
            self._name = oth.Name
            self._arguments = oth.Arguments
            self._mark = oth.Mark
            return
        else:
            self._complete = Complete
            self._main = Main
            self._protocol = Protocol
            self._user = User
            self._password = Password
            self._server = Server
            self._port = Port
            self._path = Path
            self._name = Name
            self._arguments = Arguments
            self._mark = Mark



    @property
    def Complete(self) -> str:
        """
        contains the string representation of the complete URL, for example, http://www.sun.de:8080/pub/test/foo.txt?a=b#xyz
        
        It is used as a central input/output or input parameter for the interfaces of XURLTransformer. The usage of one of the XURLTransformer function is mandatory to validate the URL. It cannot be assumed that URL.Complete represents always a valid URL!
        """
        return self._complete
    
    @Complete.setter
    def Complete(self, value: str) -> None:
        self._complete = value

    @property
    def Main(self) -> str:
        """
        contains the URL without a mark and without arguments, for example, http://www.sun.de:8080/pub/test/foo.txt
        """
        return self._main
    
    @Main.setter
    def Main(self, value: str) -> None:
        self._main = value

    @property
    def Protocol(self) -> str:
        """
        contains the protocol (scheme) of the URL, for example, \"http\"
        """
        return self._protocol
    
    @Protocol.setter
    def Protocol(self, value: str) -> None:
        self._protocol = value

    @property
    def User(self) -> str:
        """
        contains the user-identifier of the URL, for example, \"me\"
        """
        return self._user
    
    @User.setter
    def User(self, value: str) -> None:
        self._user = value

    @property
    def Password(self) -> str:
        """
        contains the users password of the URL, for example, \"pass\"
        """
        return self._password
    
    @Password.setter
    def Password(self, value: str) -> None:
        self._password = value

    @property
    def Server(self) -> str:
        """
        contains the server part of the URL, for example, \"www.sun.de\"
        """
        return self._server
    
    @Server.setter
    def Server(self, value: str) -> None:
        self._server = value

    @property
    def Port(self) -> int:
        """
        contains the port at the server of the URL, for example, \"8080\"
        """
        return self._port
    
    @Port.setter
    def Port(self, value: int) -> None:
        self._port = value

    @property
    def Path(self) -> str:
        """
        contains all segments but the last one of the hierarchical path of the URL, for example, \"/pub/test/\"
        """
        return self._path
    
    @Path.setter
    def Path(self, value: str) -> None:
        self._path = value

    @property
    def Name(self) -> str:
        """
        contains the last segment of the hierarchical path of the URL, for the above example, \"foo.txt\"
        
        Attention:A service implementing the XURLTransformer interface will normally not detect if the last segment is a folder or a file. So it is possible that the last segment describes a folder. If you want to be sure that a file URL that references a folder will be correctly put into the URL fields you should append a \"/\" at the end of the hierarchical path.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Arguments(self) -> str:
        """
        contains the arguments part of the URL, for example, \"a=b\"
        """
        return self._arguments
    
    @Arguments.setter
    def Arguments(self, value: str) -> None:
        self._arguments = value

    @property
    def Mark(self) -> str:
        """
        contains the mark part of the URL, for example, \"xyz\"
        """
        return self._mark
    
    @Mark.setter
    def Mark(self, value: str) -> None:
        self._mark = value


__all__ = ['URL']
