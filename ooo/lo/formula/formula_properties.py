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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.formula
from abc import abstractproperty, ABC

class FormulaProperties(ABC):
    """
    Service Class

    The formula properties provide access to the properties of a formula in a formula generator.
    
    **since**
    
        OOo 3.4

    See Also:
        `API FormulaProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1formula_1_1FormulaProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.formula'
    __ooo_full_ns__: str = 'com.sun.star.formula.FormulaProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Alignment(self) -> int:
        """
        contains the alignment of the formula.
        """
        ...

    @abstractproperty
    def BaseFontHeight(self) -> int:
        """
        contains the base font height in point the formula will be formatted in.
        
        All properties containing relative values are related to this value.
        """
        ...

    @abstractproperty
    def BaseLine(self) -> int:
        """
        contains the baselines offset in respect to the top of the formula rectangle
        
        **since**
        
            OOo 3.4
        """
        ...

    @abstractproperty
    def BottomMargin(self) -> int:
        """
        contains the metric value of the bottom margin of the formula.
        """
        ...

    @abstractproperty
    def CustomFontNameFixed(self) -> str:
        """
        customized name for fixed font.
        """
        ...

    @abstractproperty
    def CustomFontNameSans(self) -> str:
        """
        customized name for sans serif font
        """
        ...

    @abstractproperty
    def CustomFontNameSerif(self) -> str:
        """
        customized name for serif font
        """
        ...

    @abstractproperty
    def FontFixedIsBold(self) -> bool:
        """
        determines if the customized fixed font is bold.
        """
        ...

    @abstractproperty
    def FontFixedIsItalic(self) -> bool:
        """
        determines if the customized fixed font is italic.
        """
        ...

    @abstractproperty
    def FontFunctionsIsBold(self) -> bool:
        """
        determines if the font that is used to display functions is bold.
        """
        ...

    @abstractproperty
    def FontFunctionsIsItalic(self) -> bool:
        """
        determines if the font that is used to display functions is italic.
        """
        ...

    @abstractproperty
    def FontNameFunctions(self) -> str:
        """
        contains the name of the font that is used to display functions contained in the formula.
        """
        ...

    @abstractproperty
    def FontNameNumbers(self) -> str:
        """
        contains the name of the font that is used to display numbers contained in the formula.
        """
        ...

    @abstractproperty
    def FontNameText(self) -> str:
        """
        contains the name of the font that is used to display text contained in the formula.
        """
        ...

    @abstractproperty
    def FontNameVariables(self) -> str:
        """
        contains the name of the font that is used to display variables contained in the formula.
        """
        ...

    @abstractproperty
    def FontNumbersIsBold(self) -> bool:
        """
        determines if the font that is used to display numbers is bold.
        """
        ...

    @abstractproperty
    def FontNumbersIsItalic(self) -> bool:
        """
        determines if the font that is used to display numbers is italic.
        """
        ...

    @abstractproperty
    def FontSansIsBold(self) -> bool:
        """
        determines if the customized sans serif font is bold.
        """
        ...

    @abstractproperty
    def FontSansIsItalic(self) -> bool:
        """
        determines if the customized sans serif font is italic.
        """
        ...

    @abstractproperty
    def FontSerifIsBold(self) -> bool:
        """
        determines if the customized serif font is bold.
        """
        ...

    @abstractproperty
    def FontSerifIsItalic(self) -> bool:
        """
        determines if the customized serif font is italic.
        """
        ...

    @abstractproperty
    def FontTextIsBold(self) -> bool:
        """
        determines if the font that is used to display text is bold.
        """
        ...

    @abstractproperty
    def FontTextIsItalic(self) -> bool:
        """
        determines if the font that is used to display text is italic.
        """
        ...

    @abstractproperty
    def FontVariablesIsBold(self) -> bool:
        """
        determines if the font that is used to display variables is bold.
        """
        ...

    @abstractproperty
    def FontVariablesIsItalic(self) -> bool:
        """
        determines if the font that is used to display variables is italic.
        """
        ...

    @abstractproperty
    def Formula(self) -> str:
        """
        contains the command string of the formula
        """
        ...

    @abstractproperty
    def IsScaleAllBrackets(self) -> bool:
        """
        decides if all brackets (even those without \"left\"/\"right\" modifier) are scaled.
        """
        ...

    @abstractproperty
    def IsTextMode(self) -> bool:
        """
        switches into text mode.
        
        This is a mode where formulas are displayed the same height as a line of text.
        """
        ...

    @abstractproperty
    def LeftMargin(self) -> int:
        """
        contains the metric value of the left margin of the formula.
        """
        ...

    @abstractproperty
    def RelativeBracketDistance(self) -> int:
        """
        contains the relative distance of brackets.
        """
        ...

    @abstractproperty
    def RelativeBracketExcessSize(self) -> int:
        """
        contains the relative excess size of brackets.
        """
        ...

    @abstractproperty
    def RelativeFontHeightFunctions(self) -> int:
        """
        contains the relative height of the font for functions.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...

    @abstractproperty
    def RelativeFontHeightIndices(self) -> int:
        """
        contains the relative height of the font for indices.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...

    @abstractproperty
    def RelativeFontHeightLimits(self) -> int:
        """
        contains the relative height of the font for limits.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...

    @abstractproperty
    def RelativeFontHeightOperators(self) -> int:
        """
        contains the relative height of the font for operators.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...

    @abstractproperty
    def RelativeFontHeightText(self) -> int:
        """
        contains the relative height of the font for text.
        
        The values unit is percent of the com.sun.star.formula.FormulaProperties.BaseFontHeight
        """
        ...

    @abstractproperty
    def RelativeFractionBarExcessLength(self) -> int:
        """
        contains the relative excess length of a fraction bar.
        """
        ...

    @abstractproperty
    def RelativeFractionBarLineWeight(self) -> int:
        """
        contains the relative line weight of a fraction bar.
        """
        ...

    @abstractproperty
    def RelativeFractionDenominatorDepth(self) -> int:
        """
        contains the relative depth of the denominator of a fraction
        """
        ...

    @abstractproperty
    def RelativeFractionNumeratorHeight(self) -> int:
        """
        contains the relative height of the numerator of a fraction.
        """
        ...

    @abstractproperty
    def RelativeIndexSubscript(self) -> int:
        """
        contains the relative superscript of indices.
        """
        ...

    @abstractproperty
    def RelativeIndexSuperscript(self) -> int:
        """
        contains the relative subscript of indices.
        """
        ...

    @abstractproperty
    def RelativeLineSpacing(self) -> int:
        """
        contains the relative line spacing.
        """
        ...

    @abstractproperty
    def RelativeLowerLimitDistance(self) -> int:
        """
        contains the relative distance of lower limits.
        """
        ...

    @abstractproperty
    def RelativeMatrixColumnSpacing(self) -> int:
        """
        contains the relative column spacing of matrices.
        """
        ...

    @abstractproperty
    def RelativeMatrixLineSpacing(self) -> int:
        """
        contains the relative line spacing of matrices.
        """
        ...

    @abstractproperty
    def RelativeOperatorExcessSize(self) -> int:
        """
        contains the relative excess of operators.
        """
        ...

    @abstractproperty
    def RelativeOperatorSpacing(self) -> int:
        """
        contains the relative spacing of operators.
        """
        ...

    @abstractproperty
    def RelativeRootSpacing(self) -> int:
        """
        contains the relative root spacing
        """
        ...

    @abstractproperty
    def RelativeScaleBracketExcessSize(self) -> int:
        """
        contains the relative scaling of the bracket excess.
        """
        ...

    @abstractproperty
    def RelativeSpacing(self) -> int:
        """
        contains the relative spacing.
        """
        ...

    @abstractproperty
    def RelativeSymbolMinimumHeight(self) -> int:
        """
        contains the relative minimum height of the formula.
        """
        ...

    @abstractproperty
    def RelativeSymbolPrimaryHeight(self) -> int:
        """
        contains the relative primary height of symbols.
        """
        ...

    @abstractproperty
    def RelativeUpperLimitDistance(self) -> int:
        """
        contains the relative distance of upper limits
        """
        ...

    @abstractproperty
    def RightMargin(self) -> int:
        """
        contains the metric value of the right margin of the formula.
        """
        ...

    @abstractproperty
    def TopMargin(self) -> int:
        """
        contains the metric value of the top margin of the formula.
        """
        ...



__all__ = ['FormulaProperties']

