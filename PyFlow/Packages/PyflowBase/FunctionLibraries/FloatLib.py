from math import pi
from numpy import sign

from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core.Common import *


class FloatLib(FunctionLibraryBase):
    '''doc string for FloatLib'''
    def __init__(self, packageName):
        super(FloatLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=('FloatPin', 0.0), meta={'Category': 'Math|Float', 'Keywords': ['lerp']})
    ## Linear interpolate
    def lerpf(a=('FloatPin', 0.0), b=('FloatPin', 0.0), alpha=('FloatPin', 0.0)):
        '''
        Linear interpolate
        '''
        return lerp(a, b, clamp(alpha, 0.0, 1.0))

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), meta={'Category': 'Math|Float', 'Keywords': []})
    def nearlyEqual(a=('FloatPin', 0.0), b=('FloatPin', 0.0), abs_tol=('FloatPin', 0.0)):
        return abs(a - b) < abs_tol

    @staticmethod
    @IMPLEMENT_NODE(returns=('FloatPin', 0.0), meta={'Category': 'Math|Float', 'Keywords': []})
    def multByPi(a=('FloatPin', 0.0)):
        '''
        Multiplies the input value by pi
        '''
        return a * pi

    @staticmethod
    @IMPLEMENT_NODE(returns=('FloatPin', 0.0), meta={'Category': 'Math|Float', 'Keywords': []})
    def normalizeToRange(Value=('FloatPin', 0.0), RangeMin=('FloatPin', 0.0), RangeMax=('FloatPin', 0.0)):
        '''
        Returns Value normalized to the given range. (e.g. 20 normalized to the range 10->50 would result in 0.25)
        '''
        if RangeMin == RangeMax:
            return RangeMin

        if RangeMin > RangeMax:
            RangeMin, RangeMax = RangeMax, RangeMin
        return (Value - RangeMin) / (RangeMax - RangeMin)

    @staticmethod
    @IMPLEMENT_NODE(returns=('FloatPin', 0.0), meta={'Category': 'Math|Float', 'Keywords': []})
    def selectFloat(A=('FloatPin', 0.0), B=('FloatPin', 0.0), PickA=('BoolPin', False)):
        '''
        If bPickA is true, A is returned, otherwise B is
        '''
        return A if PickA else B

    @staticmethod
    @IMPLEMENT_NODE(returns=('FloatPin', 0.0), meta={'Category': 'Math|Float', 'Keywords': []})
    def signf(a=('FloatPin', 0.0)):
        '''
        Returns -1 if x &lt; 0, 0 if x==0, 1 if x &gt; 0
        '''
        return float(sign(a))

    @staticmethod
    @IMPLEMENT_NODE(returns=('FloatPin', 0.0), meta={'Category': 'Math|Float', 'Keywords': []})
    def roundf(Value=('FloatPin', 0.0), Digits=('IntPin', 1)):
        '''
        Round a number to a given precision in decimal digits (default 0 digits)
        '''
        return round(Value, Digits)

    @staticmethod
    @IMPLEMENT_NODE(returns=('FloatPin', 0.0), meta={'Category': 'Math|Float', 'Keywords': []})
    def arraySum(Value=('FloatPin', [])):
        '''
        Sum of list of floats
        '''
        return sum(Value)
