from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def c(index, target, subCombinations):
            for i in range(index, len(candidates)):
                if candidates[i] >= target:
                    if candidates[i] == target:
                        subCombinations.append(candidates[i])
                        combinations.append(subCombinations)
                    break
                c(i, target - candidates[i], [candidates[i]] + subCombinations)

        c(0, target, [])
        return combinations


candidates = [1, 2, 3, 7, 6]
target = 7

print(Solution().combinationSum(candidates, target))
