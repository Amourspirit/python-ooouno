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
import typing
if typing.TYPE_CHECKING:
    from .outgoing_message_state import OutgoingMessageState as OutgoingMessageState_c200e54


class RecipientInfo(object):
    """
    Struct Class

    contains all information needed to send a message using one send protocol.
    
    To send one message via two different protocols, two RecipientInfos are needed - to send one message to different users with one protocol, one RecipientInfo can be used.

    See Also:
        `API RecipientInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1RecipientInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.RecipientInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.RecipientInfo'
    """Literal Constant ``com.sun.star.ucb.RecipientInfo``"""


    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``RecipientInfo`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``RecipientInfo``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ProtocolType (str, optional): ProtocolType value
            State (OutgoingMessageState, optional): State value
            To (str, optional): To value
            CC (str, optional): CC value
            BCC (str, optional): BCC value
            Newsgroups (str, optional): Newsgroups value
            Server (str, optional): Server value
            Username (str, optional): Username value
            Password (str, optional): Password value
            VIMPostOfficePath (str, optional): VIMPostOfficePath value
            ProtocolErrorString (str, optional): ProtocolErrorString value
            ProtocolErrorNumber (int, optional): ProtocolErrorNumber value
            SendTries (int, optional): SendTries value
        """
        self._protocol_type = None
        self._state = None
        self._to = None
        self._cc = None
        self._bcc = None
        self._newsgroups = None
        self._server = None
        self._username = None
        self._password = None
        self._vim_post_office_path = None
        self._protocol_error_string = None
        self._protocol_error_number = None
        self._send_tries = None

        key_order = ('ProtocolType', 'State', 'To', 'CC', 'BCC', 'Newsgroups', 'Server', 'Username', 'Password', 'VIMPostOfficePath', 'ProtocolErrorString', 'ProtocolErrorNumber', 'SendTries')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], RecipientInfo):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("RecipientInfo.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)

    @property
    def ProtocolType(self) -> str:
        """
        the protocol to use for sending (i.e.
        
        \"NNTP\", \"SMTP\", \"VIM\").
        """
        return self._protocol_type
    
    @ProtocolType.setter
    def ProtocolType(self, value: str) -> None:
        self._protocol_type = value

    @property
    def State(self) -> 'OutgoingMessageState_c200e54':
        """
        the current state of the message.
        """
        return self._state
    
    @State.setter
    def State(self, value: 'OutgoingMessageState_c200e54') -> None:
        self._state = value

    @property
    def To(self) -> str:
        """
        the recipient(s) (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """
        return self._to
    
    @To.setter
    def To(self, value: str) -> None:
        self._to = value

    @property
    def CC(self) -> str:
        """
        the recipient(s) of a \"carbon copy\" (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """
        return self._cc
    
    @CC.setter
    def CC(self, value: str) -> None:
        self._cc = value

    @property
    def BCC(self) -> str:
        """
        the recipient(s) of \"blind carbon copy\" (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """
        return self._bcc
    
    @BCC.setter
    def BCC(self, value: str) -> None:
        self._bcc = value

    @property
    def Newsgroups(self) -> str:
        """
        the newsgroup(s) to which an article is be posted.
        
        Multiple addresses are separated by commas.
        """
        return self._newsgroups
    
    @Newsgroups.setter
    def Newsgroups(self, value: str) -> None:
        self._newsgroups = value

    @property
    def Server(self) -> str:
        """
        the name of the server to be used for sending the message.
        """
        return self._server
    
    @Server.setter
    def Server(self, value: str) -> None:
        self._server = value

    @property
    def Username(self) -> str:
        """
        the user name to be used for authorizing on the send server.
        """
        return self._username
    
    @Username.setter
    def Username(self, value: str) -> None:
        self._username = value

    @property
    def Password(self) -> str:
        """
        the password to be used for authorizing on the send server.
        """
        return self._password
    
    @Password.setter
    def Password(self, value: str) -> None:
        self._password = value

    @property
    def VIMPostOfficePath(self) -> str:
        """
        the Post Office Path (VIM only).
        """
        return self._vim_post_office_path
    
    @VIMPostOfficePath.setter
    def VIMPostOfficePath(self, value: str) -> None:
        self._vim_post_office_path = value

    @property
    def ProtocolErrorString(self) -> str:
        """
        string representing the last error (generated by send server).
        """
        return self._protocol_error_string
    
    @ProtocolErrorString.setter
    def ProtocolErrorString(self, value: str) -> None:
        self._protocol_error_string = value

    @property
    def ProtocolErrorNumber(self) -> int:
        """
        the number representing the last error (generated by send server).
        """
        return self._protocol_error_number
    
    @ProtocolErrorNumber.setter
    def ProtocolErrorNumber(self, value: int) -> None:
        self._protocol_error_number = value

    @property
    def SendTries(self) -> int:
        """
        the count of tries to send a message.
        
        This count is 1 if the message was sent with the first try and increases with every unsuccessful retry.
        """
        return self._send_tries
    
    @SendTries.setter
    def SendTries(self, value: int) -> None:
        self._send_tries = value


__all__ = ['RecipientInfo']
