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
from ooo_uno.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not typing.TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True
    from ooo_uno.helper import uno_helper

if typing.TYPE_CHECKING or _DYNAMIC is False:


    class CheckinArgument(object):
        """
        Struct Class

        contains information needed to checkin a document.
        
        The checkin command is always called on the target private working copy document.

        See Also:
            `API CheckinArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1CheckinArgument.html>`_


        Note:
            | At runtime CheckinArgument will be an actual uno struct however can seamlessly be treated as a regualr class.
            | At design time a class is presumed. This allows for better typings.
            | CheckinArgument is a callable and can be treatead as a class and create instances.
        """

        def __init__(self, MajorVersion: typing.Optional[bool] = None, MimeType: typing.Optional[str] = None, NewTitle: typing.Optional[str] = None, SourceURL: typing.Optional[str] = None, TargetURL: typing.Optional[str] = None, VersionComment: typing.Optional[str] = None):
            self._major_version = MajorVersion
            self._mime_type = MimeType
            self._new_title = NewTitle
            self._source_url = SourceURL
            self._target_url = TargetURL
            self._version_comment = VersionComment

        @property
        def MajorVersion(self) -> bool:
            """
            Tells whether to create a new major or minor version during the checkin.
            """
            return self._major_version
        
        @MajorVersion.setter
        def MajorVersion(self, value: bool) -> None:
            self._major_version = value

        @property
        def MimeType(self) -> str:
            """
            contains the Mime-Type of the content to check-in as it may be different from the original one.
            """
            return self._mime_type
        
        @MimeType.setter
        def MimeType(self, value: str) -> None:
            self._mime_type = value

        @property
        def NewTitle(self) -> str:
            """
            contains the title of the transferred object, if it is different from the original one.
            
            If this field is filled, for example, a file will be renamed while it is being checked in.
            """
            return self._new_title
        
        @NewTitle.setter
        def NewTitle(self, value: str) -> None:
            self._new_title = value

        @property
        def SourceURL(self) -> str:
            """
            contains the URL of the source of the action (e.g.
            
            the URL of the temporary file to checkin).
            """
            return self._source_url
        
        @SourceURL.setter
        def SourceURL(self, value: str) -> None:
            self._source_url = value

        @property
        def TargetURL(self) -> str:
            """
            contains the URL of the private working copy to checkin.
            """
            return self._target_url
        
        @TargetURL.setter
        def TargetURL(self, value: str) -> None:
            self._target_url = value

        @property
        def VersionComment(self) -> str:
            """
            Contains the version comment to set during the checkin.
            """
            return self._version_comment
        
        @VersionComment.setter
        def VersionComment(self, value: str) -> None:
            self._version_comment = value

if not typing.TYPE_CHECKING and _DYNAMIC:
    def _dynamic_struct() -> None:
        # Dynamically create uno struct using uno
        global CheckinArgument
        order = ('MajorVersion', 'MimeType', 'NewTitle', 'SourceURL', 'TargetURL', 'VersionComment')

        def _struct_init(*args, **kwargs):
            struct = uno_helper.create_uno_struct('com.sun.star.ucb.CheckinArgument')
            for i, arg in enumerate(args):
                if arg is None:
                    continue
                setattr(struct, order[i], arg)
            for k, v in kwargs.items():
                setattr(struct, k, v)
            return struct
        CheckinArgument = _struct_init

    _dynamic_struct()

__all__ = ['CheckinArgument']
