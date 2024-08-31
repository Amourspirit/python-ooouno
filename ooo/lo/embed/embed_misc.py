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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.embed


class EmbedMisc(object):
    """
    Const Class

    The constant set contains flags describing miscellaneous characteristics of embedded objects.
    
    The constant values can be combined with \"or\" operation. The first 32 bits are reserved for MS values, they are added because this API is going to be used to embed MS OLE objects into OOo documents, so there should be a possibility to transfer all the possible MS flags to container. In case own specific values should be added those bits can not be used.

    See Also:
        `API EmbedMisc <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1embed_1_1EmbedMisc.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.EmbedMisc'
    __ooo_type_name__: str = 'const'

    MS_EMBED_RECOMPOSEONRESIZE = 1
    """
    means that the object wish to regenerate view representation if it's view in the container is resized.
    """
    MS_EMBED_ONLYICONIC = 2
    """
    The object has no view representation except icon.
    """
    MS_EMBED_INSERTNOTREPLACE = 4
    """
    If the object is generated from a selection, the selection should not be removed, the object should be inserted beside the selection.
    """
    MS_EMBED_STATIC = 8
    """
    The object is a static object that contains only representation.
    """
    MS_EMBED_CANTLINKINSIDE = 16
    MS_EMBED_CANLINKBYOLE1 = 32
    MS_EMBED_ISLINKOBJECT = 64
    MS_EMBED_INSIDEOUT = 128
    MS_EMBED_ACTIVATEWHENVISIBLE = 256
    MS_EMBED_RENDERINGISDEVICEINDEPENDENT = 512
    MS_EMBED_INVISIBLEATRUNTIME = 1024
    MS_EMBED_ALWAYSRUN = 2048
    MS_EMBED_ACTSLIKEBUTTON = 4096
    MS_EMBED_ACTSLIKELABEL = 8192
    MS_EMBED_NOUIACTIVATE = 16384
    MS_EMBED_ALIGNABLE = 32768
    MS_EMBED_SIMPLEFRAME = 65536
    MS_EMBED_SETCLIENTSITEFIRST = 131072
    MS_EMBED_IMEMODE = 262144
    MS_EMBED_IGNOREACTIVATEWHENVISIBLE = 524288
    MS_EMBED_WANTSTOMENUMERGE = 1048576
    MS_EMBED_SUPPORTSMULTILEVELUNDO = 2097152
    EMBED_ACTIVATEIMMEDIATELY = 4294967296
    EMBED_NEVERRESIZE = 8589934592
    EMBED_NEEDSSIZEONLOAD = 17179869184
    """
    The object needs the size to be provided from the container after it is loaded to function in optimal way.
    """

__all__ = ['EmbedMisc']
