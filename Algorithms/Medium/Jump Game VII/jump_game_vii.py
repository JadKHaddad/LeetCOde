# slow
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != "0":
            return False
        cache = {}

        def c(index):
            if index == len(s) - 1:
                return True
            if index in cache:
                return False
            for i in range(index + minJump, min(index + maxJump + 1, len(s))):
                if s[i] == "0" and c(i):
                    return True
            cache[index] = None
            return False
            
        return c(0)


# dp, Internet
class Solution:
    def canReach(self, s, minJump, maxJump):
        n, count = len(s), 1
        dp = [True] + [False]*(n-1)
        for i in range(minJump, n):
            if (s[i] == "0" and count > 0):
                dp[i] = True
            if (i - maxJump >= 0 and dp[i - maxJump] == True):
                count -= 1
            if (dp[i - minJump + 1] == True):
                count += 1
        return dp[-1]


s = "0110111001010000"
minJump = 2
maxJump = 4

print(Solution().canReach(s, minJump, maxJump))
