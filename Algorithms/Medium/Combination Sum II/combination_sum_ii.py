from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = set()

        def c(index, target, subCombinations):
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] >= target:
                    if candidates[i] == target:
                        combinations.add(
                            tuple(subCombinations + [candidates[i]]))
                    break

                c(i+1, target - candidates[i],
                  [candidates[i]] + subCombinations)

        c(0, target, [])
        return [list(x) for x in combinations]


candidates = [1, 1, 2, 5, 6, 7, 10]
target = 8

print(Solution().combinationSum2(candidates, target))
