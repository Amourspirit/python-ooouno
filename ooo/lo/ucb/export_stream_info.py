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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..io.x_output_stream import XOutputStream as XOutputStream_a4e00b35


class ExportStreamInfo(object):
    """
    Struct Class

    information needed to export an object in mbx format (supplying an output stream to export into).

    See Also:
        `API ExportStreamInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1ExportStreamInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.ExportStreamInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.ExportStreamInfo'
    """Literal Constant ``com.sun.star.ucb.ExportStreamInfo``"""

    def __init__(self, Target: typing.Optional[XOutputStream_a4e00b35] = None, ForceBodies: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Target (XOutputStream, optional): Target value.
            ForceBodies (bool, optional): ForceBodies value.
        """
        super().__init__()

        if isinstance(Target, ExportStreamInfo):
            oth: ExportStreamInfo = Target
            self.Target = oth.Target
            self.ForceBodies = oth.ForceBodies
            return

        kargs = {
            "Target": Target,
            "ForceBodies": ForceBodies,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._target = kwargs["Target"]
        self._force_bodies = kwargs["ForceBodies"]


    @property
    def Target(self) -> XOutputStream_a4e00b35:
        """
        the output stream to export into.
        """
        return self._target
    
    @Target.setter
    def Target(self, value: XOutputStream_a4e00b35) -> None:
        self._target = value

    @property
    def ForceBodies(self) -> bool:
        """
        tries hard to make message (document) bodies available for export.
        """
        return self._force_bodies
    
    @ForceBodies.setter
    def ForceBodies(self, value: bool) -> None:
        self._force_bodies = value


__all__ = ['ExportStreamInfo']
