'''Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1


        def recurse(x, n):
            if n==0:
                return 1
            if n == 1:
                return x
            new_pow = n//2
            val = recurse(x, new_pow)
            return val * val * recurse(x, n%2)

        if n < 0:
            return 1/recurse(x, abs(n)) 
        if n > 0:
            return recurse(x, n)