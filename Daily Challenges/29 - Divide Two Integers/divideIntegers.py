class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 0:
            return float('inf')
        
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quo = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            quo += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)
        
        if negative:
            quo = -quo
        return min(max(-2147483648, quo), 2147483647)
