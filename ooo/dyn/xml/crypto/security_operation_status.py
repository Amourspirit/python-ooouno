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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.xml.crypto
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
from enum import Enum
from ooo.oenv import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import uno_enum_class_new
    from com.sun.star.xml.crypto.SecurityOperationStatus import (ASSERTION, CERT_HAS_EXPIRED, CERT_ISSUER_FAILED, CERT_NOT_FOUND, CERT_NOT_YET_VALID, CERT_REVOKED, CERT_VERIFY_FAILED, CRYPTO_FAILED, DATA_NOT_MATCH, DISABLED, DSIG_INVALID_REFERENCE, DSIG_NO_REFERENCES, ENGINE_FAILED, INVALID_DATA, INVALID_FORMAT, INVALID_KEY_DATA, INVALID_KEY_DATA_SIZE, INVALID_NODE, INVALID_NODE_ATTRIBUTE, INVALID_NODE_CONTENT, INVALID_OPERATION, INVALID_RESULT, INVALID_SIZE, INVALID_STATUS, INVALID_TRANSFORM, INVALID_TRANSFORM_KEY, INVALID_TYPE, INVALID_URI_TYPE, IO_FAILED, KEYDATA_DISABLED, KEY_DATA_ALREADY_EXIST, KEY_DATA_NOT_FOUND, KEY_NOT_FOUND, MALLOC_FAILED, MAX_ENCKEY_LEVEL, MAX_RETRIEVALS_LEVEL, MAX_RETRIEVAL_TYPE_MISMATCH, MISSING_NODE_ATTRIBUTE, NODE_ALREADY_PRESENT, NODE_NOT_FOUND, NOT_IMPLEMENTED, OPERATION_SUCCEEDED, RUNTIMEERROR_FAILED, STRDUP_FAILED, TRANSFORM_DISABLED, TRANSFORM_SAME_DOCUMENT_REQUIRED, UNEXPECTED_NODE, UNKNOWN, XML_FAILED, XSLT_FAILED)

    def _dynamic_enum():
        # Dynamically create class that actually contains UNO enum instances
        global SecurityOperationStatus
        _dict = {
            "ASSERTION": ASSERTION,
            "CERT_HAS_EXPIRED": CERT_HAS_EXPIRED,
            "CERT_ISSUER_FAILED": CERT_ISSUER_FAILED,
            "CERT_NOT_FOUND": CERT_NOT_FOUND,
            "CERT_NOT_YET_VALID": CERT_NOT_YET_VALID,
            "CERT_REVOKED": CERT_REVOKED,
            "CERT_VERIFY_FAILED": CERT_VERIFY_FAILED,
            "CRYPTO_FAILED": CRYPTO_FAILED,
            "DATA_NOT_MATCH": DATA_NOT_MATCH,
            "DISABLED": DISABLED,
            "DSIG_INVALID_REFERENCE": DSIG_INVALID_REFERENCE,
            "DSIG_NO_REFERENCES": DSIG_NO_REFERENCES,
            "ENGINE_FAILED": ENGINE_FAILED,
            "INVALID_DATA": INVALID_DATA,
            "INVALID_FORMAT": INVALID_FORMAT,
            "INVALID_KEY_DATA": INVALID_KEY_DATA,
            "INVALID_KEY_DATA_SIZE": INVALID_KEY_DATA_SIZE,
            "INVALID_NODE": INVALID_NODE,
            "INVALID_NODE_ATTRIBUTE": INVALID_NODE_ATTRIBUTE,
            "INVALID_NODE_CONTENT": INVALID_NODE_CONTENT,
            "INVALID_OPERATION": INVALID_OPERATION,
            "INVALID_RESULT": INVALID_RESULT,
            "INVALID_SIZE": INVALID_SIZE,
            "INVALID_STATUS": INVALID_STATUS,
            "INVALID_TRANSFORM": INVALID_TRANSFORM,
            "INVALID_TRANSFORM_KEY": INVALID_TRANSFORM_KEY,
            "INVALID_TYPE": INVALID_TYPE,
            "INVALID_URI_TYPE": INVALID_URI_TYPE,
            "IO_FAILED": IO_FAILED,
            "KEYDATA_DISABLED": KEYDATA_DISABLED,
            "KEY_DATA_ALREADY_EXIST": KEY_DATA_ALREADY_EXIST,
            "KEY_DATA_NOT_FOUND": KEY_DATA_NOT_FOUND,
            "KEY_NOT_FOUND": KEY_NOT_FOUND,
            "MALLOC_FAILED": MALLOC_FAILED,
            "MAX_ENCKEY_LEVEL": MAX_ENCKEY_LEVEL,
            "MAX_RETRIEVALS_LEVEL": MAX_RETRIEVALS_LEVEL,
            "MAX_RETRIEVAL_TYPE_MISMATCH": MAX_RETRIEVAL_TYPE_MISMATCH,
            "MISSING_NODE_ATTRIBUTE": MISSING_NODE_ATTRIBUTE,
            "NODE_ALREADY_PRESENT": NODE_ALREADY_PRESENT,
            "NODE_NOT_FOUND": NODE_NOT_FOUND,
            "NOT_IMPLEMENTED": NOT_IMPLEMENTED,
            "OPERATION_SUCCEEDED": OPERATION_SUCCEEDED,
            "RUNTIMEERROR_FAILED": RUNTIMEERROR_FAILED,
            "STRDUP_FAILED": STRDUP_FAILED,
            "TRANSFORM_DISABLED": TRANSFORM_DISABLED,
            "TRANSFORM_SAME_DOCUMENT_REQUIRED": TRANSFORM_SAME_DOCUMENT_REQUIRED,
            "UNEXPECTED_NODE": UNEXPECTED_NODE,
            "UNKNOWN": UNKNOWN,
            "XML_FAILED": XML_FAILED,
            "XSLT_FAILED": XSLT_FAILED,
        }

        SecurityOperationStatus = type('SecurityOperationStatus', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(SecurityOperationStatus, k, v)
        setattr(SecurityOperationStatus, '__ooo_ns__', 'com.sun.star.xml.crypto')
        setattr(SecurityOperationStatus, '__ooo_full_ns__', 'com.sun.star.xml.crypto.SecurityOperationStatus')
        setattr(SecurityOperationStatus, '__ooo_type_name__', 'enum')
    _dynamic_enum()
else:
    from ....lo.xml.crypto.security_operation_status import SecurityOperationStatus as SecurityOperationStatus

__all__ = ['SecurityOperationStatus']

