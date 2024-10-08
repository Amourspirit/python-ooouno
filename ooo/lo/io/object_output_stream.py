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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.io
from __future__ import annotations
from .x_active_data_source import XActiveDataSource as XActiveDataSource_d1900c7f
from .x_connectable import XConnectable as XConnectable_980a0a96
from .x_object_output_stream import XObjectOutputStream as XObjectOutputStream_ee190d8c

class ObjectOutputStream(XActiveDataSource_d1900c7f, XConnectable_980a0a96, XObjectOutputStream_ee190d8c):
    """
    Service Class

    is a stream which allows writing the data of persistent objects.
    
    Implementations of this service must fulfill the specifications of the DataOutputStream service; furthermore, the stream needs to be chained to a XMarkableStream. Therefore, it also provides the XMarkableStream interface, but it delegates the calls to the chained object. The written objects are held until this instance is destroyed. The references to the objects are written as four-byte integers and begin at 1. Data format is written:

    See Also:
        `API ObjectOutputStream <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1io_1_1ObjectOutputStream.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.ObjectOutputStream'
    __ooo_type_name__: str = 'service'


__all__ = ['ObjectOutputStream']

