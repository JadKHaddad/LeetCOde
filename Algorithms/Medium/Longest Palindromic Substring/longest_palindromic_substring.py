class Solution:
    def longestPalindrome(self, s: str) -> str:
        stack = []
        m = (0, 0)
        for i in range(0, len(s)):
            print(s[i])
            stack.append([i])
            if i < 1:
                continue
            if s[i] == s[i - 1]:
                stack[i].append(i - 1)
                if m[1] - m[0] < 1:
                    m = (i - 1, i)
            for index in stack[i - 1]:
                if index - 1 < 0:
                    break
                if s[i] == s[index - 1]:
                    stack[i].append(index - 1)
                    if m[1] - m[0] < i - (index - 1):
                        m = (index - 1, i)
        return s[m[0]: m[1] + 1]


s = "bababd"

print(Solution().longestPalindrome(s))
