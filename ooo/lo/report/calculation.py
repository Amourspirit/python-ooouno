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
# Namespace: com.sun.star.report


class Calculation(object):
    """
    Const Class

    Specifies how to calculate a value.

    See Also:
        `API Calculation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1report_1_1Calculation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.Calculation'
    __ooo_type_name__: str = 'const'

    NONE = 0
    """
    returns the average of a field.
    """
    AVERAGE = 1
    """
    returns the average of a field.
    """
    CORRELATION = 2
    """
    returns the correlation of two fields.
    """
    COUNT = 3
    """
    counts the number of values, from the field.
    """
    COVARIANCE = 4
    """
    returns the measure of the linear relation between paired variables.
    """
    DISTINCTCOUNT = 5
    """
    returns the number of none repeating values, from the field.
    """
    MAXIMUM = 6
    """
    returns the largest value from the field.
    """
    MEDIAN = 7
    """
    returns the middle value in a sequence of numeric values.
    """
    MINIMUM = 8
    """
    returns the smallest value from the field.
    """
    MODE = 9
    """
    returns the most frequently returning value from the field.
    """
    NTHLARGEST = 10
    """
    returns the Nth largest value from the field.
    """
    NTHMOSTFREQUENT = 11
    """
    returns the Nth most commonly occurring value from the field.
    """
    NTHSMALLEST = 12
    """
    returns the Nth smallest value from the field.
    """
    PERCENTAGE = 13
    """
    returns as a percentage of the grand total summary.
    """
    PERCENTILE = 14
    """
    returns the value for a specified percentile in a Number or Currency field.
    """
    POPSTANDARDDEVIATION = 15
    """
    returns how much each value in the field deviate from the mean or average value for that field.
    """
    POPVARIANCE = 16
    """
    returns the square of the standard deviation.
    """
    SAMPLESTANDARDDEVIATION = 17
    """
    returns the sample standard deviation for the field.
    """
    SAMPLEVARIANCE = 18
    """
    returns the sample variance for the field.
    """
    SUM = 19
    """
    returns the total of all the values for the field.
    """
    WEIGHTEDAVG = 20
    """
    returns the weighted average for the field.
    """

__all__ = ['Calculation']