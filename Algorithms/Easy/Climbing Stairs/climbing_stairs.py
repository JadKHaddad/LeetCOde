class Solution:
    def climbStairs(self, n: int) -> int:
        def fac(n: int) -> int:
            if n < 1:
                return 1
            return n * fac(n - 1)

        ones = n
        sum, twos = (0, 0)
        while ones > -1:
            perm = fac(ones + twos) // (fac(ones) * fac(twos))
            sum = sum + perm
            ones = ones - 2
            twos = twos + 1
        return sum


print(Solution().climbStairs(6))
