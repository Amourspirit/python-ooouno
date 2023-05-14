# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.packages.zip
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import uno
import typing


class ZipEntry(object):
    """
    Struct Class

    used to represent a ZIP file entry
    
    This interface is an IDL version of the Java interface java.util.zip.ZipFile with some minor adaptations.

    See Also:
        `API ZipEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1packages_1_1zip_1_1ZipEntry.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.packages.zip'
    __ooo_full_ns__: str = 'com.sun.star.packages.zip.ZipEntry'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.packages.zip.ZipEntry'
    """Literal Constant ``com.sun.star.packages.zip.ZipEntry``"""

    def __init__(self, extra: typing.Optional[uno.ByteSequence] = UNO_NONE, nVersion: typing.Optional[int] = 0, nFlag: typing.Optional[int] = 0, nMethod: typing.Optional[int] = 0, nTime: typing.Optional[int] = 0, nCrc: typing.Optional[int] = 0, nCompressedSize: typing.Optional[int] = 0, nSize: typing.Optional[int] = 0, nOffset: typing.Optional[int] = 0, nDiskNumber: typing.Optional[int] = 0, sName: typing.Optional[str] = '', sComment: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            extra (uno.ByteSequence, optional): extra value.
            nVersion (int, optional): nVersion value.
            nFlag (int, optional): nFlag value.
            nMethod (int, optional): nMethod value.
            nTime (int, optional): nTime value.
            nCrc (int, optional): nCrc value.
            nCompressedSize (int, optional): nCompressedSize value.
            nSize (int, optional): nSize value.
            nOffset (int, optional): nOffset value.
            nDiskNumber (int, optional): nDiskNumber value.
            sName (str, optional): sName value.
            sComment (str, optional): sComment value.
        """
        super().__init__()

        if isinstance(extra, ZipEntry):
            oth: ZipEntry = extra
            self.extra = oth.extra
            self.nVersion = oth.nVersion
            self.nFlag = oth.nFlag
            self.nMethod = oth.nMethod
            self.nTime = oth.nTime
            self.nCrc = oth.nCrc
            self.nCompressedSize = oth.nCompressedSize
            self.nSize = oth.nSize
            self.nOffset = oth.nOffset
            self.nDiskNumber = oth.nDiskNumber
            self.sName = oth.sName
            self.sComment = oth.sComment
            return

        kargs = {
            "extra": extra,
            "nVersion": nVersion,
            "nFlag": nFlag,
            "nMethod": nMethod,
            "nTime": nTime,
            "nCrc": nCrc,
            "nCompressedSize": nCompressedSize,
            "nSize": nSize,
            "nOffset": nOffset,
            "nDiskNumber": nDiskNumber,
            "sName": sName,
            "sComment": sComment,
        }
        if kargs["extra"] is UNO_NONE:
            kargs["extra"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._extra = kwargs["extra"]
        self._n_version = kwargs["nVersion"]
        self._n_flag = kwargs["nFlag"]
        self._n_method = kwargs["nMethod"]
        self._n_time = kwargs["nTime"]
        self._n_crc = kwargs["nCrc"]
        self._n_compressed_size = kwargs["nCompressedSize"]
        self._n_size = kwargs["nSize"]
        self._n_offset = kwargs["nOffset"]
        self._n_disk_number = kwargs["nDiskNumber"]
        self._s_name = kwargs["sName"]
        self._s_comment = kwargs["sComment"]


    @property
    def extra(self) -> uno.ByteSequence:
        """
        optional extra field data for entry
        """
        return self._extra

    @extra.setter
    def extra(self, value: uno.ByteSequence) -> None:
        self._extra = value

    @property
    def nVersion(self) -> int:
        """
        version needed to extract
        """
        return self._n_version

    @nVersion.setter
    def nVersion(self, value: int) -> None:
        self._n_version = value

    @property
    def nFlag(self) -> int:
        """
        bit flags
        """
        return self._n_flag

    @nFlag.setter
    def nFlag(self, value: int) -> None:
        self._n_flag = value

    @property
    def nMethod(self) -> int:
        """
        compression method
        """
        return self._n_method

    @nMethod.setter
    def nMethod(self, value: int) -> None:
        self._n_method = value

    @property
    def nTime(self) -> int:
        """
        modification time
        """
        return self._n_time

    @nTime.setter
    def nTime(self, value: int) -> None:
        self._n_time = value

    @property
    def nCrc(self) -> int:
        """
        CRC-32 of entry data.
        """
        return self._n_crc

    @nCrc.setter
    def nCrc(self, value: int) -> None:
        self._n_crc = value

    @property
    def nCompressedSize(self) -> int:
        """
        uncompressed size of entry data
        """
        return self._n_compressed_size

    @nCompressedSize.setter
    def nCompressedSize(self, value: int) -> None:
        self._n_compressed_size = value

    @property
    def nSize(self) -> int:
        """
        uncompressed size of entry data
        """
        return self._n_size

    @nSize.setter
    def nSize(self, value: int) -> None:
        self._n_size = value

    @property
    def nOffset(self) -> int:
        """
        offset of LOC header
        """
        return self._n_offset

    @nOffset.setter
    def nOffset(self, value: int) -> None:
        self._n_offset = value

    @property
    def nDiskNumber(self) -> int:
        """
        The number of the disk this entry is saved on.
        """
        return self._n_disk_number

    @nDiskNumber.setter
    def nDiskNumber(self, value: int) -> None:
        self._n_disk_number = value

    @property
    def sName(self) -> str:
        """
        the entry name
        """
        return self._s_name

    @sName.setter
    def sName(self, value: str) -> None:
        self._s_name = value

    @property
    def sComment(self) -> str:
        """
        optional comment
        """
        return self._s_comment

    @sComment.setter
    def sComment(self, value: str) -> None:
        self._s_comment = value


__all__ = ['ZipEntry']
