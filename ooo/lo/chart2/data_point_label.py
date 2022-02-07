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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.2


class DataPointLabel(object):
    """
    Struct Class

    
    **since**
    
        LibreOffice 7.1

    See Also:
        `API DataPointLabel <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1DataPointLabel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.DataPointLabel'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart2.DataPointLabel'
    """Literal Constant ``com.sun.star.chart2.DataPointLabel``"""

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Other Arguments:
            First positinal arg can be another ``DataPointLabel`` instance,
                if it is the only argument passed to contructor;
                Otherwise, postitional arguments are treated as ``DataPointLabel``
                values. Following the order of ``Keyword Arguments``.

        Keyword Arguments:
            ShowNumber (bool, optional): ShowNumber value
            ShowNumberInPercent (bool, optional): ShowNumberInPercent value
            ShowCategoryName (bool, optional): ShowCategoryName value
            ShowLegendSymbol (bool, optional): ShowLegendSymbol value
            ShowCustomLabel (bool, optional): ShowCustomLabel value
            ShowSeriesName (bool, optional): ShowSeriesName value
        """
        self._show_number = None
        self._show_number_in_percent = None
        self._show_category_name = None
        self._show_legend_symbol = None
        self._show_custom_label = None
        self._show_series_name = None

        key_order = ('ShowNumber', 'ShowNumberInPercent', 'ShowCategoryName', 'ShowLegendSymbol', 'ShowCustomLabel', 'ShowSeriesName')
        arg_len = len(args)
        if arg_len == 1:
            if isinstance(args[0], DataPointLabel):
                oth = args[0]
                for key in key_order:
                    setattr(self, key, getattr(oth, key))
                return

        if  arg_len > len(key_order):
            raise ValueError("DataPointLabel.__init__() To many parameters")
        for i, arg in enumerate(args):
            setattr(self, key_order[i], arg)
        for k, v in kwargs.items():
            if k in key_order:
                setattr(self, k, v)


    @property
    def ShowNumber(self) -> bool:
        """
        if TRUE, the value that is represented by a data point is displayed next to it.
        """
        return self._show_number
    
    @ShowNumber.setter
    def ShowNumber(self, value: bool) -> None:
        self._show_number = value

    @property
    def ShowNumberInPercent(self) -> bool:
        """
        This is only effective, if ShowNumber is TRUE.
        
        If this member is also TRUE, the numbers are displayed as percentages of a category.
        
        That means, if a data point is the first one of a series, the percentage is calculated by using the first data points of all available series.
        """
        return self._show_number_in_percent
    
    @ShowNumberInPercent.setter
    def ShowNumberInPercent(self, value: bool) -> None:
        self._show_number_in_percent = value

    @property
    def ShowCategoryName(self) -> bool:
        """
        The caption contains the category name of the category to which a data point belongs.
        """
        return self._show_category_name
    
    @ShowCategoryName.setter
    def ShowCategoryName(self, value: bool) -> None:
        self._show_category_name = value

    @property
    def ShowLegendSymbol(self) -> bool:
        """
        The symbol of data series is additionally displayed in the caption.
        """
        return self._show_legend_symbol
    
    @ShowLegendSymbol.setter
    def ShowLegendSymbol(self, value: bool) -> None:
        self._show_legend_symbol = value

    @property
    def ShowCustomLabel(self) -> bool:
        """
        The caption contains a custom label text, which belongs to a data point label.
        
        **since**
        
            LibreOffice 7.1
        """
        return self._show_custom_label
    
    @ShowCustomLabel.setter
    def ShowCustomLabel(self, value: bool) -> None:
        self._show_custom_label = value

    @property
    def ShowSeriesName(self) -> bool:
        """
        The name of the data series is additionally displayed in the caption.
        
        **since**
        
            LibreOffice 7.2
        """
        return self._show_series_name
    
    @ShowSeriesName.setter
    def ShowSeriesName(self, value: bool) -> None:
        self._show_series_name = value


__all__ = ['DataPointLabel']
