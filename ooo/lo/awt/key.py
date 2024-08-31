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
# Namespace: com.sun.star.awt


class Key(object):
    """
    Const Class

    These values are used to specify distinct physical keys, plus some special values used by the macOS implementation.
    
    Noting that these numbers are simply allocated here, and not taken from any specification.
    
    **since**
    
        LibreOffice 7.6

    See Also:
        `API Key <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1Key.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.Key'
    __ooo_type_name__: str = 'const'

    NUM0 = 256
    NUM1 = 257
    NUM2 = 258
    NUM3 = 259
    NUM4 = 260
    NUM5 = 261
    NUM6 = 262
    NUM7 = 263
    NUM8 = 264
    NUM9 = 265
    A = 512
    B = 513
    C = 514
    D = 515
    E = 516
    F = 517
    G = 518
    H = 519
    I = 520
    J = 521
    K = 522
    L = 523
    M = 524
    N = 525
    O = 526
    P = 527
    Q = 528
    R = 529
    S = 530
    T = 531
    U = 532
    V = 533
    W = 534
    X = 535
    Y = 536
    Z = 537
    F1 = 768
    F2 = 769
    F3 = 770
    F4 = 771
    F5 = 772
    F6 = 773
    F7 = 774
    F8 = 775
    F9 = 776
    F10 = 777
    F11 = 778
    F12 = 779
    F13 = 780
    F14 = 781
    F15 = 782
    F16 = 783
    F17 = 784
    F18 = 785
    F19 = 786
    F20 = 787
    F21 = 788
    F22 = 789
    F23 = 790
    F24 = 791
    F25 = 792
    F26 = 793
    DOWN = 1024
    UP = 1025
    LEFT = 1026
    RIGHT = 1027
    HOME = 1028
    END = 1029
    PAGEUP = 1030
    PAGEDOWN = 1031
    RETURN = 1280
    ESCAPE = 1281
    TAB = 1282
    BACKSPACE = 1283
    SPACE = 1284
    INSERT = 1285
    DELETE = 1286
    ADD = 1287
    SUBTRACT = 1288
    MULTIPLY = 1289
    DIVIDE = 1290
    POINT = 1291
    COMMA = 1292
    LESS = 1293
    GREATER = 1294
    EQUAL = 1295
    OPEN = 1296
    CUT = 1297
    COPY = 1298
    PASTE = 1299
    UNDO = 1300
    REPEAT = 1301
    FIND = 1302
    PROPERTIES = 1303
    FRONT = 1304
    CONTEXTMENU = 1305
    HELP = 1306
    MENU = 1307
    HANGUL_HANJA = 1308
    DECIMAL = 1309
    TILDE = 1310
    QUOTELEFT = 1311
    CAPSLOCK = 1312
    NUMLOCK = 1313
    SCROLLLOCK = 1314
    DELETE_TO_BEGIN_OF_LINE = 1536
    DELETE_TO_END_OF_LINE = 1537
    DELETE_TO_BEGIN_OF_PARAGRAPH = 1538
    BRACKETLEFT = 1315
    BRACKETRIGHT = 1316
    SEMICOLON = 1317
    QUOTERIGHT = 1318
    RIGHTCURLYBRACKET = 1319
    COLON = 1320
    NUMBERSIGN = 191
    XF86FORWARD = 167
    XF86BACK = 166
    DELETE_TO_END_OF_PARAGRAPH = 1539
    """
    The following values don't correspond to physical keys on any keyboard but are used in the macOS implementation of VCL.
    
    They correspond to some of the action messages of the NSResponder abstract class.
    """
    DELETE_WORD_BACKWARD = 1540
    DELETE_WORD_FORWARD = 1541
    INSERT_LINEBREAK = 1542
    INSERT_PARAGRAPH = 1543
    MOVE_WORD_BACKWARD = 1544
    MOVE_WORD_FORWARD = 1545
    MOVE_TO_BEGIN_OF_LINE = 1546
    MOVE_TO_END_OF_LINE = 1547
    MOVE_TO_BEGIN_OF_PARAGRAPH = 1548
    MOVE_TO_END_OF_PARAGRAPH = 1549
    SELECT_BACKWARD = 1550
    SELECT_FORWARD = 1551
    SELECT_WORD_BACKWARD = 1552
    SELECT_WORD_FORWARD = 1553
    SELECT_WORD = 1554
    SELECT_LINE = 1555
    SELECT_PARAGRAPH = 1556
    SELECT_ALL = 1557
    SELECT_TO_BEGIN_OF_LINE = 1558
    SELECT_TO_END_OF_LINE = 1559
    MOVE_TO_BEGIN_OF_DOCUMENT = 1560
    MOVE_TO_END_OF_DOCUMENT = 1561
    SELECT_TO_BEGIN_OF_DOCUMENT = 1562
    SELECT_TO_END_OF_DOCUMENT = 1563
    SELECT_TO_BEGIN_OF_PARAGRAPH = 1564
    SELECT_TO_END_OF_PARAGRAPH = 1565

__all__ = ['Key']
