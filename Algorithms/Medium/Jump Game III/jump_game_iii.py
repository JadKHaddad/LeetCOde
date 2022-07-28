from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = {}

        def can_reach(start: int) -> bool:
            if start in seen or start < 0 or start > len(arr) - 1:
                return False
            if arr[start] == 0:
                return True
            seen[start] = None
            return can_reach(start - arr[start]) or can_reach(start + arr[start])

        return can_reach(start)


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5

print(Solution().canReach(arr, start))
