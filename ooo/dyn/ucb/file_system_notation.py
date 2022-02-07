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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.ucb
from enum import IntEnum
from ...lo.ucb.file_system_notation import FileSystemNotation as FileSystemNotation


class FileSystemNotationEnum(IntEnum):
    """
    Enum of Const Class FileSystemNotation

    The notational conventions used to denote file system paths on different file systems or operating systems.
    """
    UNKNOWN_NOTATION = FileSystemNotation.UNKNOWN_NOTATION
    """
    No information regarding any conventions is available.
    """
    UNIX_NOTATION = FileSystemNotation.UNIX_NOTATION
    """
    The conventions of Unix like file systems (e.g., /dir1/dir2/file).
    """
    DOS_NOTATION = FileSystemNotation.DOS_NOTATION
    """
    The conventions of DOS like file systems (e.g., a:\\dir1\\dir2\\file or UNC notation like \\\\host\\dir1\\dir2\\file).
    """
    MAC_NOTATION = FileSystemNotation.MAC_NOTATION
    """
    The conventions of Mac like file systems (e.g., volume:dir1:dir2:file).
    """

__all__ = ['FileSystemNotation', 'FileSystemNotationEnum']
