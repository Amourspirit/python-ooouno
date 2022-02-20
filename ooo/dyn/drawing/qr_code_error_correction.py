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
# Namespace: com.sun.star.drawing
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.drawing import QRCodeErrorCorrection as QRCodeErrorCorrection
    if hasattr(QRCodeErrorCorrection, '_constants') and isinstance(QRCodeErrorCorrection._constants, dict):
        QRCodeErrorCorrection._constants['__ooo_ns__'] = 'com.sun.star.drawing'
        QRCodeErrorCorrection._constants['__ooo_full_ns__'] = 'com.sun.star.drawing.QRCodeErrorCorrection'
        QRCodeErrorCorrection._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global QRCodeErrorCorrectionEnum
        ls = [f for f in dir(QRCodeErrorCorrection) if not callable(getattr(QRCodeErrorCorrection, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(QRCodeErrorCorrection, name)
        QRCodeErrorCorrectionEnum = IntEnum('QRCodeErrorCorrectionEnum', _dict)
    build_enum()
else:
    from ...lo.drawing.qr_code_error_correction import QRCodeErrorCorrection as QRCodeErrorCorrection

    class QRCodeErrorCorrectionEnum(IntEnum):
        """
        Enum of Const Class QRCodeErrorCorrection

        These constants identify the type of Error Correction for a QR Code.
        
        The Error Correction for a QR code is a measure that helps a QR code to recover, if it is destroyed.
        
        Level L (Low) 7% of codewords can be restored. Level M (Medium) 15% of codewords can be restored. Level Q (Quartile) 25% of codewords can be restored. Level H (High) 30% of codewords can be restored.
        
        More Info - here
        
        **since**
        
            LibreOffice 6.4
        """
        LOW = QRCodeErrorCorrection.LOW
        MEDIUM = QRCodeErrorCorrection.MEDIUM
        QUARTILE = QRCodeErrorCorrection.QUARTILE
        HIGH = QRCodeErrorCorrection.HIGH

__all__ = ['QRCodeErrorCorrection', 'QRCodeErrorCorrectionEnum']
