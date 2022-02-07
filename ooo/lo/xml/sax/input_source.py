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
# Namespace: com.sun.star.xml.sax
# Libre Office Version: 7.2
import typing
if typing.TYPE_CHECKING:
    from ...io.x_input_stream import XInputStream as XInputStream_98d40ab4


class InputSource(object):
    """
    Struct Class

    specifies the Datasource plus some additional information for the parser.
    
    There are two places where the application will deliver this input source to the parser:

    See Also:
        `API InputSource <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1sax_1_1InputSource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.sax.InputSource'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.xml.sax.InputSource'
    """Literal Constant ``com.sun.star.xml.sax.InputSource``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``InputSource`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``InputSource``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            aInputStream (XInputStream, optional): aInputStream value
            sEncoding (str, optional): sEncoding value
            sPublicId (str, optional): sPublicId value
            sSystemId (str, optional): sSystemId value
        """
        self._a_input_stream = None
        self._s_encoding = None
        self._s_public_id = None
        self._s_system_id = None

        key_order = ('aInputStream', 'sEncoding', 'sPublicId', 'sSystemId')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], InputSource):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("InputSource.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def aInputStream(self) -> 'XInputStream_98d40ab4':
        """
        contains the byte input stream of the document.
        """
        return self._a_input_stream
    
    @aInputStream.setter
    def aInputStream(self, value: 'XInputStream_98d40ab4') -> None:
        self._a_input_stream = value

    @property
    def sEncoding(self) -> str:
        """
        contains the encoding of the data stream.
        
        This is used by the parser to do Unicode conversions.
        
        Note that in general you do not need to specify an encoding. Either it is UTF-8 or UTF-16 which is recognized by the parser or it is specified in the first line of the XML-File ( e.g. ?xml encoding=\"EUC-JP\"? ).
        """
        return self._s_encoding
    
    @sEncoding.setter
    def sEncoding(self, value: str) -> None:
        self._s_encoding = value

    @property
    def sPublicId(self) -> str:
        """
        contains the public Id of the document, for example, needed in exception-message strings.
        """
        return self._s_public_id
    
    @sPublicId.setter
    def sPublicId(self, value: str) -> None:
        self._s_public_id = value

    @property
    def sSystemId(self) -> str:
        """
        contains the system ID of the document.
        """
        return self._s_system_id
    
    @sSystemId.setter
    def sSystemId(self, value: str) -> None:
        self._s_system_id = value


__all__ = ['InputSource']
