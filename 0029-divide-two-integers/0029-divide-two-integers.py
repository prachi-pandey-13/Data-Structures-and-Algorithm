class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        quotient = 0
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        sign = (divisor < 0) ^ (dividend < 0) 
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << (1 + shift)):
                shift += 1
            quotient += 1 << shift
            dividend -= divisor << shift
        if sign:
            return -quotient
        return quotient

