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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.packages.zip
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ZipConstants(metaclass=UnoConstMeta, type_name="com.sun.star.packages.zip.ZipConstants", name_space="com.sun.star.packages.zip"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.packages.zip.ZipConstants``"""
        pass

    class ZipConstantsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.packages.zip.ZipConstants", name_space="com.sun.star.packages.zip"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.packages.zip.ZipConstants`` as Enum values"""
        pass

else:
    from ....lo.packages.zip.zip_constants import ZipConstants as ZipConstants

    class ZipConstantsEnum(IntEnum):
        """
        Enum of Const Class ZipConstants

        defines the constants used by the ZIP interfaces.
        """
        DEFLATED = ZipConstants.DEFLATED
        """
        Compression method for the deflate algorithm (the only one currently supported).
        """
        NO_COMPRESSION = ZipConstants.NO_COMPRESSION
        """
        Compression level for no compression.
        """
        BEST_SPEED = ZipConstants.BEST_SPEED
        """
        Compression level for fastest compression.
        """
        BEST_COMPRESSION = ZipConstants.BEST_COMPRESSION
        """
        Compression level for best compression.
        """
        DEFAULT_COMPRESSION = ZipConstants.DEFAULT_COMPRESSION
        """
        Default compression level.
        """
        FILTERED = ZipConstants.FILTERED
        """
        Compression strategy best used for data consisting mostly of small values with a somewhat random distribution.
        
        Forces more Huffman coding and less string matching.
        """
        HUFFMAN_ONLY = ZipConstants.HUFFMAN_ONLY
        """
        Compression strategy for Huffman coding only.
        """
        DEFAULT_STRATEGY = ZipConstants.DEFAULT_STRATEGY
        """
        Default compression strategy.
        """
        STORED = ZipConstants.STORED
        """
        entry is uncompressed
        """
        DEF_MEM_LEVEL = ZipConstants.DEF_MEM_LEVEL
        """
        entry is uncompressed
        """
        LOCSIG = ZipConstants.LOCSIG
        """
        Header Signature: \"PK\\003\\004\".
        """
        EXTSIG = ZipConstants.EXTSIG
        """
        Header Signature: \"PK\\007\\008\".
        """
        CENSIG = ZipConstants.CENSIG
        """
        Header Signature: \"PK\\001\\002\".
        """
        ENDSIG = ZipConstants.ENDSIG
        """
        Header Signature: \"PK\\005\\006\".
        """
        SPANSIG = ZipConstants.SPANSIG
        """
        Header Signature: \"PK\\007\\008\".
        """
        LOCHDR = ZipConstants.LOCHDR
        """
        LOC header size in bytes (including signatures)
        """
        EXTHDR = ZipConstants.EXTHDR
        """
        EXT header size in bytes (including signatures)
        """
        CENHDR = ZipConstants.CENHDR
        """
        CEN header size in bytes (including signatures)
        """
        ENDHDR = ZipConstants.ENDHDR
        """
        END header size in bytes (including signatures)
        """
        LOCVER = ZipConstants.LOCVER
        """
        LOC LOC LOC.
        
        LOC header field \"version needed to extract\" offset
        """
        LOCFLG = ZipConstants.LOCFLG
        """
        LOC header field \"general purpose bit flags\" offset.
        """
        LOCHOW = ZipConstants.LOCHOW
        """
        LOC header field \"compression method\" offset.
        """
        LOCTIM = ZipConstants.LOCTIM
        """
        LOC header field \"modification time\" offset.
        """
        LOCCRC = ZipConstants.LOCCRC
        """
        LOC header field \"CRC of uncompressed data\" offset.
        """
        LOCSIZ = ZipConstants.LOCSIZ
        """
        LOC header field \"compressed data size\" offset.
        """
        LOCLEN = ZipConstants.LOCLEN
        """
        LOC header field \"uncompressed data size\" offset.
        """
        LOCNAM = ZipConstants.LOCNAM
        """
        LOC header field \"filename length\" offset.
        """
        LOCEXT = ZipConstants.LOCEXT
        """
        LOC header field \"extra field length\" offset.
        """
        EXTCRC = ZipConstants.EXTCRC
        """
        EXT header field \"CRC of uncompressed data\" offsets.
        """
        EXTSIZ = ZipConstants.EXTSIZ
        """
        EXT header field \"compressed size\" offsets.
        """
        EXTLEN = ZipConstants.EXTLEN
        """
        EXT header field \"uncompressed size\" offsets.
        """
        CENVEM = ZipConstants.CENVEM
        """
        CEN header field \"version made by\" offset.
        """
        CENVER = ZipConstants.CENVER
        """
        CEN header field \"version needed to extract\" offset.
        """
        CENFLG = ZipConstants.CENFLG
        """
        CEN header field \"general purpose bit flags\" offset.
        """
        CENHOW = ZipConstants.CENHOW
        """
        CEN header field \"compression method\" offset.
        """
        CENTIM = ZipConstants.CENTIM
        """
        CEN header field \"modification time\" offset.
        """
        CENDAT = ZipConstants.CENDAT
        """
        CEN header field \"modification time\" offset.
        """
        CENCRC = ZipConstants.CENCRC
        """
        CEN header field \"CRC of uncompressed data\" offset.
        """
        CENSIZ = ZipConstants.CENSIZ
        """
        CEN header field \"compressed size\" offset.
        """
        CENLEN = ZipConstants.CENLEN
        """
        CEN header field \"uncompressed size\" offset.
        """
        CENNAM = ZipConstants.CENNAM
        """
        CEN header field \"length of filename\" offset.
        """
        CENEXT = ZipConstants.CENEXT
        """
        CEN header field \"length of extra field\" offset.
        """
        CENCOM = ZipConstants.CENCOM
        """
        CEN header field \"file comment length\" offset.
        """
        CENDSK = ZipConstants.CENDSK
        """
        CEN header field \"disk number start\" offset.
        """
        CENATT = ZipConstants.CENATT
        """
        CEN header field \"internal file attributes\" offset.
        """
        CENATX = ZipConstants.CENATX
        """
        CEN header field \"external file attributes\" offset.
        """
        CENOFF = ZipConstants.CENOFF
        """
        CEN header field \"offset of local header\" offset.
        """
        ENDSUB = ZipConstants.ENDSUB
        """
        END header field \"number of entries on this disk\" offset.
        """
        ENDTOT = ZipConstants.ENDTOT
        """
        END header field \"total number of entries\" offset.
        """
        ENDSIZ = ZipConstants.ENDSIZ
        """
        END header field \"central directory size\" offset.
        """
        ENDOFF = ZipConstants.ENDOFF
        """
        END header field \"central directory offset\" offset.
        """
        ENDCOM = ZipConstants.ENDCOM
        """
        END header field \"size of zip file comment\" offset.
        """

__all__ = ['ZipConstants', 'ZipConstantsEnum']
