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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.io
from __future__ import annotations
from .x_active_data_source import XActiveDataSource as XActiveDataSource_d1900c7f
from .x_text_output_stream import XTextOutputStream as XTextOutputStream_d55f0cda

class XTextOutputStream2(XActiveDataSource_d1900c7f, XTextOutputStream_d55f0cda):
    """
    Provides a unified interface for the new-style service TextOutputStream.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XTextOutputStream2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XTextOutputStream2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XTextOutputStream2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XTextOutputStream2'


__all__ = ['XTextOutputStream2']

