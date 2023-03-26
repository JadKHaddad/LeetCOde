class Solution:
    def climbStairs(self, n: int) -> int:
        cache: dict[int, int] = {}

        def fac(n: int) -> int:
            if n < 1:
                return 1

            if n in cache:
                return cache[n]

            cache[n] = n * fac(n - 1)

            return cache[n]

        ones = n
        twos = 0
        sum = 0

        while ones > -1:
            perm = fac(ones + twos) // (fac(ones) * fac(twos))
            sum += perm
            ones -= 2
            twos += 1

        return sum


print(Solution().climbStairs(6))
