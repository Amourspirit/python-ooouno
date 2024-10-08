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


class CheckinArgument(object):
    """
    Struct Class

    contains information needed to checkin a document.
    
    The checkin command is always called on the target private working copy document.

    See Also:
        `API CheckinArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1CheckinArgument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.CheckinArgument'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.CheckinArgument'
    """Literal Constant ``com.sun.star.ucb.CheckinArgument``"""

    def __init__(self, MajorVersion: typing.Optional[bool] = False, VersionComment: typing.Optional[str] = '', SourceURL: typing.Optional[str] = '', TargetURL: typing.Optional[str] = '', NewTitle: typing.Optional[str] = '', MimeType: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            MajorVersion (bool, optional): MajorVersion value.
            VersionComment (str, optional): VersionComment value.
            SourceURL (str, optional): SourceURL value.
            TargetURL (str, optional): TargetURL value.
            NewTitle (str, optional): NewTitle value.
            MimeType (str, optional): MimeType value.
        """
        super().__init__()

        if isinstance(MajorVersion, CheckinArgument):
            oth: CheckinArgument = MajorVersion
            self.MajorVersion = oth.MajorVersion
            self.VersionComment = oth.VersionComment
            self.SourceURL = oth.SourceURL
            self.TargetURL = oth.TargetURL
            self.NewTitle = oth.NewTitle
            self.MimeType = oth.MimeType
            return

        kargs = {
            "MajorVersion": MajorVersion,
            "VersionComment": VersionComment,
            "SourceURL": SourceURL,
            "TargetURL": TargetURL,
            "NewTitle": NewTitle,
            "MimeType": MimeType,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._major_version = kwargs["MajorVersion"]
        self._version_comment = kwargs["VersionComment"]
        self._source_url = kwargs["SourceURL"]
        self._target_url = kwargs["TargetURL"]
        self._new_title = kwargs["NewTitle"]
        self._mime_type = kwargs["MimeType"]


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
    def VersionComment(self) -> str:
        """
        Contains the version comment to set during the checkin.
        """
        return self._version_comment

    @VersionComment.setter
    def VersionComment(self, value: str) -> None:
        self._version_comment = value

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
    def MimeType(self) -> str:
        """
        contains the Mime-Type of the content to check-in as it may be different from the original one.
        """
        return self._mime_type

    @MimeType.setter
    def MimeType(self, value: str) -> None:
        self._mime_type = value


__all__ = ['CheckinArgument']
