class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        ## I will just try to reduce the divisor from dividend
        ## getting the sign of the numbers
        sign = (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0)

        ## getting the absolute value
        a = abs(dividend)
        b = abs(divisor)
        result = 0

        ## until dividend is greater than divisor
        while a >= b:
            ## need to minus b from a
            decrease = b
            ## keeping a counter because if I continue to minus then I get TLE
            ## So I will make jumps as longs as possible
            ## 21 and 3 ; 21-3 then 18-6 then 12-12 like this
            count = 1

            while a >= decrease:
                ## reduce a
                a -= decrease

                ## add the number of reduction
                result += count
                ## count the number of reduction
                count += count
                ## make a 2x Jump
                decrease += decrease

        ## check the sign before returning
        output = result if not sign else -result

        ## Okay, had to get an error for this
        return min(max(-2147483648, output), 2147483647)
