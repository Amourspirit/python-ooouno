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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.2
from ..sdbc.sql_exception import SQLException as SQLException_acc90b43

class RowSetVetoException(SQLException_acc90b43):
    """
    is an exception fired whenever a row set operation was cancelled because of of a veto of an approved listener.

    See Also:
        `API RowSetVetoException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdb_1_1RowSetVetoException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.RowSetVetoException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.sdb.RowSetVetoException'
    __pyunostruct__: str = 'com.sun.star.sdb.RowSetVetoException'

    typeName: str = 'com.sun.star.sdb.RowSetVetoException'
    """Literal Constant ``com.sun.star.sdb.RowSetVetoException``"""

    def __init__(self, **kwargs) -> None:
        """
        Constructor

        Keyword Arguments:

            Other ``*args`` and ``**kwargs`` are passed to parent class.
        """
        super().__init__(**kwargs)


