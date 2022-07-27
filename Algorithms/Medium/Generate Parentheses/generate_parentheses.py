from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        combos = {1: {"()"}}
        for i in range(2, n + 1):
            combos[i] = set()
            for combo in combos[i - 1]:
                combos[i].add("(" + combo + ")")
            for j in range(1, i):
                for combo in combos[j]:
                    for combo_ in combos[i - j]:
                        combos[i].add(combo + combo_)
        return list(combos[n])


n = 4
print(Solution().generateParenthesis(n))
